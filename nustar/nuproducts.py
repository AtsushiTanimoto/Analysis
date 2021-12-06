import subprocess


def main():
    print("Please enter obsid.")
    obsid = input()
    subprocess.call("nuproducts indir=. outdir=. instrument=FPMA steminputs=nu{0:s} bkgextract=yes bkgregionfile=bkg.reg srcregionfile=src.reg".format(obsid), shell=True)
    subprocess.call("nuproducts indir=. outdir=. instrument=FPMB steminputs=nu{0:s} bkgextract=yes bkgregionfile=bkg.reg srcregionfile=src.reg".format(obsid), shell=True)
    subprocess.call("mv nu*A01.flc    fpmasrc.flc", shell=True)
    subprocess.call("mv nu*A01_bk.lc  fpmabkg.lc" , shell=True)
    subprocess.call("mv nu*A01_bk.pha fpmabkg.pha", shell=True)
    subprocess.call("mv nu*A01_im.gif fpmaimg.gif", shell=True)
    subprocess.call("mv nu*A01_lc.gif fpmalic.gif", shell=True)
    subprocess.call("mv nu*A01_ph.fig fpmapha.gif", shell=True)
    subprocess.call("mv nu*A01_sk.img fpmasky.img", shell=True)
    subprocess.call("mv nu*A01_sr.arf fpmasrc.arf", shell=True)
    subprocess.call("mv nu*A01_sr.lc  fpmasrc.lc" , shell=True)
    subprocess.call("mv nu*A01_sr.pha fpmasrc.pha", shell=True)
    subprocess.call("mv nu*A01_sr.rmf fpmasrc.rmf", shell=True)
    subprocess.call("mv nu*B01.flc    fpmbsrc.flc", shell=True)
    subprocess.call("mv nu*B01_bk.lc  fpmbbkg.lc" , shell=True)
    subprocess.call("mv nu*B01_bk.pha fpmbbkg.pha", shell=True)
    subprocess.call("mv nu*B01_im.gif fpmbimg.gif", shell=True)
    subprocess.call("mv nu*B01_lc.gif fpmblic.gif", shell=True)
    subprocess.call("mv nu*B01_ph.fig fpmbpha.gif", shell=True)
    subprocess.call("mv nu*B01_sk.img fpmbsky.img", shell=True)
    subprocess.call("mv nu*B01_sr.arf fpmbsrc.arf", shell=True)
    subprocess.call("mv nu*B01_sr.lc  fpmbsrc.lc" , shell=True)
    subprocess.call("mv nu*B01_sr.pha fpmbsrc.pha", shell=True)
    subprocess.call("mv nu*B01_sr.rmf fpmbsrc.rmf", shell=True)


if __name__=="__main__":
    main()
