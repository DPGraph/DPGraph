#!/usr/bin/env python3

import sys
import timeit
from util import *
from edgeDP_degDist import *
from nodeDP_degDist import * 


dataDir ="Datasets/"
dataNames = ["facebook_combined.txt", "cit-HepTh.txt", "com-dblp.ungraph.txt", "toydata.txt", "wiki-Vote.txt", "email-Enron.txt"]
dataKey = int(sys.argv[1])
dataName = dataNames[dataKey]
#print(dataName)

datafile = dataDir+dataName #"facebook_combined.txt"
G=nx.read_edgelist(datafile, nodetype=int)
#G = nx.fast_gnp_random_graph(20,0.2)

nodesNum = len(G.nodes()) #assume this is given 
maxDeg = nodesNum -1  #assume this is given 

trueHis = getDegHis(G,maxDeg)



###Evaluation of algorithms for degree distribution


algoNames = ["edgeDP_degHis_Lap", 
             "edgeDP_degSeq_Lap", 
             "nodeDP_degHis_Lap", 
             "nodeDP_degSeq_Lap", 
             "nodeDP_nodeTrun_Smooth", 
             "nodeDP_edgeAdd_degHisPart_Lap", 
             "nodeDP_edgeAdd_degCum_Lap",
             "nodeDP_edgeAdd_degCum_Lap_variant",
             "nodeDP_flowgraph_degSeq_Lap"]

algoKey = int(sys.argv[2]) 
algo = algoNames[algoKey]
#print(algo)

epsList = [0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0]
#epsList = [0.1, 0.5, 1.0, 1.5, 2.0]
#epsList = [0.1]
repeats = 3 

maxTheta = min(nodesNum-1,200)
thetaCandidates = [20,40,60,80,100,120,140,160,180,200]
if maxTheta < 200:
    thetaCandidates = [i+1 for i in range(maxTheta)]

for epsilon in epsList:
    #errors = []
    time = []
    noisyDegHis1 = np.zeros(maxDeg+1)
    noisyDegHis2 = np.zeros(maxDeg+1)
    noisyDegHis3 = np.zeros(maxDeg+1)
    noisyDegHis4 = np.zeros(maxDeg+1)
    noisyDegHis5 = np.zeros(maxDeg+1)
    noisyDegHis6 = np.zeros(maxDeg+1)
    noisyDegHis7 = np.zeros(maxDeg+1)
    noisyDegHis8 = np.zeros(maxDeg+1)
    noisyDegHis9 = np.zeros(maxDeg+1)
    noisyDegHis10 = np.zeros(maxDeg+1)
    if algo == "edgeDP_degHis_Lap":        
        start = timeit.default_timer();
        noisyDegHis1 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis2 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis3 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis4 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis5 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis6 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis7 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis8 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis9 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis10 = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        end = timeit.default_timer();
    elif algo == "edgeDP_degSeq_Lap":
        start = timeit.default_timer();
        noisyDegHis1 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis2= edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis3 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis4 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis5 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis6 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis7 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis8 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis9 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis10 = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        end = timeit.default_timer();
    elif algo == "nodeDP_degHis_Lap":
        start = timeit.default_timer();
        noisyDegHis1 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis2 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis3 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis4 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis5 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis6 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis7 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis8 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis9 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        noisyDegHis10 = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        end = timeit.default_timer();
    elif algo == "nodeDP_degSeq_Lap":
        start = timeit.default_timer();
        noisyDegHis1 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis2 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis3 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis4 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis5 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis6 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis7 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis8 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis9 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        noisyDegHis10 = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        end = timeit.default_timer();
    elif algo == "nodeDP_nodeTrun_Smooth":
        start = timeit.default_timer();
        noisyDegHis1 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis2 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis3 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis4 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis5 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis6 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis7 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis8 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis9 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        noisyDegHis10 = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        end = timeit.default_timer();
    elif algo == "nodeDP_edgeAdd_degHisPart_Lap":
        start = timeit.default_timer();
        rCandidates = [1.2,1.5,1.8] #r determines the partition (g_i = {k:r^{i-1}<= k < r^i})
        noisyDegHis1 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis2 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis3 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis4 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates) 
        noisyDegHis5 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis6 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis7 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis8 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis9 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        noisyDegHis10 = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates)
        end = timeit.default_timer();
    elif algo == "nodeDP_edgeAdd_degCum_Lap":
        start = timeit.default_timer();
        noisyDegHis1 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis2 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis3 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis4 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis5 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis6 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis7 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis8 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis9 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis10 = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        end = timeit.default_timer();
    elif algo == "nodeDP_edgeAdd_degCum_Lap_variant":
        start = timeit.default_timer();
        noisyDegHis1 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis2 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis3 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis4 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis5 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis6 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis7 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis8 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis9 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        noisyDegHis10 = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        end = timeit.default_timer();
    elif algo == "nodeDP_flowgraph_degSeq_Lap":
        start = timeit.default_timer();
        noisyDegHis1 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis2 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis3 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis4 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis5 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis6 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis7 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis8 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis9 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        noisyDegHis10 = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        end = timeit.default_timer();
    else:
            print("no valid algo")
    #error = difDegHis_L1(trueHis/nodesNum, noisyDegHis/nodesNum)
        #print(i, error)
    #errors.append(error)
    time.append(end-start)
        #plotHis(trueHis/nodesNum,noisyDegHis/nodesNum)
        #plotCum(trueHis/nodesNum,noisyDegHis/nodesNum)
    
    for j in range(nodesNum):
        print(algoKey+1,epsilon,j,noisyDegHis1[j],noisyDegHis2[j],noisyDegHis3[j],noisyDegHis4[j],noisyDegHis5[j],noisyDegHis6[j],noisyDegHis7[j],noisyDegHis8[j],noisyDegHis9[j],noisyDegHis10[j])
    #print(algoKey-1,epsilon, np.mean(errors), np.std(errors),np.mean(time),np.std(time))

