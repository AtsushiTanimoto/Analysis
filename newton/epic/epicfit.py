import subprocess


if __name__=="__main__":
    subprocess.run("addascaspec epn.dat epnsrc.pha epnsrc.rsp epnbkg.pha", shell=True)
    subprocess.run("addascaspec mos.dat mossrc.pha mossrc.rsp mosbkg.pha", shell=True)
    subprocess.run("mv mossrc.pha	../../../analysis/", shell=True)
    subprocess.run("mv mosbkg.pha	../../../analysis/", shell=True)
    subprocess.run("mv mossrc.rsp	../../../analysis/", shell=True)
    subprocess.run("mv epnsrc.pha	../../../analysis/", shell=True)
    subprocess.run("mv epnbkg.pha	../../../analysis/", shell=True)
    subprocess.run("mv epnsrc.rsp	../../../analysis/", shell=True)