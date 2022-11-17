import glob
import heasoftpy
import re



if __name__=="__main__": 
    xis0att = glob.glob("*.att")[0]
    xis1att = glob.glob("*.att")[0]
    xis2att = glob.glob("*.att")[0]
    xis3att = glob.glob("*.att")[0]
    xis0gti = glob.glob("*xi0*3x3*cl.evt")
    xis1gti = glob.glob("*xi1*3x3*cl.evt")
    xis2gti = glob.glob("*xi2*3x3*cl.evt")
    xis3gti = glob.glob("*xi3*3x3*cl.evt")

    with open("sour.reg", mode="r") as fin:
        for data in fin.readlines():
            if data[:6]=="circle":
                sourx = re.findall("\d+(?:\.\d+)?", data)[0]
                soury = re.findall("\d+(?:\.\d+)?", data)[1]
    
    xissimarfgen = heasoftpy.HSPTask("xissimarfgen")
    
    if 0<len(xis0gti):
        xissimarfgen(instrume="XIS0", rmffile="xis0src.rmf", estepfile="dense", source_mode="SKYXY", source_x="{0:s}".format(sourx), source_y="{0:s}".format(soury), num_region=1, region_mode="SKYREG", regfile1="sour.reg", arffile1="xis0src.arf", detmask="none", limit_mode="NUM_PHOTON", num_photon=100000, gtifile="{0:s}".format(xis0gti[0]), pointing="AUTO", attitude="{0:s}".format(xis0att), phafile="xis0src.pha", noprompt=True, verbose=True)
    if 0<len(xis1gti):
        xissimarfgen(instrume="XIS1", rmffile="xis1src.rmf", estepfile="dense", source_mode="SKYXY", source_x="{0:s}".format(sourx), source_y="{0:s}".format(soury), num_region=1, region_mode="SKYREG", regfile1="sour.reg", arffile1="xis1src.arf", detmask="none", limit_mode="NUM_PHOTON", num_photon=100000, gtifile="{0:s}".format(xis1gti[0]), pointing="AUTO", attitude="{0:s}".format(xis1att), phafile="xis1src.pha", noprompt=True, verbose=True)
    if 0<len(xis2gti):
        xissimarfgen(instrume="XIS2", rmffile="xis2src.rmf", estepfile="dense", source_mode="SKYXY", source_x="{0:s}".format(sourx), source_y="{0:s}".format(soury), num_region=1, region_mode="SKYREG", regfile1="sour.reg", arffile1="xis2src.arf", detmask="none", limit_mode="NUM_PHOTON", num_photon=100000, gtifile="{0:s}".format(xis2gti[0]), pointing="AUTO", attitude="{0:s}".format(xis2att), phafile="xis2src.pha", noprompt=True, verbose=True)
    if 0<len(xis3gti):
        xissimarfgen(instrume="XIS3", rmffile="xis3src.rmf", estepfile="dense", source_mode="SKYXY", source_x="{0:s}".format(sourx), source_y="{0:s}".format(soury), num_region=1, region_mode="SKYREG", regfile1="sour.reg", arffile1="xis3src.arf", detmask="none", limit_mode="NUM_PHOTON", num_photon=100000, gtifile="{0:s}".format(xis3gti[0]), pointing="AUTO", attitude="{0:s}".format(xis3att), phafile="xis3src.pha", noprompt=True, verbose=True)    