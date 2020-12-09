#!/usr/bin/env python3

import networkx as nx
import collections 
import numpy as np
from scipy.stats import cauchy
from sklearn.isotonic import IsotonicRegression  
from sklearn.linear_model import LinearRegression 
import matplotlib
import matplotlib.pyplot as plt
from qpsolvers import solve_qp
from scipy.special import comb
from collections import defaultdict
import time



#utility functions
def getSortedDegSeq(G):
    degSeq = sorted([d for n, d in G.degree()], reverse=False) #small to large degrees
    return degSeq

def getDegHis(G,maxDeg):
    degSeq = getSortedDegSeq(G)
    degreeCount = collections.Counter(degSeq)
    degHis = np.zeros(maxDeg+1)
    for deg in degreeCount:
        degHis[deg]=degreeCount[deg]    
    return degHis

def degSeqToDegHis(degSeq, maxDeg):
    #assume deg sequence could be non-integer and be bigger than maxDegree
    degHis = np.zeros(maxDeg+1)
    for deg in degSeq:
        #print(deg)
        deg = int(round(deg))
        if deg <= maxDeg:
            degHis[deg]= degHis[deg]+1
    return degHis
    
    
def pdfToCdf(pdf):
    cdf = np.zeros(len(pdf))
    cdf[0] = pdf[0]
    for i in range(1,len(pdf)):
         cdf[i] = cdf[i-1] + pdf[i]            
    return cdf

def cdfToPdf(cdf):
    pdf = np.zeros(len(cdf))
    pdf[0] = cdf[0]
    for i in range(1,len(pdf)):
         pdf[i] = cdf[i] - cdf[i-1]            
    return pdf
    

def difDegHis_L1(his1,his2):
    #assume the same length
    return sum(abs(his1 - his2))

def difDegHis_L2(his1,his2):
    return sum(np.square(his1-his2))



def plotHis(trueHis,noisyHis):
    plt.plot(trueHis,'-g', label='trueHis')
    plt.plot(noisyHis,'--r', label='noisyHis')
    plt.legend();
    plt.xscale('log')

    
def plotCum(trueHis,noisyHis):
    plt.plot(pdfToCdf(trueHis), '3b', label='trueCum')
    plt.plot(pdfToCdf(noisyHis), '2y', label='noisyCum')
    plt.legend();
    plt.xscale('log')

#DP basic functions
def lap(trueCounts, sens, epsilon):
    scale = 1.0* sens/epsilon
    noisyCounts = trueCounts + np.random.laplace(0.0, scale, len(trueCounts))
    return noisyCounts

def postprocessCdf(noisyCdf, totalCount):
    #apply isotonic regression
    ir = IsotonicRegression(y_min=0, y_max=totalCount, increasing=True)
    cdf= ir.fit_transform(X=range(len(noisyCdf)),y=noisyCdf)   
    return cdf

def postprocessPdf(noisyPdf, nodesNum):
    cdf = pdfToCdf(noisyPdf)
    cdf = postprocessCdf(cdf, nodesNum)
    pdf = cdfToPdf(cdf)
    return pdf


def extendHis(his,maxDeg):
    #his has a shortern length 
    if (maxDeg+1) > len(his):
        hisExtended = np.zeros(maxDeg + 1)
        hisExtended[0:len(his)] = his
        return hisExtended
    else:
        return his

    
def sampleProbList(probList):
    #print(probList)
    normalizedProbList = probList/sum(probList)
    #print(normalizedProbList)
    r = np.random.uniform(0,1,1)
    s = 0 
    for i in range(len(probList)):
        s += normalizedProbList[i]
        if s >= r:
            return i
    return len(probList)-1


#graph transformation/clean up for subgraph counting aglo (e.g. ladder function) 
#this remap the node id, such that node id starts from 0 and increments to the total number of nodes 
def translate(datafile, newDatafile):
    nodeMap = dict()
    
    fin = open(datafile, "r")
    fout = open(newDatafile, "w")
    for ij in fin:
        i,j = ij.split()
        #i = int(i)
        #j = int(j)
        if i not in nodeMap:
            nodeMap[i] = len(nodeMap)
        if j not in nodeMap:
            nodeMap[j] = len(nodeMap)
        
        i_map = nodeMap[i]
        j_map = nodeMap[j]
        if i_map < j_map:
            fout.write(str(i_map)+" "+str(j_map)+"\n")
        else:
            fout.write(str(j_map)+" "+str(i_map)+"\n")

    fout.close()
    fin.close() 


#####utility functions for subgraph counting

class graphStat(object):
    #mainly store aggregated statistics of G
    
    def __init__(self, G):
        #take in networkx as an argument
    
        #degree number 
        self.nodesNum = len(G.nodes())

        #A_ij: the set of common neighbors of i and j 
        self.A = defaultdict(set)
        self.maxA = -1.0

        self.initSparseA(G)
         
    def initSparseA(self, G):
        start_time = time.time()
        for u,v in G.edges(): #edges in G only store one copy: either (u,v) or (v,u), not both
            for p in G[u]:
                if p != v:
                    self.A['{},{}'.format(min(p,v), max(p,v))].add(u)
            for p in G[v]:
                if p != u:
                    self.A['{},{}'.format(min(p,u),max(p,u))].add(v)
        #print("--- %s seconds ---" % (time.time() - start_time))
        
        for commonNeighbors in self.A.values():
            self.maxA = max(self.maxA, len(commonNeighbors))
        
        
    def getA(self,i,j):
        return self.A['{},{}'.format(i,j)]
    
    
    def geta(self,i,j):
        return len(self.getA(i,j))
       


def count_clique(G,nodesRange,k):
    if(len(nodesRange)<k):
        return 0
    elif k==1:
        return len(nodesRange)

    count = 0
    for i in nodesRange:
        count += count_clique(G, set(G[i].keys()).intersection(nodesRange),k-1)
    return count/k

def count(G, Gstat, queryType, k):
    #start_time = time.time()
    count = 0
    if queryType == "triangle":
        for u,v in G.edges():
            count = count + Gstat.geta(min(u,v),max(u,v))
        count = count/3 
    elif queryType == "kstar":
        for i in range(Gstat.nodesNum):
            d = G.degree[i]
            if d >= k:
                count = count + comb(d,k)
    elif queryType == "kclique":
        for u,v in G.edges():
            count += count_clique(G,Gstat.getA(min(u,v),max(u,v)), k-2)
        count /= comb(k,2)
    elif queryType == "ktriangle":
        for u,v in G.edges():
            count = count + comb(Gstat.geta(min(u,v),max(u,v)),k)    
    #print("--- %s seconds ---" % (time.time() - start_time))
    return count  

