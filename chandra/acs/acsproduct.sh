#!/bin/sh
file=`ls *evt2.fits`
specextract bkgfile="${file}[sky=region(bkg.reg)]" infile="${file}[sky=region(src.reg)]" outroot=acs

mv acs_bkg.pi acsbkg.pha
mv acs.arf    acssrc.arf
mv acs.pi     acssrc.pha
mv acs.rmf    acssrc.rmf