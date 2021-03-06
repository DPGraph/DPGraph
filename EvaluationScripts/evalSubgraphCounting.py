import sys
import os.path
from edgeDP_subgraphCounting import *
import os.path

#Caller 

dataDir ="Datasets/"
dataNames = ["HepPh", "facebook_combined", "wiki-Vote", 
             "email-Enron",  "cit-HepTh", "com-dblp.ungraph"]
#dataKey = 1
dataKey = int(sys.argv[1])
dataName = dataNames[dataKey]
print(dataName)

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
#print(len(G.edges))

nodesNum = len(G.nodes()) #assume this is given
maxDeg = nodesNum -1  #assume this is given

queryTypeList = ["triangle", "kstar", "kclique", "ktriangle"]
kList = [-1, 3, 4, 2]
queryKey = int(sys.argv[2]) 
#queryKey = 0
queryType = queryTypeList[queryKey]
k = kList[queryKey]

algoNames = ["edgeDP_ladder", 
             "edgeDP_laplace", 
             "edgeDP_smooth"]


#epsList = [0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0]
epsList = [0.1, 0.5, 1.0, 1.5, 2.0]
#epsList = [0.1]
repeats = 3 


#######code for utility evaluation########

Gstat = graphStat(G)
ladders = edgeDP_LadderFunction(G,Gstat,queryType,k)  
trueCount = count(G,Gstat,queryType,k)


for algoKey in range(len(algoNames)):
    algo = algoNames[algoKey]
    print(algo)

    for epsilon in epsList:
        errors = []
        for i in range(repeats):
            noisyCount = 0.0
            if algo == "edgeDP_ladder":
                noisyCount = edgeDP_LadderMechanismFast(G, Gstat, queryType, k, epsilon,ladders,trueCount)
            elif algo == "edgeDP_laplace":
                noisyCount = edgeDP_LaplaceMechanismFast(G, Gstat, queryType, k, epsilon,trueCount)
            elif algo == "edgeDP_smooth":
                noisyCount = edgeDP_SmoothSensitivityMechanismFast(G, Gstat, queryType, k, epsilon,ladders,trueCount)
            errors.append(abs(noisyCount-trueCount)/trueCount)
        print(np.mean(errors), np.std(errors))
    
    print("\n")


######code for time evaluation#######
"""
algoKey = int(sys.argv[3]) 
#algoKey = 1
algo = algoNames[algoKey]
print(algo)

#epsList = [0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0]
#epsList = [0.1, 0.5, 1.0, 1.5, 2.0]
epsList = [0.1]
repeats = 3 

start_time = time.time()
Gstat = graphStat(G)
trueCount = count(G,Gstat,queryType,k)

for epsilon in epsList:
    errors = []
    for i in range(repeats):
        noisyCount = 0.0
        if algo == "edgeDP_ladder":
            noisyCount = edgeDP_LadderMechanism(G, Gstat, queryType, k, epsilon)
        elif algo == "edgeDP_laplace":
            noisyCount = edgeDP_LaplaceMechanism(G, Gstat, queryType, k, epsilon)
        elif algo == "edgeDP_smooth":
            noisyCount = edgeDP_SmoothSensitivityMechanism(G, Gstat, queryType, k, epsilon)
        errors.append(abs(noisyCount-trueCount)/trueCount)
    print(np.mean(errors), np.std(errors))

print("--- %s seconds (average) ---" % ((time.time() - start_time)/repeats))
"""
