import subprocess


if __name__=="__main__":
    print("Please enter obsid.")
    obsid = input()
    subprocess.run("nuproducts indir=. outdir=. instrument=FPMA steminputs=nu{0:s} bkgextract=yes bkgregionfile=bkg.reg srcregionfile=src.reg".format(obsid), shell=True)
    subprocess.run("nuproducts indir=. outdir=. instrument=FPMB steminputs=nu{0:s} bkgextract=yes bkgregionfile=bkg.reg srcregionfile=src.reg".format(obsid), shell=True)
    subprocess.run("mv nu*A01_bk.pha fpmabkg.pha", shell=True)
    subprocess.run("mv nu*A01_sr.arf fpmasrc.arf", shell=True)
    subprocess.run("mv nu*A01_sr.pha fpmasrc.pha", shell=True)
    subprocess.run("mv nu*A01_sr.rmf fpmasrc.rmf", shell=True)
    subprocess.run("mv nu*B01_bk.pha fpmbbkg.pha", shell=True)
    subprocess.run("mv nu*B01_sr.arf fpmbsrc.arf", shell=True)
    subprocess.run("mv nu*B01_sr.pha fpmbsrc.pha", shell=True)
    subprocess.run("mv nu*B01_sr.rmf fpmbsrc.rmf", shell=True)