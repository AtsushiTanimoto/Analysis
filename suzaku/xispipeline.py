import os
import subprocess


if __name__=="__main__":
    obsid   = os.listdir("../suzaku/")[0]
    subprocess.run("aepipeline indir=../suzaku/{0:s} outdir=. steminputs={0:s} entry_stage=1 exit_stage=2 instrument=XIS clobber=yes".format(obsid), shell=True)