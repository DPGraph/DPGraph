#!/bin/bash

python3 edgealgo.py 0 2 >> FACEBOOKedgealgo.csv
python3 timeedge.py 3 0.01 >> FACEBOOKcdfedgealgo.csv
python3 timeedge.py 3 0.02 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 0.05 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 0.1 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 0.2 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 0.5 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 1.0 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 2.0 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 5.0 >> FACEBOOKcdfedgealgo.csv 
python3 timeedge.py 3 10.0 >> FACEBOOKcdfedgealgo.csv 
python3 evalDegDistedge.py 0 2 >>FACEBOOKedge.csv
python3 edgealgo_density.py > new.csv 
mv new.csv FACEBOOKedgealgo.csv
