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

#j = 0;
#while j < len(trueHis):
#    rounds = 10
#    total = 0
#    for i in range(rounds):
#        if j+i < nodesNum : 
#            total += trueHis[j+i]
#        j+=1

 #   print(j-5, total)

for i in range(len(trueHis)):
    print(i, end = ",")
    print(trueHis[i])
