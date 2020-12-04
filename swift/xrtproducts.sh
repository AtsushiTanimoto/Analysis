#!/usr/bin/env bash
infile=`ls *xpcw3po_cl.evt`
expofile=`ls *xpcw3po_ex.img`
xrtproducts bkgextract=yes bkgregionfile=bkg.reg correctlc=no clobber=yes expofile=$expofile infile=$infile outdir=. regionfile=src.reg  
mv *xpcw3pobkg.pha xrtbkg.pha
mv *xpcw3posr.pha  xrtsrc.pha
mv *xpcw3posr.arf  xrtsrc.arf
