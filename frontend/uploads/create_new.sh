#!/bin/bash
rm *.csv
chmod u+x *.sh
cp ../*.csv .
echo "7,new_algorithm">>looking.csv
./create_FACEBOOK.sh
./create_EMAIL.sh
./create_WIKI.sh
./create_DBLP.sh
./create_CIT.sh
./create_TOYDATA.sh
