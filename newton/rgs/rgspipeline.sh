#!/bin/bash
#Reprocess RGS data
rgsproc bkgcorrect=no orders="1 2" spectrumbinning=lambda withmlambdacolumn=yes


#Rename
mv *R1U*EVENLI* rgs01.fits
mv *R2U*EVENLI* rgs02.fits