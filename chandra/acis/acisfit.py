import subprocess


if __name__=="__main__":
    subprocess.run("addascaspec acis.dat acssrc.pha acssrc.rsp acsbkg.pha", shell=True)
    subprocess.run("mv acsbkg.pha	../../../analysis", shell=True)
    subprocess.run("mv acssrc.pha	../../../analysis", shell=True)
    subprocess.run("mv acssrc.rsp	../../../analysis", shell=True)