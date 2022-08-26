import glob
import subprocess


if __name__=="__main__":
    obsid = glob.glob("../../*")[0]
    subprocess.run("chandra_repro {0:s} outdir=.".format(obsid), shell=True)