import subprocess


if __name__=="__main__":
    subprocess.run("chandra_repro indir=../ outdir=../analysis", shell=True)