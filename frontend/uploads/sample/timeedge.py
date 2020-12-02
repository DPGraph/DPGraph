#/usr/bin/env python3
	
import sys
import csv



algo = sys.argv[1]
epsilon = sys.argv[2]
data = []
with open('FACEBOOKedgealgo.csv') as data_file:
    datas = csv.reader(data_file,delimiter=',')
    lingCount = 0
    for row in datas:
        if lingCount == 0:
            lingCount = 1
        else:
            if row[0] == algo and row[1] == epsilon:
                ret = []
                for i in range(2,len(row)):
                    ret.append(float(row[i]))
                data.append(ret)

probability = []
for i in range(1,11):
    sum = 0.0
    for j in data:
        sum = sum + j[i]
    temp = sum
    for k in data:
        if sum > 0.0:
            tt = k[i]
            k[i] =temp/sum
            temp = temp - tt

for j in data:
    print(algo,end = ",")
    print(epsilon,end = ",")
    for i in range(len(j)):
        if i < len(j)-1:
            print(j[i],end = ",")
        else:
            print(j[i])
    

