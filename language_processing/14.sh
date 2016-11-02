#!/bin/sh

echo "input number : "
read n

head -n $n hightemp.txt > head_n_sh.txt

diff --report-identical-files head_n.txt head_n_sh.txt
