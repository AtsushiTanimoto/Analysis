import glob
import heasoftpy
import subprocess


if __name__=="__main__":
    atfile      = glob.glob("*attorb")[0]
    exfile      = glob.glob("*xpcw3po_ex.img")[0]
    hkfile      = glob.glob("*.hk")[0]
    infile      = glob.glob("*xpcw3po_cl.evt")[0]
    xrtproducts = heasoftpy.HSPTask("xrtproducts")
    xrtproducts(infile="{0:s}".format(infile), regionfile="sour.reg", bkgextract="yes", bkgregionfile="back.reg", outdir=".", expofile="{0:s}".format(exfile), correctlc="no", clobber="yes", noprompt=True, verbose=True)
    subprocess.run("mv *xpcw3pobkg.pha xrtbkg.pha", shell=True)
    subprocess.run("mv *xpcw3posr.pha  xrtsrc.pha", shell=True)
    subprocess.run("mv *xpcw3posr.arf  xrtsrc.arf", shell=True)
