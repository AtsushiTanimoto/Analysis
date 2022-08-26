import glob
import subprocess


if __name__=="__main__":
    fin = glob.glob("*evt2.fits")[0]
    subprocess.run("specextract infile='{0:s}[sky=region(src.reg)]' outroot=acs bkgfile='{0:s}[sky=region(bkg.reg)]'".format(fin), shell=True)
    subprocess.run("mv acs_bkg.pi acsbkg.pha", shell=True)
    subprocess.run("mv acs.arf    acssrc.arf", shell=True)
    subprocess.run("mv acs.pi     acssrc.pha", shell=True)
    subprocess.run("mv acs.rmf    acssrc.rmf", shell=True)
    subprocess.run("rm acs_bkg.arf", shell=True)
    subprocess.run("rm acs_bkg.rmf", shell=True)
    subprocess.run("rm acs_grp.pi", shell=True)