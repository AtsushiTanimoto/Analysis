#!/bin/bash
#Reprocess RGS data
rgsproc rebin=5 rmfbins=5000 spectrumbinning=lambda withmlambdacolumn=yes


#Rename
mv *R1S*EVENLI* rgs01.fits
mv *R2S*EVENLI* rgs02.fits


#Generate RMF
rgssrcpha0101=`ls *R1S*SRSPEC1001*`
rgssrcpha0102=`ls *R1S*SRSPEC2001*`
rgssrcpha0201=`ls *R2S*SRSPEC1001*`
rgssrcpha0202=`ls *R2S*SRSPEC2001*`
rgsrmfgen emin=0.5 emax=2.5 evlist=rgs01.fits rmfset=rgs0101.rmf rows=5000 spectrumset=$rgssrcpha0101
rgsrmfgen emin=0.5 emax=2.5 evlist=rgs01.fits rmfset=rgs0102.rmf rows=5000 spectrumset=$rgssrcpha0102
rgsrmfgen emin=0.5 emax=2.5 evlist=rgs02.fits rmfset=rgs0201.rmf rows=5000 spectrumset=$rgssrcpha0201
rgsrmfgen emin=0.5 emax=2.5 evlist=rgs02.fits rmfset=rgs0202.rmf rows=5000 spectrumset=$rgssrcpha0202


#Combine Spectra
rgsbkgpha0101=`ls *R1S*BGSPEC1001*`
rgsbkgpha0102=`ls *R1S*BGSPEC2001*`
rgsbkgpha0201=`ls *R2S*BGSPEC1001*`
rgsbkgpha0202=`ls *R2S*BGSPEC2001*`
rgscombine bkg="$rgsbkgpha0101 $rgsbkgpha0201" filebkg="rgs01bkg.pha" filepha="rgs01src.pha" filermf="rgs01.rmf" pha="$rgssrcpha0101 $rgssrcpha0201" rmf="rgs0101.rmf rgs0201.rmf" rmfgrid=5000
rgscombine bkg="$rgsbkgpha0102 $rgsbkgpha0202" filebkg="rgs02bkg.pha" filepha="rgs02src.pha" filermf="rgs02.rmf" pha="$rgssrcpha0102 $rgssrcpha0202" rmf="rgs0102.rmf rgs0202.rmf" rmfgrid=5000