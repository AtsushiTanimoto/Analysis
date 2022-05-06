import glob
import subprocess


if __name__=="__main__":
    #Reprocess RGS data
    subprocess.run("rgsproc orders='1' spectrumbinning=lambda withmlambdacolumn=yes", shell=True)
    subprocess.run("mv *R1S*EVENLI* rgs01.fits",       shell=True)
    subprocess.run("mv *R2S*EVENLI* rgs02.fits",       shell=True)
    #subprocess.run("mv *R1S*BGSPEC1001* rgs01bkg.pha", shell=True)
    #subprocess.run("mv *R2S*BGSPEC1001* rgs02bkg.pha", shell=True)
    #subprocess.run("mv *R1S*SRSPEC1001* rgs01src.pha", shell=True)
    #subprocess.run("mv *R2S*SRSPEC1001* rgs02src.pha", shell=True)
    
    #Generate RMF
    subprocess.run("rgsrmfgen emin=0.5 emax=2.5 evlist=rgs01.fits rmfset=rgs01.rmf rows=5000 spectrumset=rgs01src.pha", shell=True)
    #subprocess.run("rgsrmfgen emin=0.5 emax=2.5 evlist=rgs02.fits rmfset=rgs02.rmf rows=5000 spectrumset=rgs02src.pha", shell=True)
    #subprocess.run("rgscombine bkg='rgs01bkg.pha rgs02bkg.pha' filebkg='rgs0001bkg.pha' filepha='rgs0001src.pha' filermf='rgs0001.rmf' pha='rgs01src.pha rgs02src.pha' rmf='rgs01.rmf rgs02.rmf' rmfgrid=5000", shell=True)