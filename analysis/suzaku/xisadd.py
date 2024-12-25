import glob
import subprocess


if __name__=="__main__":
    xis2    = glob.glob("xis2*")

    if 0<len(xis2):
        subprocess.run("addascaspec xisb1.dat xibsrc.pha xibsrc.rsp xibbkg.pha", shell=True)
        subprocess.run("addascaspec xisf1.dat xifsrc.pha xifsrc.rsp xifbkg.pha", shell=True)
    else:
        subprocess.run("addascaspec xisb1.dat xibsrc.pha xibsrc.rsp xibbkg.pha", shell=True)
        subprocess.run("addascaspec xisf2.dat xifsrc.pha xifsrc.rsp xifbkg.pha", shell=True)
    
    subprocess.run("mv xibbkg.pha ../../../analysis/", shell=True)
    subprocess.run("mv xibsrc.pha ../../../analysis/", shell=True)
    subprocess.run("mv xibsrc.rsp ../../../analysis/", shell=True)
    subprocess.run("mv xifbkg.pha ../../../analysis/", shell=True)
    subprocess.run("mv xifsrc.pha ../../../analysis/", shell=True)
    subprocess.run("mv xifsrc.rsp ../../../analysis/", shell=True)