#!/bin/bash

python3 algo.py 0 8 > testing.csv
python3 algo.py 0 8 >> FACEBOOKalgo.csv
python3 time.py 7 0.01 > tt.csv 
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv
python3 time.py 7 0.02 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.05 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.1 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.2 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.5 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 1.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 2.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 5.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 time.py 7 10.0 > tt.csv
./noisy_cdf < tt.csv >> FACEBOOKcdfalgo.csv 
python3 evalDegDist.py 0 8 >>FACEBOOK.csv
rm tt.csv
rm testing.csv
