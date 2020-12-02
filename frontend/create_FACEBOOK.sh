#!/bin/bash

python3 algo.py 0 8 >>FACEBOOKalgo.csv
python3 time.py 7 0.01 >> FACEBOOKcdfalgo.csv
python3 time.py 7 0.02 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.05 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.1 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.2 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 0.5 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 1.0 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 2.0 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 5.0 >> FACEBOOKcdfalgo.csv 
python3 time.py 7 10.0 >> FACEBOOKcdfalgo.csv 
python3 evalDegDist.py 0 8 >>FACEBOOK.csv
