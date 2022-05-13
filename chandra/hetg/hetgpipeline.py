import subprocess


if __name__=="__main__":
    subprocess.run("mv heg_1.arf heg_+1.arf", shell=True)
    subprocess.run("mv heg_1.pha heg_+1.pha", shell=True)
    subprocess.run("mv heg_1.rmf heg_+1.rmf", shell=True)
    subprocess.run("mv meg_1.arf meg_+1.arf", shell=True)
    subprocess.run("mv meg_1.pha meg_+1.pha", shell=True)
    subprocess.run("mv meg_1.rmf meg_+1.rmf", shell=True)