#!/bin/bash
#Generate Lightcurve
evselect table=rgs01.fits withrateset=yes rateset=rgs01.lc maketimecolumn=yes timebinsize=100 makeratecolumn=yes expression="(CCDNR==9)&&(REGION(P0112210201R1U002SRCLI_0000.FIT:RGS1_BACKGROUND, M_LAMBDA, XDSP_CORR))"
evselect table=rgs02.fits withrateset=yes rateset=rgs02.lc maketimecolumn=yes timebinsize=100 makeratecolumn=yes expression="(CCDNR==9)&&(REGION(P0112210201R2U002SRCLI_0000.FIT:RGS2_BACKGROUND, M_LAMBDA, XDSP_CORR))"


#Generate GTI
#tabgtigen table=rgs01.lc gtiset=rgs01.gti expression="RATE<0.2"
#tabgtigen table=rgs02.lc gtiset=rgs02.gti expression="RATE<0.2"


#Apply GTI
#rgsproc orders="1 2" auxgtitables=rgs01.gti bkgcorrect=no withmlambdacolumn=yes entrystage=3:filter finalstage=5:fluxing
#rgsproc orders="1 2" auxgtitables=rgs02.gti bkgcorrect=no withmlambdacolumn=yes entrystage=3:filter finalstage=5:fluxing