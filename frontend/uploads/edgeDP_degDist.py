#!/usr/bin/env python3

from util import *

#Edge DP algorithms for degree distribution

#Hay et al. ICDM'09 (baseline)
def edgeDP_degHis_Lap(G, maxDeg, epsilon):
    degHis = getDegHis(G, maxDeg)
    sens = 4.0
    noisyDegHis = lap(degHis, sens, epsilon)
    noisyDegHis = postprocessPdf(noisyDegHis, len(G.nodes()))
    return noisyDegHis


#Hay et al. ICDM'09, Proserpio et al. WOSN'12 (wPINQ)
def edgeDP_degSeq_Lap(G, maxDeg, epsilon):
    degSeq = np.array(getSortedDegSeq(G))
    sens = 2.0
    #print(degSeq)
    noisyDegSeq = lap(degSeq, sens,epsilon)
    noisyDegSeq = postprocessCdf(noisyDegSeq, maxDeg)
    #print(noisyDegSeq)
    noisyDegHis = degSeqToDegHis(noisyDegSeq, maxDeg)
    return noisyDegHis

