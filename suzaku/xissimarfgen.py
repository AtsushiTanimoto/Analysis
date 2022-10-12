import glob
import re
import subprocess


if __name__=="__main__": 
    xis0att = glob.glob("*.att")[0]
    xis1att = glob.glob("*.att")[0]
    xis2att = glob.glob("*.att")[0]
    xis3att = glob.glob("*.att")[0]
    xis0gti = glob.glob("*xi0*3*cl.evt")
    xis1gti = glob.glob("*xi1*3*cl.evt")
    xis2gti = glob.glob("*xi2*3*cl.evt")
    xis3gti = glob.glob("*xi3*3*cl.evt")

    with open("sour.reg", mode="r") as fin:
        for data in fin.readlines():
            if data[:6]=="circle":
                sourx = re.findall("\d+(?:\.\d+)?", data)[0]
                soury = re.findall("\d+(?:\.\d+)?", data)[1]
    
    if 1<=len(xis0gti):
        subprocess.run("xissimarfgen instrume=XIS0 rmffile=xis0src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=sour.reg arffile1=xis0src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis0src.pha".format(sourx, soury, xis0gti[0], xis0att), shell=True)
    if 1<=len(xis1gti):
        subprocess.run("xissimarfgen instrume=XIS1 rmffile=xis1src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=sour.reg arffile1=xis1src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis1src.pha".format(sourx, soury, xis1gti[0], xis1att), shell=True)
    if 1<=len(xis2gti):
        subprocess.run("xissimarfgen instrume=XIS2 rmffile=xis2src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=sour.reg arffile1=xis2src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis2src.pha".format(sourx, soury, xis2gti[0], xis2att), shell=True)
    if 1<=len(xis3gti):
        subprocess.run("xissimarfgen instrume=XIS3 rmffile=xis3src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=sour.reg arffile1=xis3src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis3src.pha".format(sourx, soury, xis3gti[0], xis3att), shell=True)