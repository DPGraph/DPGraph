#!/bin/bash

python algo.py 3 8 > testing.csv
./clear < testing.csv >> TOYDATAalgo.csv
./modify_noisy 7 0.01 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 0.02 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 0.05 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 0.1 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 0.2 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 0.5 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 1.0 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 2.0 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 5.0 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
./modify_noisy 7 10.0 < TOYDATAalgo.csv | ./noisycdf >> TOYDATAcdfalgo.csv
python evalDegDist.py 3 8 > testing.csv
./clear < testing.csv >> TOYDATA.csv
rm testing.csv
