#!/bin/sh

echo "input number : "
read n

tail -n $n txt_data/hightemp.txt > txt_data/tail_n_sh.txt

diff --report-identical-files txt_data/tail_n.txt txt_data/tail_n_sh.txt
