import heasoftpy


if __name__=="__main__":
    print("Please input observation id.")
    obsid       = input()
    indir       = "../../{0:s}".format(obsid)
    steminputs  = "nu{0:s}".format(obsid)
    nupipeline  = heasoftpy.HSPTask("nupipeline")
    nupipeline(indir=indir, steminputs=steminputs, outdir=".", saamode="optimized", tentacle="yes", noprompt=True, verbose=True)