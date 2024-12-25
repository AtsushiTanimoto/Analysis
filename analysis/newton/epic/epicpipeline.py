import subprocess


if __name__=="__main__":
    subprocess.run("mv *EMOS1*ImagingEvts.ds mos01.fits", shell=True)
    subprocess.run("mv *EMOS2*ImagingEvts.ds mos02.fits", shell=True)
    subprocess.run("mv *EPN*ImagingEvts.ds epn01.fits", shell=True)

    #Create Light Curve
    subprocess.run("evselect table=mos01.fits withrateset=yes rateset=mos01.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression='(PATTERN == 0) && (PI > 10000) && #XMMEA_EM'", shell=True)
    subprocess.run("evselect table=mos02.fits withrateset=yes rateset=mos02.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression='(PATTERN == 0) && (PI > 10000) && #XMMEA_EM'", shell=True)
    subprocess.run("evselect table=epn01.fits withrateset=yes rateset=epn01.lc maketimecolumn=yes timecolumn=TIME timebinsize=100 makeratecolumn=yes expression='(PATTERN == 0) && (PI in [10000:12000] && #XMMEA_EP)'", shell=True)

    #Create Gti
    subprocess.run("tabgtigen table=mos01.lc gtiset=mos01.gti timecolumn=TIME expression='(RATE <= 1)'", shell=True)
    subprocess.run("tabgtigen table=mos02.lc gtiset=mos02.gti timecolumn=TIME expression='(RATE <= 1)'", shell=True)
    subprocess.run("tabgtigen table=epn01.lc gtiset=epn01.gti timecolumn=TIME expression='(RATE <= 1)'", shell=True)

    #Applying Time Filters
    subprocess.run("evselect table=mos01.fits withfilteredset=yes expression='GTI(mos01.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EM' filteredset=mos01.ffits filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes", shell=True)
    subprocess.run("evselect table=mos02.fits withfilteredset=yes expression='GTI(mos02.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EM' filteredset=mos02.ffits filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes", shell=True)
    subprocess.run("evselect table=epn01.fits withfilteredset=yes expression='GTI(epn01.gti,TIME) && (PATTERN <= 12) && (PI in [200:12000]) && #XMMEA_EP' filteredset=epn01.ffits filtertype=expression keepfilteroutput=yes updateexposure=yes filterexposure=yes", shell=True)