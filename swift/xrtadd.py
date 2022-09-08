import subprocess


if __name__=="__main__":
    subprocess.run("addascaspec xrt.dat xrtsrc.pha xrtsrc.rsp xrtbkg.pha", shell=True)
    subprocess.run("mv xrtsrc.pha	../../../analysis/", shell=True)
    subprocess.run("mv xrtbkg.pha	../../../analysis/", shell=True)
    subprocess.run("mv xrtsrc.rsp	../../../analysis/", shell=True)