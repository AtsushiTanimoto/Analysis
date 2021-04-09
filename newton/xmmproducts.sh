#!/usr/bin/env bash
#Region
xbkg=`cat bkg.reg | cut -sd"(" -f2 | cut -d"," -f1`
xsrc=`cat src.reg | cut -sd"(" -f2 | cut -d"," -f1`
ybkg=`cat bkg.reg | cut -sd"," -f2 | cut -d"," -f1`
ysrc=`cat src.reg | cut -sd"," -f2 | cut -d"," -f1`


#Evselect
evselect table=mos01.ffits energycolumn=PI withfilteredset=yes filteredset=mos01src.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xsrc,$ysrc,600))" withspectrumset=yes spectrumset=mos01src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=mos01.ffits energycolumn=PI withfilteredset=yes filteredset=mos01bkg.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xbkg,$ybkg,600))" withspectrumset=yes spectrumset=mos01bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=mos02.ffits energycolumn=PI withfilteredset=yes filteredset=mos02src.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xsrc,$ysrc,600))" withspectrumset=yes spectrumset=mos02src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=mos02.ffits energycolumn=PI withfilteredset=yes filteredset=mos02bkg.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xbkg,$ybkg,600))" withspectrumset=yes spectrumset=mos02bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=epn01.ffits energycolumn=PI withfilteredset=yes filteredset=epn01src.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xsrc,$ysrc,600)) && (FLAG == 0) && (PATTERN <= 4)" withspectrumset=yes spectrumset=epn01src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479
evselect table=epn01.ffits energycolumn=PI withfilteredset=yes filteredset=epn01bkg.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xbkg,$ybkg,600)) && (FLAG == 0) && (PATTERN <= 4)" withspectrumset=yes spectrumset=epn01bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479


#Backscale
backscale spectrumset=mos01src.pha badpixlocation=mos01.ffits
backscale spectrumset=mos01bkg.pha badpixlocation=mos01.ffits
backscale spectrumset=mos02src.pha badpixlocation=mos02.ffits
backscale spectrumset=mos02bkg.pha badpixlocation=mos02.ffits
backscale spectrumset=epn01src.pha badpixlocation=epn01.ffits
backscale spectrumset=epn01bkg.pha badpixlocation=epn01.ffits


#Rmfgen
rmfgen rmfset=mos01src.rmf spectrumset=mos01src.pha
rmfgen rmfset=mos02src.rmf spectrumset=mos02src.pha
rmfgen rmfset=epn01src.rmf spectrumset=epn01src.pha


#Arfgen
arfgen arfset=mos01src.arf spectrumset=mos01src.pha withrmfset=yes rmfset=mos01src.rmf withbadpixcorr=yes badpixlocation=mos01.ffits
arfgen arfset=mos02src.arf spectrumset=mos02src.pha withrmfset=yes rmfset=mos02src.rmf withbadpixcorr=yes badpixlocation=mos02.ffits
arfgen arfset=epn01src.arf spectrumset=epn01src.pha withrmfset=yes rmfset=epn01src.rmf withbadpixcorr=yes badpixlocation=epn01.ffits
