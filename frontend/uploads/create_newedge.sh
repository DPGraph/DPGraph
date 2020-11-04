#!/bin/bash
cd uploads/
rm *.csv
chmod u+x *.sh
cp ../*.csv .
echo "3,new_algorithm">>lookingedge.csv
./create_FACEBOOKedge.sh
