#!/usr/bin/env python3

from util import *

##Edge-DP 
def edgeDP_computeGS(G, Gstat, queryType, k):
    nodesNum = Gstat.nodesNum
    if queryType == "triangle":
        return nodesNum-2
    elif queryType == "kstar":
        return 2 * comb(nodesNum-2, k-1)
    elif queryType == "kclique":
        return comb(nodesNum-2,k-2)
    elif queryType == "ktriangle":
        return comb(nodesNum-2,k) + 2*(nodesNum-2)*comb(nodesNum-3,k-1)
    else:
        print(queryType, "is unspecified")
        return -1.0


#refer to graph.cpp:  graph::ls for implementation details 
def edgeDP_computeLS(G, Gstat, queryType, k):
    ls = 0.0 
    if queryType == "triangle":
        ls = Gstat.maxA
        return ls
    elif queryType == "kstar":
        nodesNum = Gstat.nodesNum
        bucket = [-1] * nodesNum #bucket: the common neighbor sizes 
        for i in range(nodesNum):
            for j in range(i+1, nodesNum):
                xij = int(G.has_edge(i,j))
                di = max(G.degree[i],G.degree[j]) - xij
                dj = min(G.degree[i],G.degree[j]) - xij 
                bucket[di] = max(bucket[di],dj)
                
        uppers = []
        for i in reversed(range(nodesNum)):
            if bucket[i] <0:
                continue
            if (len(uppers)==0) or uppers[-1][1] < bucket[i]:
                uppers.append([i, bucket[i]])    
        #print("uppers(0-10):", uppers[0:10])        
        for p in uppers:
            ls = max(ls, comb(p[0],k-1)+comb(p[1],k-1))
        
        #print(ls)
        return ls
    
    elif queryType == "kclique":
        nodesNum = Gstat.nodesNum
        for i in range(nodesNum):
            for j in range(i+1, nodesNum):
                ls  = max(ls, count_clique(G,Gstat.getA(min(i,j),max(i,j)),k-2))
        #print(ls)
        return ls
    
    elif queryType == "ktriangle":
        nodesNum = Gstat.nodesNum
        for i in range(nodesNum):
            for j in range(i+1, nodesNum):
                Aij = Gstat.getA(min(i,j),max(i,j))
                xij = int(G.has_edge(i,j))
                
                lsij = comb(len(Aij),k)
                for l in Aij:
                    ail = Gstat.geta(min(i,l),max(i,l))
                    ajl = Gstat.geta(min(l,j),max(l,j))
                    lsij = lsij + comb(ail-xij, k-1) + comb(ajl-xij,k-1)
                ls = max(ls,lsij)
        #print(ls)
        return ls
    
    else:
        print(queryType, "is unspecified")
        return ls



def edgeDP_LadderFunction(G, Gstat, queryType, k):
    lsd = []    
    if queryType == "triangle":
        lsd = lsd_triangle(G,Gstat,queryType,k)
    elif queryType == "kstar":
        lsd = lsd_kstar(G,Gstat,queryType,k)
        return lsd
    elif queryType == "kclique":
        lsd = lsd_kclique(G,Gstat,queryType,k)
        return lsd
    elif queryType == "ktriangle":
        lsd = lsd_ktriangle(G,Gstat,queryType,k)
        return lsd
    else:
        print(queryType, "is unspecified")
    return lsd


def lsd_triangle(G,Gstat,queryType,k):
    start_time = time.time()
    nodesNum = Gstat.nodesNum
    bucket = [-1] * nodesNum #bucket: the common neighbor sizes 
    for i in range(nodesNum):
        for j in range(i+1, nodesNum):
            #aij: the number of common neighbors of i and j
            aij = Gstat.geta(i,j)
            #di = G.degree[i]
            #dj = G.degree[j]
            #xij = int(G.has_edge(i,j))
            #bij: the number of nodes connected to exactly one of i and j
            bij = G.degree[i] + G.degree[j] - 2*aij - 2*int(G.has_edge(i,j))
            bucket[aij] = max(bucket[aij], bij)  
            #if (i==0 and j <10):
            #    print(i,j,aij, bucket[aij], di,dj,xij)
            
    #print("bucket(0-10):", bucket[0:10])
    
    uppers = []
    for i in reversed(range(nodesNum)):
        if bucket[i] <0:
            continue
        if (len(uppers)==0) or (i*2+bucket[i] > uppers[-1][0]*2 + uppers[-1][1]):
            uppers.append([i, bucket[i]])
    #print("uppers(0-10):", uppers[0:10])
    
    gs = edgeDP_computeGS(G,Gstat,queryType,k)
    #print("gs: ", gs)
    
    LSD = []
    t = 0
    
    while 1:
        lsd = 0
        for p in uppers:
            lsd = max(lsd, p[0]+ (t+min(t,p[1])) /2)
        t +=1 
        if lsd < gs:
            LSD.append(lsd)
        else:
            LSD.append(gs)
            #print("LSD(0-10):", LSD[0:10])
            #print("--- %s seconds ---" % (time.time() - start_time))
            return LSD      
    
#refer to graph.cpp: lsd_kstar for implementation details 
def lsd_kstar(G,Gstat,queryType,k):
    start_time = time.time()
    nodesNum = Gstat.nodesNum
    bucket = [-1] * nodesNum #bucket: the common neighbor sizes 
    for i in range(nodesNum):
        for j in range(i+1, nodesNum):
            xij = int(G.has_edge(i,j))
            di = max(G.degree[i],G.degree[j]) - xij
            dj = min(G.degree[i],G.degree[j]) - xij 
            bucket[di] = max(bucket[di],dj)
            
    #print("bucket(0-10):", bucket[0:10])
    
    uppers = []
    for i in reversed(range(nodesNum)):
        if bucket[i] <0:
            continue
        if (len(uppers)==0) or uppers[-1][1] < bucket[i]:
            uppers.append([i, bucket[i]])   
    #print("uppers(0-10):", uppers[0:10])
    
    gs = edgeDP_computeGS(G,Gstat,queryType,k)
    #print("gs: ", gs)
    
    LSD = []
    
    while 1:
        lsd = 0
        for p in uppers:
            lsd = max(ls, comb(p[0],k-1)+comb(p[1],k-1))
            
            if p[0] < nodesNum-2:
                p[0] = p[0]+1
            elif p[1] < nodesNum-2:
                p[1] = p[1]+1
            
        if lsd < gs:
            LSD.append(lsd)
        else:
            LSD.append(gs)
            #print("LSD(0-10):", LSD[0:10])
            #print("--- %s seconds ---" % (time.time() - start_time))
            return LSD    
          

#refer to graph.cpp: ladder_kclique for implementation details 
def lsd_kclique(G,Gstat,queryType,k):
    start_time = time.time()
    gs = edgeDP_computeGS(G,Gstat,queryType,k)
    ls = edgeDP_computeLS(G,Gstat,queryType,k)
    #print("gs: ", gs, "; ls", ls)
    
    LSD = []
    lsd = ls 
    t = 0
    
    while 1:
        if lsd < gs:
            LSD.append(lsd)
        else:
            LSD.append(gs)
            #print("LSD(0-10):", LSD[0:10])
            #print("--- %s seconds ---" % (time.time() - start_time))
            return LSD   
        lsd = lsd + comb(Gstat.maxA+t, k-3)
        t +=1 
        


#refer to graph.cpp: ladder_ktriangle for implementation details 
def lsd_ktriangle(G,Gstat,queryType,k):
    start_time = time.time()
    gs = edgeDP_computeGS(G,Gstat,queryType,k)
    ls = edgeDP_computeLS(G,Gstat,queryType,k)
    #print("gs: ", gs, "; ls", ls)
    
    LSD = []
    lsd = ls 
    t = 0
    amax = Gstat.maxA
    
    while 1:
        if lsd < gs:
            LSD.append(lsd)
        else:
            LSD.append(gs)
            #print("LSD(0-10):", LSD[0:10])
            #print("--- %s seconds ---" % (time.time() - start_time))
            return LSD   
        
        lsd = lsd + 3* comb(amax+t, k-1) + (amax+t) * comb(amax+t,k-2)
        t +=1 
    
    return -1



#end-to-end: ladder function paper: algorithm 1 
def edgeDP_LadderMechanism(G, Gstat, queryType, k, epsilon):
    trueCount = count(G,Gstat,queryType,k)
    #print(queryType,k, "true count: ", trueCount)
    
    #ladders: ladder function evaluated on G
    ladders = edgeDP_LadderFunction(G,Gstat,queryType,k)  
    #M: length of the ladder function
    M = len(ladders)
    
    ranges = []
    weights = [1.0] #the center's weight
    
    #rungs 1 to M
    dst = 0.0 
    for t in range(M):
        weights.append(2*ladders[t]*np.exp(epsilon/2.0*(-t-1)))
        ranges.append(dst)
        dst = dst + ladders[t]
        
    #rung M+1
    weights.append(2*ladders[-1]* np.exp(epsilon/2.0*(-M-1))/(1-np.exp(-epsilon/2.0)))
        
    ####the only part that involves randomness, may store the earlier results for evaluation over multiple runs 

    noisyCount = 0

    t = int(sampleProbList(weights))

    if t==0:
        noisyCount = trueCount

    elif t<= M:
        flag = -1.0
        if (np.random.uniform()>0.5):
            flag = 1.0
        low = ranges[t-1]
        delta = np.ceil(np.random.uniform() * (ranges[t] - ranges[t-1]))
        noisyCount = flag * delta + trueCount

    else:
        p = 1.0 - np.exp(-epsilon/2.0)
        ext = np.random.geometric(p)
        low = dst + ext * ladders[-1]
        high = low + ladders[-1]
        flag = -1.0
        if (np.random.uniform()>0.5):
            flag = 1.0
        noisyCount = flag * np.random.randint(low, high+1) + trueCount
    
    return noisyCount
        
#Laplace mechanism
def edgeDP_LaplaceMechanism(G, Gstat, queryType, k, epsilon):

    trueCount = count(G,Gstat,queryType,k)
    #print(queryType,k, "true count: ", trueCount)
        
    gs = edgeDP_computeGS(G, Gstat, queryType, k)
    
    scale =1.0* gs/epsilon
    noisyCount = trueCount + np.random.laplace(0.0, scale, 1)
    
    return noisyCount

 
#Smooth sensitivity mechanism
def edgeDP_SmoothSensitivityFunction(lsd, beta):
    ss = 0.0
    for i in range(len(lsd)):
        ss = max(ss, lsd[i]* np.exp(beta* (-1.0)* i))
    return ss 
 

def edgeDP_SmoothSensitivityMechanism(G, Gstat, queryType, k, epsilon):
    trueCount = count(G,Gstat,queryType,k)
    #print(queryType,k, "true count: ", trueCount)
    
    #ladders: ladder function evaluated on G or LSD
    ladders = edgeDP_LadderFunction(G,Gstat,queryType,k)  
    #M: length of the ladder function
    M = len(ladders)
    
    ss = edgeDP_SmoothSensitivityFunction(ladders, epsilon/6.0)
    
    noisyCount = trueCount + 6.0/epsilon * ss * np.random.standard_cauchy(1)  
    return noisyCount
            


###########faster version without recomputing ladders function
#Fast version: no repeat on ladders, true count
def edgeDP_LadderMechanismFast(G, Gstat, queryType, k, epsilon, ladders, trueCount):
    #trueCount = count(G,Gstat,queryType,k)
    #print(queryType,k, "true count: ", trueCount)
    
    #ladders: ladder function evaluated on G
    #ladders = edgeDP_LadderFunction(G,Gstat,queryType,k)  
    #M: length of the ladder function
    M = len(ladders)
    
    ranges = []
    weights = [1.0] #the center's weight
    
    #rungs 1 to M
    dst = 0.0 
    for t in range(M):
        weights.append(2*ladders[t]*np.exp(epsilon/2.0*(-t-1)))
        ranges.append(dst)
        dst = dst + ladders[t]
        
    #rung M+1
    weights.append(2*ladders[-1]* np.exp(epsilon/2.0*(-M-1))/(1-np.exp(-epsilon/2.0)))
        
    noisyCount = 0

    t = int(sampleProbList(weights))

    if t==0:
        noisyCount = trueCount

    elif t<= M:
        flag = -1.0
        if (np.random.uniform()>0.5):
            flag = 1.0
        low = ranges[t-1]
        delta = np.ceil(np.random.uniform() * (ranges[t] - ranges[t-1]))
        noisyCount = flag * delta + trueCount

    else:
        p = 1.0 - np.exp(-epsilon/2.0)
        ext = np.random.geometric(p)
        low = dst + ext * ladders[-1]
        high = low + ladders[-1]
        flag = -1.0
        if (np.random.uniform()>0.5):
            flag = 1.0
        noisyCount = flag * np.random.randint(low, high+1) + trueCount
    
    return noisyCount

#Fast version: no repeat on true count
def edgeDP_LaplaceMechanismFast(G, Gstat, queryType, k, epsilon, trueCount):

    #trueCount = count(G,Gstat,queryType,k)
    #print(queryType,k, "true count: ", trueCount)
        
    gs = edgeDP_computeGS(G, Gstat, queryType, k)
    
    scale =1.0* gs/epsilon
    noisyCount = trueCount + np.random.laplace(0.0, scale, 1)
    
    return noisyCount
    
#Fast version: no repeat on ladders, true count
def edgeDP_SmoothSensitivityMechanismFast(G, Gstat, queryType, k, epsilon,ladders,trueCount):
    #trueCount = count(G,Gstat,queryType,k)
    #print(queryType,k, "true count: ", trueCount)
    
    #ladders: ladder function evaluated on G or LSD
    #ladders = edgeDP_LadderFunction(G,Gstat,queryType,k)  
    #M: length of the ladder function
    M = len(ladders)
    
    ss = edgeDP_SmoothSensitivityFunction(ladders, epsilon/6.0)
    
    noisyCount = trueCount + 6.0/epsilon * ss * np.random.standard_cauchy(1)  
    return noisyCount
            
     
    
