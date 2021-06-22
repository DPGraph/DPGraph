import networkx as nx
import collections 
import numpy as np
from scipy.stats import cauchy
from sklearn.isotonic import IsotonicRegression  
from sklearn.linear_model import LinearRegression 
import matplotlib
import matplotlib.pyplot as plt
from scipy.special import comb
from collections import defaultdict
import time



# utility functions
def get_sorted_deg_seq(G): # return ascending degree sequence
    deg_seq = sorted([d for n, d in G.degree()], reverse=False) 
    return deg_seq

def get_deg_his(G, max_deg): # degree histogram from graph G, capped at max_deg
    deg_seq = get_sorted_deg_seq(G)
    degree_count = collections.Counter(deg_seq)
    deg_his = np.zeros(max_deg+1)
    for deg in degree_count:
        deg_his[deg] = degree_count[deg]    
    return deg_his

def deg_seq_to_deg_his(deg_seq, max_deg):
    #assume deg sequence could be non-integer and be bigger than maxDegree
    deg_his = np.zeros(max_deg + 1)
    for deg in deg_seq:
        deg = int(round(deg))
        if deg <= max_deg:
            deg_his[deg]= deg_his[deg]+1
    return deg_his

def his_to_pdf(his):
    area = sum(his)
    if area == 0:
        print("AREA 0!!!!")
        print(his)
    max_deg = len(his)
    pdf = np.zeros(max_deg)
    for i in range(max_deg):
        pdf[i] = his[i]/area
    return pdf
    
def pdf_to_cdf(pdf): # convert probability density function to cumulative distribution
    cdf = np.zeros(len(pdf))
    cdf[0] = pdf[0]
    for i in range(1,len(pdf)):
         cdf[i] = cdf[i-1] + pdf[i]            
    return cdf

def cdf_to_pdf(cdf): # convert cumulative distribution to probability density 
    pdf = np.zeros(len(cdf))
    pdf[0] = cdf[0]
    for i in range(1,len(pdf)):
         pdf[i] = cdf[i] - cdf[i-1]            
    return pdf
    

def dif_deg_his_L1(his1,his2): # compute L1 error between 2 histogram
    #assume the same length
    return sum(abs(his1 - his2))

def dif_deg_his_L2(his1,his2): # compute L2 error between 2 histogram
    return sum(np.square(his1-his2))



def plot_his(trueHis,noisyHis):
    plt.plot(trueHis,'-g', label='trueHis')
    plt.plot(noisyHis,'--r', label='noisyHis')
    plt.legend();
    plt.xscale('log')

    
def plot_cum(trueHis,noisyHis):
    plt.plot(pdfToCdf(trueHis), '3b', label='trueCum')
    plt.plot(pdfToCdf(noisyHis), '2y', label='noisyCum')
    plt.legend();
    plt.xscale('log')

#DP basic functions
def add_laplace(true_counts, sens, epsilon): # Add Laplace noise to true distribution, given sensitivity and epsilon
    scale = 1.0* sens/epsilon
    noisy = true_counts + np.random.laplace(0.0, scale, len(true_counts))
    return noisy

# Smooth out the Laplace noise added to cdf using isotonic regression
def post_process_cdf(noisy_cdf, total_count): 
    ir = IsotonicRegression(y_min=0, y_max=total_count, increasing=True)
    cdf= ir.fit_transform(X=range(len(noisy_cdf)),y=noisy_cdf)   
    return cdf

def post_process_pdf(noisy_pdf, nodes_num):
    cdf = pdf_to_cdf(noisy_pdf)
    cdf = post_process_cdf(cdf, nodes_num)
    pdf = cdf_to_pdf(cdf)
    return pdf


def extend_his(his,max_degree): # extend truncated histogram to have {max_degree+1} points
    #his has a shortern length 
    if (max_degree+1) > len(his):
        his_extended = np.zeros(max_degree + 1)
        his_extended[0:len(his)] = his
        return his_extended
    else:
        return his

    
def sample_prob_list(prob_list):
    normalized = prob_list/sum(prob_list)
    return np.random.choice(len(prob_list),1,p=normalized)[0]

    # normalized = prob_list/sum(prob_list)
    # r = np.random.uniform(0,1,1)
    # s = 0 
    # for i in range(len(prob_list)):
    #     s += normalized[i]
    #     if s >= r:
    #         return i
    # return len(prob_list)-1


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



