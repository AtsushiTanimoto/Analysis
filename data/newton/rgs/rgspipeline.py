import subprocess


if __name__=="__main__":
    subprocess.run("cifbuild" , shell=True)
    subprocess.run("odfingest", shell=True)