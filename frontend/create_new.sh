#!/bin/bash
cd uploads/
rm *.csv 
cp sample/*.csv .
cp sample/*.py .
chmod u+x *.sh
echo "7,new_algorithm">>looking.csv
./create_FACEBOOK.sh