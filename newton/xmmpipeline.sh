#!/usr/bin/env bash
#mv
mv *EMOS1*ImagingEvts.ds	mos1.fits
mv *EMOS2*ImagingEvts.ds	mos2.fits
mv *EPN*ImagingEvts.ds		epn1.fits

#Create Light Curve
evselect table=mos1.fits withrateset=yes rateset=mos1.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression="(PATTERN == 0) && (PI > 10000) && #XMMEA_EM"
evselect table=mos2.fits withrateset=yes rateset=mos2.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression="(PATTERN == 0) && (PI > 10000) && #XMMEA_EM"
evselect table=epn1.fits withrateset=yes rateset=epn1.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression="(PATTERN == 0) && (PI in [10000:12000] && #XMMEA_EP)"

#Create Gti
tabgtigen table=mos1.lc gtiset=mos1.gti timecolumn=TIME expression="(RATE <= 1)"
tabgtigen table=mos2.lc gtiset=mos2.gti timecolumn=TIME expression="(RATE <= 1)"
tabgtigen table=epn1.lc gtiset=epn1.gti timecolumn=TIME expression="(RATE <= 1)"

#Applying Time Filters
evselect table=mos1.fits withfilteredset=yes expression="GTI(mos1.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EM" filteredset=mos1.flt filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes
evselect table=mos2.fits withfilteredset=yes expression="GTI(mos2.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EM" filteredset=mos2.flt filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes
evselect table=epn1.fits withfilteredset=yes expression="GTI(epn1.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EP" filteredset=epn1.flt filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes