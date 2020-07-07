#!/bin/bash

python algo.py 4 8 > testing.csv
./clear < testing.csv >> WIKIalgo.csv
./modify_noisy 7 0.01 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 0.02 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 0.05 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 0.1 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 0.2 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 0.5 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 1.0 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 2.0 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 5.0 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
./modify_noisy 7 10.0 < WIKIalgo.csv | ./noisycdf >> WIKIcdfalgo.csv
python evalDegDist.py 4 8 > testing.csv
./clear < testing.csv >> WIKI.csv
rm testing.csv
