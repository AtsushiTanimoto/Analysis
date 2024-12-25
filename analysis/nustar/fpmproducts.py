import heasoftpy
import os
import subprocess


if __name__=="__main__":
    obsid           = os.listdir("../../")[0]
    steminputs      = "nu{0:s}".format(obsid)
    nuproducts01    = heasoftpy.HSPTask("nuproducts")
    nuproducts02    = heasoftpy.HSPTask("nuproducts")
    nuproducts01({"indir":".", "instrument":"FPMA", "steminputs":"{0:s}".format(steminputs), "outdir":".", "srcregionfile":"sour.reg", "bkgregionfile":"back.reg"}, noprompt=True, verbose=True)
    nuproducts02({"indir":".", "instrument":"FPMB", "steminputs":"{0:s}".format(steminputs), "outdir":".", "srcregionfile":"sour.reg", "bkgregionfile":"back.reg"}, noprompt=True, verbose=True)