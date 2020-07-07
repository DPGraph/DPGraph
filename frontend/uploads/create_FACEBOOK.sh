#!/bin/bash

python algo.py 0 8 > testing.csv
./clear < testing.csv >> FACEBOOKalgo.csv
./modify_noisy 7 0.01 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 0.02 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 0.05 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 0.1 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 0.2 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 0.5 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 1.0 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 2.0 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 5.0 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
./modify_noisy 7 10.0 < FACEBOOKalgo.csv | ./noisycdf >> FACEBOOKcdfalgo.csv
python evalDegDist.py 0 8 > testing.csv
./clear < testing.csv >> FACEBOOK.csv
rm testing.csv
