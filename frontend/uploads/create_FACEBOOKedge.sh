#!/bin/bash

python edgealgo.py 0 2 > testing.csv
./clear < testing.csv >> FACEBOOKedgealgo.csv
./modify_noisy 3 0.01 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 0.02 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 0.05 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 0.1 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 0.2 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 0.5 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 1.0 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 2.0 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 5.0 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
./modify_noisy 3 10.0 < FACEBOOKedgealgo.csv | ./noisycdf >> FACEBOOKcdfedgealgo.csv
python evalDegDistedge.py 0 2 > testing.csv
./clear < testing.csv >> FACEBOOKedge.csv
rm testing.csv
