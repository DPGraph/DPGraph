#!/bin/bash

python algo.py 2 8 > testing.csv
./clear < testing.csv >> DBLPalgo.csv
./modify_noisy 7 0.01 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 0.02 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 0.05 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 0.1 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 0.2 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 0.5 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 1.0 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 2.0 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 5.0 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
./modify_noisy 7 10.0 < DBLPalgo.csv | ./noisycdf >> DBLPcdfalgo.csv
python evalDegDist.py 2 8 > testing.csv
./clear < testing.csv >> DBLP.csv
rm testing.csv
