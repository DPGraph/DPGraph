#!/bin/bash
python3 edgealgo.py 0 2 > testing.csv
python3 edgealgo.py 0 2 >> FAEBOOKedgealgo.csv
python3 time.py 3 0.01 > tt.csv 
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv
python3 time.py 3 0.02 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 0.05 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 0.1 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 0.2 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 0.5 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 1.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 2.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 5.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 time.py 3 10.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfedgealgo.csv 
python3 evalDegDistedge.py 0 2 >>FACEBOOKedge.csv
rm tt.csv
rm testing.csv
