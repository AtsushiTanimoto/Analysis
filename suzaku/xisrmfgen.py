import subprocess


if __name__=="__main__":
    subprocess.run("xisrmfgen phafile=xis0src.pha outfile=xis0src.rmf", shell=True)
    subprocess.run("xisrmfgen phafile=xis1src.pha outfile=xis1src.rmf", shell=True)
    subprocess.run("xisrmfgen phafile=xis2src.pha outfile=xis2src.rmf", shell=True)
    subprocess.run("xisrmfgen phafile=xis3src.pha outfile=xis3src.rmf", shell=True)