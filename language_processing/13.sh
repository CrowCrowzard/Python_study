#!bin/sh
paste -d '\t' col1.txt col2.txt > col12_sh.txt

diff col12.txt col12_sh.txt
if [ $? -eq 0 ]; then
    echo 'success'
else
    echo 'failed'
fi

