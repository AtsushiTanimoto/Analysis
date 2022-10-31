import heasoftpy
import os
import subprocess


if __name__=="__main__":
    obsid       = os.listdir("../../")[0]
    steminputs  = "nu{0:s}".format(obsid)
    nuproducts  = heasoftpy.HSPTask("nuproducts")
    nuproducts({"indir":".", "instrument":"FPMA", "steminputs":"{0:s}".format(steminputs), "outdir":".", "srcregionfile":"sour.reg", "bkgextract":"yes", "bkgregionfile":"back.reg"}, noprompt=True, verbose=True)
    nuproducts  = heasoftpy.HSPTask("nuproducts")
    nuproducts({"indir":".", "instrument":"FPMB", "steminputs":"{0:s}".format(steminputs), "outdir":".", "srcregionfile":"sour.reg", "bkgextract":"yes", "bkgregionfile":"back.reg"}, noprompt=True, verbose=True)
    
    subprocess.run("mv nu*A01_bk.pha fpmabkg.pha", shell=True)
    subprocess.run("mv nu*A01_sr.arf fpmasrc.arf", shell=True)
    subprocess.run("mv nu*A01_sr.pha fpmasrc.pha", shell=True)
    subprocess.run("mv nu*A01_sr.rmf fpmasrc.rmf", shell=True)
    subprocess.run("mv nu*B01_bk.pha fpmbbkg.pha", shell=True)
    subprocess.run("mv nu*B01_sr.arf fpmbsrc.arf", shell=True)
    subprocess.run("mv nu*B01_sr.pha fpmbsrc.pha", shell=True)
    subprocess.run("mv nu*B01_sr.rmf fpmbsrc.rmf", shell=True)