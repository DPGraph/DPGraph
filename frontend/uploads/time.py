#/usr/bin/env python3
	
import sys
import csv



algo = sys.argv[1]
epsilon = sys.argv[2]
print(algo)
print(epsilon)
with open('testing.csv') as data_file:
    data = csv.reader(data_file,delimiter=',')
    lingCount = 0
    for row in data:
        if lingCount == 0:
            lingCount = 1
        else:
            if row[0] == algo and row[1] == epsilon:
                ret = ""
                for i in range(len(row)):
                    if i < len(row)-1:
                        ret = ret + row[i]+","
                    else:
                        ret = ret + row[i]
                print(ret)
