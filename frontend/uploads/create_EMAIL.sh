#!/bin/bash

python algo.py 5 8 > testing.csv
./clear < testing.csv >> EMAILalgo.csv
./modify_noisy 7 0.01 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 0.02 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 0.05 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 0.1 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 0.2 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 0.5 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 1.0 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 2.0 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 5.0 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
./modify_noisy 7 10.0 < EMAILalgo.csv | ./noisycdf >> EMAILcdfalgo.csv
python evalDegDist.py 5 8 > testing.csv
./clear < testing.csv >> EMAIL.csv
rm testing.csv
