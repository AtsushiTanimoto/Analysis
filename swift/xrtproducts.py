import glob
import subprocess


if __name__=="__main__":
    infile  = glob.glob("*xpcw3po_cl.evt")
    exfile  = glob.glob("*xpcw3po_ex.img")
    subprocess.run("xrtprodcuts infile={0:s} regionfile=src.reg bkgextract=yes bkgregionfile=bkg.reg outdir=. expofile={1:s}".format(infile, exfile), shell=True)
    subprocess.run("mv *xpcw3pobkg.pha xrtbkg.pha", shell=True)
    subprocess.run("mv *xpcw3posr.pha  xrtsrc.pha", shell=True)
    subprocess.run("mv *xpcw3posr.arf  xrtsrc.arf", shell=True)
