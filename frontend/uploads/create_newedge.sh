#!/bin/bash
cd uploads/
rm *.csv 
cp sample/*.csv .
cp sample/*.py .
chmod u+x *.sh
echo "3,new_algorithm">>lookingedge.csv
./create_FACEBOOKedge.sh

