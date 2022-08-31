#!/bin/bash
ls *xi0*cl* > xis0.txt
ls *xi1*cl* > xis1.txt
ls *xi2*cl* > xis2.txt
ls *xi3*cl* > xis3.txt


for xis in xis0 xis1 xis2 xis3
do
for reg in bkg src
do
xselect<<EOF
xsel
no
read event
.
${xis}.txt
filter region ${reg}.reg
extract spec
save spec ${xis}${reg}.pha
no
exit
no
EOF
done
done


rm xis0.txt
rm xis1.txt
rm xis2.txt
rm xis3.txt
