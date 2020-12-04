#!/bin/bash
number=`ls ../../`
nuproducts indir=. outdir=. steminputs=nu$number instrument=FPMA srcregionfile=src.reg bkgregionfile=bkg.reg bkgextract=yes
nuproducts indir=. outdir=. steminputs=nu$number instrument=FPMB srcregionfile=src.reg bkgregionfile=bkg.reg bkgextract=yes

mv nu*A01.flc    fpmasrc.flc
mv nu*A01_bk.lc  fpmabkg.lc
mv nu*A01_bk.pha fpmabkg.pha
mv nu*A01_im.gif fpmaimg.gif
mv nu*A01_lc.gif fpmalic.gif
mv nu*A01_ph.gif fpmapha.gif
mv nu*A01_sk.img fpmasky.img
mv nu*A01_sr.arf fpmasrc.arf
mv nu*A01_sr.lc  fpmasrc.lc
mv nu*A01_sr.pha fpmasrc.pha
mv nu*A01_sr.rmf fpmasrc.rmf
mv nu*B01.flc    fpmbsrc.flc
mv nu*B01_bk.lc  fpmbbkg.lc
mv nu*B01_bk.pha fpmbbkg.pha
mv nu*B01_im.gif fpmbimg.gif
mv nu*B01_lc.gif fpmblic.gif
mv nu*B01_ph.gif fpmbpha.gif
mv nu*B01_sk.img fpmbsky.img
mv nu*B01_sr.arf fpmbsrc.arf
mv nu*B01_sr.lc  fpmbsrc.lc
mv nu*B01_sr.pha fpmbsrc.pha
mv nu*B01_sr.rmf fpmbsrc.rmf