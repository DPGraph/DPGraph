#!/bin/bash

python algo.py 1 8 > testing.csv
./clear < testing.csv >> CITalgo.csv
./modify_noisy 7 0.01 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 0.02 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 0.05 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 0.1 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 0.2 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 0.5 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 1.0 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 2.0 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 5.0 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
./modify_noisy 7 10.0 < CITalgo.csv | ./noisycdf >> CITcdfalgo.csv
python evalDegDist.py 1 8 > testing.csv
./clear < testing.csv >> CIT.csv
rm testing.csv
