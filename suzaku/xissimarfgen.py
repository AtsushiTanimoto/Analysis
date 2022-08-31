import glob
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

    with open("src.reg", mode="r") as fin:
        for data in fin.readlines():
            if data[:6]=="circle":
                soux = data[ 7:16]
                souy = data[17:26]
    
    if len(xis0gti)==1:
        subprocess.run("xissimarfgen instrume=XIS0 rmffile=xis0src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis0src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis0src.pha".format(soux, souy, xis0gti[0], xis0att), shell=True)
    if len(xis1gti)==1:
        subprocess.run("xissimarfgen instrume=XIS1 rmffile=xis1src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis1src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis1src.pha".format(soux, souy, xis1gti[0], xis1att), shell=True)
    if len(xis2gti)==1:
        subprocess.run("xissimarfgen instrume=XIS2 rmffile=xis2src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis2src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis2src.pha".format(soux, souy, xis2gti[0], xis2att), shell=True)
    if len(xis3gti)==1:
        subprocess.run("xissimarfgen instrume=XIS3 rmffile=xis3src.rmf estepfile=dense source_mode=SKYXY source_x={0:s} source_y={1:s} num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis3src.arf detmask=none limit_mode=NUM_PHOTON num_photon=100000 gtifile={2:s} pointing=AUTO attitude={3:s} phafile=xis3src.pha".format(soux, souy, xis3gti[0], xis3att), shell=True)