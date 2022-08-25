import os
import subprocess


if __name__=="__main__":
    obsid = os.listdir("../swift/")[0]
    subprocess.run("xrtpipeline indir=../swift/{0:s} outdir=. steminputs=sw{0:s} srcra=OBJECT srcdec=OBJECT plotdevice=ps".format(obsid), shell=True)