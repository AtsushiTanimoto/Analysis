import subprocess


if __name__=="__main__":
    subprocess.run("export SAS_ODF=../odf" , shell=True)
    subprocess.run("export SAS_CCF=ccf.cif", shell=True)
    subprocess.run("cifbuild" , shell=True)
    subprocess.run("odfingest", shell=True)