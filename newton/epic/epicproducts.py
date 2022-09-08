import subprocess


if __name__=="__main__":
    with open("back.reg", mode="r") as fin:
        for data in fin.readlines():
            if data[:6]=="circle":
                backx = data[ 7:16]
                backy = data[17:26]
    
    with open("sour.reg", mode="r") as fin:
        for data in fin.readlines():
            if data[:6]=="circle":
                sourx = data[ 7:16]
                soury = data[17:26]

    #Evselect
    subprocess.run("evselect table=mos01.ffits energycolumn=PI withfilteredset=yes filteredset=mos01bkg.fits keepfilteroutput=yes filtertype=expression expression='((X,Y) in CIRCLE({0:s},{1:s},600))'                                     withspectrumset=yes spectrumset=mos01src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999".format(backx,backy), shell=True)
    subprocess.run("evselect table=mos01.ffits energycolumn=PI withfilteredset=yes filteredset=mos01src.fits keepfilteroutput=yes filtertype=expression expression='((X,Y) in CIRCLE({0:s},{1:s},600))'                                     withspectrumset=yes spectrumset=mos01bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999".format(sourx,soury), shell=True)
    subprocess.run("evselect table=mos02.ffits energycolumn=PI withfilteredset=yes filteredset=mos02bkg.fits keepfilteroutput=yes filtertype=expression expression='((X,Y) in CIRCLE({0:s},{1:s},600))'                                     withspectrumset=yes spectrumset=mos02src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999".format(backx,backy), shell=True)
    subprocess.run("evselect table=mos02.ffits energycolumn=PI withfilteredset=yes filteredset=mos02src.fits keepfilteroutput=yes filtertype=expression expression='((X,Y) in CIRCLE({0:s},{1:s},600))'                                     withspectrumset=yes spectrumset=mos02bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=11999".format(sourx,soury), shell=True)
    subprocess.run("evselect table=epn01.ffits energycolumn=PI withfilteredset=yes filteredset=epn01bkg.fits keepfilteroutput=yes filtertype=expression expression='((X,Y) in CIRCLE({0:s},{1:s},600)) && (FLAG == 0) && (PATTERN <= 4)'    withspectrumset=yes spectrumset=epn01src.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479".format(backx,backy), shell=True)
    subprocess.run("evselect table=epn01.ffits energycolumn=PI withfilteredset=yes filteredset=epn01src.fits keepfilteroutput=yes filtertype=expression expression='((X,Y) in CIRCLE({0:s},{1:s},600)) && (FLAG == 0) && (PATTERN <= 4)'    withspectrumset=yes spectrumset=epn01bkg.pha spectralbinsize=5 withspecranges=yes specchannelmin=0 specchannelmax=20479".format(sourx,soury), shell=True)

    #Backscale
    subprocess.run("backscale spectrumset=mos01src.pha badpixlocation=mos01.ffits", shell=True)
    subprocess.run("backscale spectrumset=mos01bkg.pha badpixlocation=mos01.ffits", shell=True)
    subprocess.run("backscale spectrumset=mos02src.pha badpixlocation=mos02.ffits", shell=True)
    subprocess.run("backscale spectrumset=mos02bkg.pha badpixlocation=mos02.ffits", shell=True)
    subprocess.run("backscale spectrumset=epn01src.pha badpixlocation=epn01.ffits", shell=True)
    subprocess.run("backscale spectrumset=epn01bkg.pha badpixlocation=epn01.ffits", shell=True)

    #Rmfgen
    subprocess.run("rmfgen rmfset=mos01src.rmf spectrumset=mos01src.pha", shell=True)
    subprocess.run("rmfgen rmfset=mos02src.rmf spectrumset=mos02src.pha", shell=True)
    subprocess.run("rmfgen rmfset=epn01src.rmf spectrumset=epn01src.pha", shell=True)

    #Arfgen
    subprocess.run("arfgen arfset=mos01src.arf spectrumset=mos01src.pha withrmfset=yes rmfset=mos01src.rmf withbadpixcorr=yes badpixlocation=mos01.ffits", shell=True)
    subprocess.run("arfgen arfset=mos02src.arf spectrumset=mos02src.pha withrmfset=yes rmfset=mos02src.rmf withbadpixcorr=yes badpixlocation=mos02.ffits", shell=True)
    subprocess.run("arfgen arfset=epn01src.arf spectrumset=epn01src.pha withrmfset=yes rmfset=epn01src.rmf withbadpixcorr=yes badpixlocation=epn01.ffits", shell=True)