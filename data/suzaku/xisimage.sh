#!/bin/bash
ls *xi0*cl* > xis.txt
xselect<<EOF
xsel
no
read event
.
xis.txt
extract image
save image xis0src.fits
EOF
rm xis.txt
