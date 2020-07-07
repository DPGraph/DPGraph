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

for i in range(maxDeg):
    print(i, trueHis[i])

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

basil = int(sys.argv[3])
for epsilon in epsList:
    errors = []
    time = []
    for i in range(repeats):
        noisyDegHis = np.zeros(maxDeg+1)
        if algo == "edgeDP_degHis_Lap":        
            start = timeit.default_timer();
            noisyDegHis = edgeDP_degHis_Lap(G,maxDeg,epsilon)
            end = timeit.default_timer();
        elif algo == "edgeDP_degSeq_Lap":
            start = timeit.default_timer();
            noisyDegHis = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
            end = timeit.default_timer();
        elif algo == "nodeDP_degHis_Lap":
            start = timeit.default_timer();
            noisyDegHis = nodeDP_degHis_Lap(G,maxDeg,epsilon)
            end = timeit.default_timer();
        elif algo == "nodeDP_degSeq_Lap":
            start = timeit.default_timer();
            noisyDegHis = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
            end = timeit.default_timer();

        elif algo == "nodeDP_nodeTrun_Smooth":
            start = timeit.default_timer();
            noisyDegHis = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
            end = timeit.default_timer();
        elif algo == "nodeDP_edgeAdd_degHisPart_Lap":
            start = timeit.default_timer();
            rCandidates = [1.2,1.5,1.8] #r determines the partition (g_i = {k:r^{i-1}<= k < r^i})

            noisyDegHis = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates) 
            end = timeit.default_timer();
        elif algo == "nodeDP_edgeAdd_degCum_Lap":
            start = timeit.default_timer();
            noisyDegHis = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
            end = timeit.default_timer();
        elif algo == "nodeDP_edgeAdd_degCum_Lap_variant":
            start = timeit.default_timer();
            noisyDegHis = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
            end = timeit.default_timer();
        elif algo == "nodeDP_flowgraph_degSeq_Lap":
            start = timeit.default_timer();
            noisyDegHis = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
            end = timeit.default_timer();
        else:
            print("no valid algo")
        error = difDegHis_L1(trueHis/nodesNum, noisyDegHis/nodesNum)
        #print(i, error)
        errors.append(error)
        time.append(end-start)
        #plotHis(trueHis/nodesNum,noisyDegHis/nodesNum)
        #plotCum(trueHis/nodesNum,noisyDegHis/nodesNum)
    
    #for j in range(nodesNum):
        
     #   print(algoKey-1,epsilon,basil,j,noisyDegHis[j])
    #print(algoKey+1,epsilon, np.mean(errors), np.std(errors),np.mean(time),np.std(time))

