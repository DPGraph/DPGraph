#!/usr/bin/env python3

import sys
from util import *
from edgeDP_degDist import *
from nodeDP_degDist import * 


dataDir ="Datasets/"
dataNames = ["toydata.txt", "facebook_combined.txt", "wiki-Vote.txt", "email-Enron.txt",  "cit-HepTh.txt", "com-dblp.ungraph.txt"]
dataKey = int(sys.argv[1])
dataName = dataNames[dataKey]
print(dataName)

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
print(algo)

epsList = [0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0]
#epsList = [0.1, 0.5, 1.0, 1.5, 2.0]
#epsList = [0.1]
repeats = 30

maxTheta = min(nodesNum-1,200)
thetaCandidates = [20,40,60,80,100,120,140,160,180,200]

for epsilon in epsList:
    errors = []
    for i in range(repeats):
        noisyDegHis = np.zeros(maxDeg+1)
        if algo == "edgeDP_degHis_Lap":        
            noisyDegHis = edgeDP_degHis_Lap(G,maxDeg,epsilon)
        elif algo == "edgeDP_degSeq_Lap":
            noisyDegHis = edgeDP_degSeq_Lap(G,maxDeg,epsilon)
        elif algo == "nodeDP_degHis_Lap":
            noisyDegHis = nodeDP_degHis_Lap(G,maxDeg,epsilon)
        elif algo == "nodeDP_degSeq_Lap":
            noisyDegHis = nodeDP_degSeq_Lap(G,maxDeg,epsilon)
        elif algo == "nodeDP_nodeTrun_Smooth":
            noisyDegHis = nodeDP_nodeTrun_Smooth(G,maxDeg,epsilon,maxTheta)
        elif algo == "nodeDP_edgeAdd_degHisPart_Lap":
            rCandidates = [1.2,1.5,1.8] #r determines the partition (g_i = {k:r^{i-1}<= k < r^i})
            noisyDegHis = nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaCandidates, rCandidates) 
        elif algo == "nodeDP_edgeAdd_degCum_Lap":
            noisyDegHis = nodeDP_edgeAdd_degCum_Lap(G,maxDeg,epsilon,thetaCandidates)
        elif algo == "nodeDP_edgeAdd_degCum_Lap_variant":
            noisyDegHis = nodeDP_edgeAdd_degCum_Lap_variant(G,maxDeg,epsilon,thetaCandidates)
        elif algo == "nodeDP_flowgraph_degSeq_Lap":
            noisyDegHis = nodeDP_flowgraph_degSeq_Lap(G,maxDeg,epsilon, maxTheta) #works for small graph
        else:
            print("no valid algo")
        error = difDegHis_L1(trueHis/nodesNum, noisyDegHis/nodesNum)
        #print(i, error)
        errors.append(error)
        #plotHis(trueHis/nodesNum,noisyDegHis/nodesNum)
        #plotCum(trueHis/nodesNum,noisyDegHis/nodesNum)
                
    print(epsilon, np.mean(errors), np.std(errors))

