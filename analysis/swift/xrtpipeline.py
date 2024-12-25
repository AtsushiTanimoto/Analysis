import heasoftpy
import os


if __name__=="__main__":
    obsid = os.listdir("../swift/")[0]
    xrtpipeline = heasoftpy.HSPTask("xrtpipeline")
    xrtpipeline(indir="../swift/{0:s}".format(obsid), outdir=".", steminputs="sw{0:s}".format(obsid), srcra="OBJECT", srcdec="OBJECT", plotdevice="ps", noprompt=True, verbose=True)