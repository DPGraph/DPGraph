#!/bin/bash
cd uploads/
rm *.csv 
cp ../*.csv .
chmod u+x *.sh
echo "7,new_algorithm">>looking.csv
./create_FACEBOOK.sh
