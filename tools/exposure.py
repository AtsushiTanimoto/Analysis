import astropy.io.fits
import os

if __name__=="__main__":
    if os.path.exists("acssrc.pha"):
        with astropy.io.fits.open("acssrc.pha") as fin:
            print("Exposure of Chandra/ACIS = {0:02d} ksec".format(round(fin[0].header["EXPOSURE"]/1000)))
    
    if os.path.exists("epnsrc.pha"):
        with astropy.io.fits.open("epnsrc.pha") as fin:
            print("Exposure of Newton/EPN   = {0:02d} ksec".format(round(fin[1].header["EXPOSURE"]/1000)))

    if os.path.exists("fpmsrc.pha"):
        with astropy.io.fits.open("fpmsrc.pha") as fin:
            print("Exposure of NuSTAR/FPMA  = {0:02d} ksec".format(round(fin[1].header["EXPOSURE"]/2000)))