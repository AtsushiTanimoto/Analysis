#!/usr/bin/env bash
#mv
mv *EMOS1*ImagingEvts.ds	mos01.fits
mv *EMOS2*ImagingEvts.ds	mos02.fits
mv *EPN*ImagingEvts.ds		epn01.fits

#Create Light Curve
evselect table=mos01.fits withrateset=yes rateset=mos01.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression="(PATTERN == 0) && (PI > 10000) && #XMMEA_EM"
evselect table=mos02.fits withrateset=yes rateset=mos02.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression="(PATTERN == 0) && (PI > 10000) && #XMMEA_EM"
evselect table=epn01.fits withrateset=yes rateset=epn01.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression="(PATTERN == 0) && (PI in [10000:12000] && #XMMEA_EP)"

#Create Gti
tabgtigen table=mos01.lc gtiset=mos01.gti timecolumn=TIME expression="(RATE <= 1)"
tabgtigen table=mos02.lc gtiset=mos02.gti timecolumn=TIME expression="(RATE <= 1)"
tabgtigen table=epn01.lc gtiset=epn01.gti timecolumn=TIME expression="(RATE <= 1)"

#Applying Time Filters
evselect table=mos01.fits withfilteredset=yes expression="GTI(mos01.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EM" filteredset=mos01.ffits filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes
evselect table=mos02.fits withfilteredset=yes expression="GTI(mos02.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EM" filteredset=mos02.ffits filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes
evselect table=epn01.fits withfilteredset=yes expression="GTI(epn01.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EP" filteredset=epn01.ffits filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes