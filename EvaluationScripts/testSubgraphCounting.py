from util import *
from edgeDP_subgraphCounting import *
import os.path


#Caller 

dataDir ="Datasets/"
dataNames = ["HepPh","toydata", "facebook_combined", "wiki-Vote", 
             "email-Enron",  "cit-HepTh", "com-dblp.ungraph"]
dataKey = 2
dataName = dataNames[dataKey]

datafile = dataDir+dataName #"facebook_combined.txt"
if not os.path.isfile(datafile+"-map.txt"):
    translate(datafile+".txt", datafile+"-map.txt")
    #convert all nodes id to 0 to nodeNum
else:
    print("file exists")
    
datafile = datafile + "-map.txt"
print(datafile)

G=nx.read_edgelist(datafile, nodetype=int)
#G = nx.fast_gnp_random_graph(20,0.2)
G.remove_edges_from(nx.selfloop_edges(G))
print(len(G.edges))

nodesNum = len(G.nodes()) #assume this is given
maxDeg = nodesNum -1  #assume this is given

trueHis = getDegHis(G,maxDeg)
print(trueHis)

nodesList = list(G.nodes)
print(min(nodesList),max(nodesList),len(nodesList))

print(len(G.edges))

Gstat = graphStat(G)


epsilon = 0.05
queryType = "triangle"
k=-1
trueCount = count(G,Gstat,queryType,k)
noisyCount1 = edgeDP_LadderMechanism(G, Gstat, queryType, k, epsilon)
noisyCount2 = edgeDP_LaplaceMechanism(G, Gstat, queryType, k, epsilon)
noisyCount3 = edgeDP_SmoothSensitivityMechanism(G, Gstat, queryType, k, epsilon)
print(trueCount,noisyCount1, noisyCount2, noisyCount3)
