#!/usr/bin/env bash

#Region
xbkg=`cat bkg.reg | cut -sd"(" -f2 | cut -d"," -f1`
xsrc=`cat src.reg | cut -sd"(" -f2 | cut -d"," -f1`
ybkg=`cat bkg.reg | cut -sd"," -f2 | cut -d"," -f1`
ysrc=`cat src.reg | cut -sd"," -f2 | cut -d"," -f1`

#Evselect
evselect table=mos1.flt energycolumn=PI withfilteredset=yes filteredset=mos1src.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xsrc,$ysrc,600))" withspectrumset=yes spectrumset=mos1src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=mos2.flt energycolumn=PI withfilteredset=yes filteredset=mos2src.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xsrc,$ysrc,600))" withspectrumset=yes spectrumset=mos2src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=epn1.flt energycolumn=PI withfilteredset=yes filteredset=epn1src.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xsrc,$ysrc,600)) && (FLAG == 0) && (PATTERN <= 4)" withspectrumset=yes spectrumset=epn1src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479
evselect table=mos1.flt energycolumn=PI withfilteredset=yes filteredset=mos1bkg.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xbkg,$ybkg,600))" withspectrumset=yes spectrumset=mos1bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=mos2.flt energycolumn=PI withfilteredset=yes filteredset=mos2bkg.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xbkg,$ybkg,600))" withspectrumset=yes spectrumset=mos2bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999
evselect table=epn1.flt energycolumn=PI withfilteredset=yes filteredset=epn1bkg.fits keepfilteroutput=yes filtertype=expression expression="((X,Y) in CIRCLE($xbkg,$ybkg,600)) && (FLAG == 0) && (PATTERN <= 4)" withspectrumset=yes spectrumset=epn1bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479

#Backscale
backscale spectrumset=mos1src.pha badpixlocation=mos1.flt
backscale spectrumset=mos2src.pha badpixlocation=mos2.flt
backscale spectrumset=epn1src.pha badpixlocation=epn1.flt
backscale spectrumset=mos1bkg.pha badpixlocation=mos1.flt
backscale spectrumset=mos2bkg.pha badpixlocation=mos2.flt
backscale spectrumset=epn1bkg.pha badpixlocation=epn1.flt

#Rmfgen
rmfgen rmfset=mos1src.rmf spectrumset=mos1src.pha
rmfgen rmfset=mos2src.rmf spectrumset=mos2src.pha
rmfgen rmfset=epn1src.rmf spectrumset=epn1src.pha

#Arfgen
arfgen arfset=mos1src.arf spectrumset=mos1src.pha withrmfset=yes rmfset=mos1src.rmf withbadpixcorr=yes badpixlocation=mos1.flt
arfgen arfset=mos2src.arf spectrumset=mos2src.pha withrmfset=yes rmfset=mos2src.rmf withbadpixcorr=yes badpixlocation=mos2.flt
arfgen arfset=epn1src.arf spectrumset=epn1src.pha withrmfset=yes rmfset=epn1src.rmf withbadpixcorr=yes badpixlocation=epn1.flt
