#!/usr/bin/env python3

from util import *
from numpy import array, dot

#Node DP algorithms for degree distribution
################


#Day et al. SIGMOD'16 
#Algo 1 (projection by edge-addition, variant: output degSeq instead of graph), part of Algo 4
def edgeAddition_DegList(G, theta):    
    #Edge addition algorithm from empty graph till no edges can be added keep degree bounded by theta
    nodesNum = len(G.nodes())
    nodesList = list(G.nodes()) #the node ids are not strictly from 0 to |nodesNum|-1
    invNodesList = {}
    for id in range(nodesNum):
        v = nodesList[id]
        invNodesList[v]=id
    
    nodesIndices = np.random.permutation(nodesNum)
    degListGt = np.zeros(nodesNum)
    
    for vid in nodesIndices:
        v = nodesList[vid]
        for u in G.neighbors(v):
            uid = invNodesList[u]
            if uid<vid and degListGt[uid]<theta and degListGt[vid]<theta:
                degListGt[uid] = degListGt[uid]+1
                degListGt[vid] = degListGt[vid]+1
                
    degListGt=sorted(degListGt, reverse=False) #small to large degrees
    #print(degListGt)
    
    #degSeq = getSortedDegSeq(G)
    #diff = np.array(degSeq) - np.array(degListGt)
    #print("difference in deg seq after edge addition", sum(diff))
    
    return degListGt


#Day et al. SIGMOD'16 
#Part of Algo 4 (select an optimal theta) 
def learnTheta(G, maxDeg, epsilon_theta, epsilon_deg, thetaList):
    probList = []
    maxTheta = max(thetaList)
    sensitivity = 6.0 * maxTheta+4
    
    for theta in thetaList:
        degListGt = edgeAddition_DegList(G,theta)
        nodeNumTheta = len([deg for deg in degListGt if deg >theta])
        score = -2.0 * nodeNumTheta - np.sqrt(theta) * (theta+1)/epsilon_deg
        prob = np.exp(epsilon_theta * score /(2.0 * sensitivity))
        probList.append(prob)
        
    theta = thetaList[sampleProbList(probList)]
    return theta

#Day et al. SIGMOD'16 
#Part of Algo 2 (select an optimal theta and partition) 
def learnThetaPartition(G, maxDeg, epsilon_theta, epsilon_deg, thetaList, partitionList):
    probList = []
    maxTheta = max(thetaList)
    sensitivity = 6.0 * maxTheta+4
    
    his = getDegHis(G,maxDeg)
    for theta in thetaList:
        degListGt = edgeAddition_DegList(G,theta)
        nodeNumTheta = len([deg for deg in degListGt if deg >theta])
        lproj = 2.0 * nodeNumTheta
        for partition in partitionList:            
            lhist = 0 
            for i in range(len(partition)-1):
                start = partition[i]
                end = partition[i+1]
                ave = sum(his[start:end])/(end-start)
                diff = sum(abs(his[start:end] - ave))
                lhist = lhist + diff + (2.0*theta+1)/epsilon_deg
        score = -1.0 * (lhist + lproj)
        prob = np.exp(epsilon_theta * score /(2.0 * sensitivity))
        probList.append(prob)
        
    sampleIndex = sampleProbList(probList)
    thetaIndex = int(sampleIndex / len(partitionList))
    partitionIndex = sampleIndex % len(partitionList)
    theta= thetaList[thetaIndex]
    partition = partitionList[partitionIndex]
    return theta,partition


#Day et al. SIGMOD'16 
#Algo 3(extract histogram from cumulative histogram), part of Algo 4
def extractHist(cumHist): #cumHist is noisy cumulative histogram
    theta = len(cumHist)-1
    hist = np.zeros(len(cumHist))
    hc=list(cumHist)
    hc.append(cumHist[theta])
    hc[0] = 0
    i = 1
    if hc[1] <0:
        hc[1] = 0
    
    while i <= theta:
        if hc[i] <= hc[i+1]:
            hist[i] = max(hc[i] - hc[i-1],0)
            #print('a:', i, hist[i])
            i = i+1
        else:
            iold = i
            jlist = list(reversed(range(i,theta+2)))
            #print(jlist)
            for j in jlist:
                if hc[j-1] < hc[i]:
                    j = min(j,theta)
                    for k in range(i,j+1):
                        hist[k] = max(0,(hc[j]-hc[i-1])/(j-i+1))
                        #print('b:', k, hist[k])
                    i= j+1
                    break 
            if i == iold:
                #print("i does not change", i, cumHist[i:theta])
                break
    #print(pdfToCdf(hist))
    return hist
      

#Day et al. SIGMOD'16 
#Algo 5 (postprocess for tail destribution), part of Algo 4
#The last bin has a high count which contains the number of nodes with degree "at least" theta in G. 
def postTail(hist, theta):
    budget = hist[theta]
    #print("budget", budget)    
    start = int(round(theta/2))
    cbar = 2.0/theta * sum(hist[start:theta])
    
    X = np.array([[x] for x in range(start,theta)])
    #print(X)
    y = hist[start:theta]
    #print(y)
    reg = LinearRegression().fit(X,y)
    m = reg.coef_
    b = reg.intercept_ 
    #print(m,b)
    
    for k in range(theta, len(hist)):
        if m<0:
            #hist[k] = b + m * k #This step has an issue when theta is small, then b is small, and counts become negative
            hist[k] = max(b + m * k,0) 
        else:
            hist[k] = cbar
        budget = budget - hist[k]
        if budget <0:
            break
    return hist 


#Raskhodnikova & Smith, Arxiv'15
def flowgraph(G, theta):
    #https://pypi.org/project/qpsolvers/
    #Raskhodnikova & Smith, Arxiv'15
    #Note: this algo is slow, take more than 1 min for nodeNum=200

    nodesNum = len(G.nodes()) 
    edgesNum = len(G.edges())
    #print(nodesNum,edgesNum)

    nn = nodesNum * 2
    ne = edgesNum * 2
    n = nn + ne

    #P = np.zeros([n,n])
    #P[:(nn),:(nn)] = np.identity(nn)
    P = np.identity(n)
    
    q = np.zeros(n)
    q[:(nn)] = -2.0* theta

    T = np.identity(n)
    h = np.zeros(n)+1
    h[:nn] = theta 

    #print(T,h)

    A = np.zeros([nn,n])
    edgeCount = nn
    for i in range(nodesNum):
        A[i,i] = 1 
        A[nodesNum+i,nodesNum+i] = 1
        neighborSize = len([k for k in G.neighbors(i)])
        for j in range(neighborSize):
            A[i,(edgeCount+j)] = -1
            A[nodesNum+i,(edgeCount+j)] = -1
        edgeCount = edgeCount + neighborSize
    #print(A)
    
    b = np.repeat(0,nn)
    lb = np.repeat(0,n)
    x = solve_qp(P, q, T, h, A,b,lb)
    #print("\nThe optimal value is", prob.value)
    #print("A solution x is")

    degList = []
    #print(x.value[0])
    #print(nodesNum)
    for i in range(nodesNum):
        degList.append(int(x[i].round()))
    degSeq = sorted(degList,reverse=False)
    #print(degSeq)
    return degSeq

#Raskhodnikova & Smith, Arxiv'15
def flowgraphApprox(G,theta):
    #TODO: more efficient approximation algorithmm, but sensitivity will increase
    degSeq = []
    return degSeq

################
#Naive laplace mechanism with postprocessing
def nodeDP_degHis_Lap(G, maxDeg, epsilon):
    degHis = getDegHis(G,maxDeg)
    sens = 2.0 * (maxDeg + 1)
    noisyDegHis = lap(degHis, sens, epsilon)
    noisyDegHis = postprocessPdf(noisyDegHis, len(G.nodes()))
    return noisyDegHis

#Adapting Hay et al. ICDM'09, Proserpio et al. WOSN'12 (wPINQ)
def nodeDP_degSeq_Lap(G, maxDeg, epsilon):
    degSeq = np.array(getSortedDegSeq(G))
    sens = 1.0* (maxDeg + 1)
    #print(degSeq)
    noisyDegSeq = lap(degSeq, sens,epsilon)
    noisyDegSeq = postprocessCdf(noisyDegSeq, len(G.nodes()))
    #print(noisyDegSeq)
    noisyDegHis = degSeqToDegHis(noisyDegSeq, maxDeg)
    #print(noisyDegHis)
    return noisyDegHis

#Shiva et al. TCC'13
def nodeDP_nodeTrun_Smooth(G, maxDeg, epsilon, theta):
    epsilon_deg = epsilon 
    
    #node truncation: remove nodes with degree > theta 
    Gt = G.copy()
    nodesTrun = [n for n,d in Gt.degree() if d > theta]
    Gt.remove_nodes_from(nodesTrun)

    #smooth bound: (Prop 6.1, Algo 3)
    nodesNum = len(G.nodes())
    beta = epsilon/(np.sqrt(2.0)*(theta+1))   ## epsilon * np.log(nodesNum/theta)
    r = np.log(1.0*nodesNum/beta)
    l = len([n for n,d in Gt.degree() if (d >= theta-r and d<=theta+r)])
    smoothSens = l+1.0/beta + 1
    #print(beta, r, l,smoothSens)
    
    #add cauchy noise with epsilon_deg
    scale = 2*np.sqrt(2.0)*theta/epsilon_deg*smoothSens
    trueHisGt = getDegHis(Gt, theta)
    noisyHisGt = trueHisGt + cauchy.rvs(0,scale=smoothSens,size=len(trueHisGt))
    noisyHisG = extendHis(noisyHisGt, maxDeg)
    
    #postprocess (TCC DOES NOT HAVE THIS STEP)
    noisyHisG = postprocessPdf(noisyHisG, len(G.nodes()))
    
    return noisyHisG


#Raskhodnikova & Smith, Arxiv'15
def nodeDP_flowgraph_degSeq_Lap(G, maxDeg, epsilon, theta):
    epsilon_deg = epsilon 
    
    #TODO: add generalized exponential mechanism for selecting threshold theta
    
    
    #Flowgraph algorithm to obtain a degree sequence with max degree is bounded by theta
    degSeq = flowgraph(G,theta) #getSortedDegSeq(G) #TODO: replace this line with flowgraph algorithm 
    
    #Convert degSeq to degHis and add noise (this step can be improved by learn noisy seq first)
    sens = 6.0 *theta  #Algo 1: this requires an exact solver for the flowgraph; if an approximation algorithm is used, then the sensitivity needs go up.
    degHis = degSeqToDegHis(degSeq, theta)
    noisyDegHis = lap(degHis, sens, epsilon_deg)
    
    noisyHisG = extendHis(noisyDegHis, maxDeg)
    
    #postprocess (THE PAPER DOES NOT HAVE THIS STEP)
    noisyHisG = postprocessPdf(noisyHisG, len(G.nodes()))
    
    return noisyHisG


#Day et al. SIGMOD'16
def nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaList, paritionList):
    ##TODO: incomplete (exponential mechanism to get a partition first, and then apply Lap)
    return 0


#Day et al. SIGMOD'16
#variant of Algo 4 (\theta-constrained)
def nodeDP_edgeAdd_degCum_Lap_variant(G, maxDeg, epsilon, thetaList):
    theta = thetaList[0]
    epsilon_deg = epsilon
    
    #Learning theta 
    if len(thetaList) >1: #many choices 
        epsilon_theta = epsilon * 0.1
        epsilon_deg = epsilon-epsilon_theta
        theta = learnTheta(G, maxDeg, epsilon_theta, epsilon_deg, thetaList)
        #print("sampled theta", theta)

    #Edge addition algorithm from empty graph till no edges can be added keep degree bounded by theta
    degListGt = edgeAddition_DegList(G,theta)
    #print(degListGt)
    
    #cumulative historm + lap noise
    degHis = degSeqToDegHis(degListGt, theta)
    degCum = pdfToCdf(degHis)
    #print(degCum[0:30]) 
    sens = theta + 1 
    noisyDegCum = lap(degCum, sens, epsilon_deg)
    
    #print("noisyDegCum", noisyDegCum[0:30])
    noisyDegCum = postprocessCdf(noisyDegCum, len(G.nodes())) #Not Algo 3
    #print("noisyDegCum - monotonicity", noisyDegCum[0:30])
    noisyDegHis = cdfToPdf(noisyDegCum)
    noisyDegHis = extendHis(noisyDegHis,maxDeg)
    #print("noisyDegHis - extend lengh", noisyDegHis)
    noisyDegHis = postTail(noisyDegHis, theta)
    #print("noisyDegHis - post tail", noisyDegHis)
    
    return noisyDegHis
        

#Day et al. SIGMOD'16
#Algo 4 (\theta-cumulative)
def nodeDP_edgeAdd_degCum_Lap(G, maxDeg, epsilon, thetaList):
    theta = thetaList[0]
    epsilon_deg = epsilon
    
    #Learning theta 
    if len(thetaList) >1: #many choices 
        epsilon_theta = epsilon * 0.1
        epsilon_deg = epsilon-epsilon_theta
        theta = learnTheta(G, maxDeg, epsilon_theta, epsilon_deg, thetaList)
        #print("sampled theta", theta)

    #Edge addition algorithm from empty graph till no edges can be added keep degree bounded by theta
    degListGt = edgeAddition_DegList(G,theta)
    #print(degListGt)
    
    #cumulative historm + lap noise
    degHis = degSeqToDegHis(degListGt, theta)
    degCum = pdfToCdf(degHis)
    #print(degCum[0:30]) 
    sens = theta + 1 
    noisyDegCum = lap(degCum, sens, epsilon_deg)
    
    #print("noisyDegCum", noisyDegCum[0:30])
    noisyDegHis = extractHist(noisyDegCum) #Algo 3
    #print("noisyDegCum - monotonicity", noisyDegCum[0:30])
    
    noisyDegHis = extendHis(noisyDegHis,maxDeg)
    #print("noisyCumDegHis - extend lengh", noisyDegHis[0:30])
    noisyDegHis = postTail(noisyDegHis, theta)
    #print("noisyDegHis - post tail", noisyDegHis[0:30])
    
    return noisyDegHis


#Day et al. SIGMOD'16
#Algo 2 (\theta,\Omega-cumulative)
def nodeDP_edgeAdd_degHisPart_Lap(G, maxDeg, epsilon, thetaList, rList):
    theta = thetaList[0]
    epsilon_deg = epsilon

    #Create a set of partitions based on rList
    partitionList = []
    for r in rList:
        partition = [0]
        i = 0 
        k = int(round(np.power(r, i)))
        while k < maxDeg:
            if k > partition[len(partition)-1]:
                partition.append(k)
            i = i+1
            k = int(round(np.power(r, i)))
        partition.append(maxDeg) #we also add the maxDeg for the easy aggregation
        partitionList.append(partition)
    
    partition = partitionList[0]
    #Learning theta and partition
    if len(thetaList) >1 or len(partitionList)>1: #many choices 
        epsilon_theta = epsilon * 0.1
        epsilon_deg = epsilon-epsilon_theta
        (theta, partition) = learnThetaPartition(G, maxDeg, epsilon_theta, epsilon_deg, thetaList, partitionList)
        #print("sampled theta", theta, "sampled partition", partition)

    #Edge addition algorithm from empty graph till no edges can be added keep degree bounded by theta
    degListGt = edgeAddition_DegList(G,theta)
    #print(degListGt)
    
    # historm + lap noise
    degHis = degSeqToDegHis(degListGt, theta)
    noisyDegHis = np.zeros(len(degHis))
    sens = 2 * theta + 1
    for i in range(len(partition)-1):
        start = partition[i]
        end = partition[i+1]
        if end >= (theta+1):
            end = min(end,theta+1)
        noisyAve = (sum(degHis[start:end]) + lap([0],sens,epsilon_deg)[0])/(end-start)
        for j in range(start,end):
            noisyDegHis[j] = noisyAve
        if end >= (theta+1):
            break 
                
    noisyDegHis = extendHis(noisyDegHis,maxDeg)
    #print("noisyCumDegHis - extend lengh", noisyDegHis[90:110])
    noisyDegHis = postTail(noisyDegHis, theta)
    #print("noisyDegHis - post tail", noisyDegHis[90:110])
    
    return noisyDegHis
