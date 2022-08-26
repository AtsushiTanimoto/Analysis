import glob
import subprocess


if __name__=="__main__":
    atfile  = glob.glob("*attorb")[0]
    exfile  = glob.glob("*xpcw3po_ex.img")[0]
    hkfile  = glob.glob("*.hk")[0]
    infile  = glob.glob("*xpcw3po_cl.evt")[0]
    subprocess.run("xrtproducts infile={0:s} regionfile=src.reg bkgextract=yes bkgregionfile=bkg.reg outdir=. expofile={1:s} correctlc=no clobber=yes".format(infile, exfile), shell=True)
    subprocess.run("mv *xpcw3pobkg.pha xrtbkg.pha", shell=True)
    subprocess.run("mv *xpcw3posr.pha  xrtsrc.pha", shell=True)
    subprocess.run("mv *xpcw3posr.arf  xrtsrc.arf", shell=True)
