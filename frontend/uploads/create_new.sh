#!/bin/bash
cd uploads/
chmod u+x *.sh
echo "7,new_algorithm">>looking.csv
./create_FACEBOOK.sh
