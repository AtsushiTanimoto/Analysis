import heasoftpy
import os


if __name__=="__main__":
    obsid       = os.listdir("../suzaku/")[0]
    aepipeline  = heasoftpy.HSPTask("aepipeline")
    aepipeline(indir="../suzaku/{0:s}".format(obsid), outdir=".", steminputs="{0:s}".format(obsid), entry_stage=1, exit_stage=2, instrument="XIS", clobber="yes", noprompt=True, verbose=True)