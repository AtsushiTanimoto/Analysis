import heasoftpy
import os


if __name__=="__main__":
    obsid       = os.listdir("../../")[0]
    indir       = "../../{0:s}".format(obsid)
    steminputs  = "nu{0:s}".format(obsid)
    nupipeline  = heasoftpy.HSPTask("nupipeline")
    nupipeline(indir=indir, steminputs=steminputs, outdir=".", saamode="optimized", tentacle="yes", noprompt=True, verbose=True)