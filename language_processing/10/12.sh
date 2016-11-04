#!/bin/sh

file='hightemp.txt'
out1='col1.txt'
out1_sh='col1_sh.txt'
out2='col2.txt'
out2_sh='col2_sh.txt'

cut -f 1 $file > $out1_sh
cut -f 2 $file > $out2_sh

diff $out1 $out1_sh
if [ $? -eq 0 ]; then
    diff $out2 $out2_sh
    if [ $? -eq 0 ]; then
        echo 'success'
    else
        echo 'failed'
    fi
else
    echo 'failed'
fi

