#!/bin/sh

sh='txt_data/set_sh.txt'
py='txt_data/set.txt'

cut -f 1 txt_data/hightemp.txt | sort | uniq > $sh

python 17.py | sort > $py

diff --report-identical-files $sh $py

