#!/bin/bash
ls *xi0*cl* > xis.txt
xselect<<EOF
xsel
no
read event
./
xis.txt
extract image
saoimage
EOF
rm xis.txt
