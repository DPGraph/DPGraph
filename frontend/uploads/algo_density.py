#!/usr/bin/env3 python3

algolist = [1,2,3,4,5,6,7]
eplist = [0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0]
data = {}
for algo in algolist:
    data[algo] = {}
    for ep in eplist:
        data[algo][ep] = {}
        

total = 0.0
title = ""
with open('FACEBOOKalgo.csv') as data_file:
    count = 0
    for line in data_file:
        if count == 0:
            title = line
            count = 1
        else:
            temp = line.split(",")
            data[int(temp[0])][float(temp[1])][int(temp[2])] = temp[3:]

print(title,end = "")
for algo in algolist:
    for ep in eplist:
        total1 = 0.0
        total2 = 0.0
        total3 = 0.0
        total4 = 0.0
        total5 = 0.0
        total6 = 0.0
        total7 = 0.0
        total8 = 0.0
        total9 = 0.0
        total10 = 0.0
        for key,value in data[algo][ep].items():
            total1 = total1 + float(value[0])
            total2 = total2 + float(value[1])
            total3 = total3 + float(value[2])
            total4 = total4 + float(value[3])
            total5 = total5 + float(value[4])
            total6 = total6 + float(value[5])
            total7 = total7 + float(value[6])
            total8 = total8 + float(value[7])
            total9 = total9 + float(value[8])
            total10 = total10 + float(value[9])
        for key,value in data[algo][ep].items():
            print(algo,end = ",")
            print(ep,end = ",")
            print(key,end = ",")
            if total1 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[0])/total1,end =",")
            if total2 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[1])/total2,end = ",")
            if total3 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[2])/total3,end =",")
            if total4 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[3])/total4,end = ",")
            if total5 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[4])/total5,end =",")
            if total6 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[5])/total6,end = ",")
            if total7 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[6])/total7,end =",")
            if total8 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[7])/total8,end = ",")
            if total9 == 0.0:
                print(0.0,end = ",")
            else:
                print(float(value[8])/total9,end =",")
            if total10 == 0.0:
                print(0.0)
            else:
                print(float(value[9])/total10)
            
    
