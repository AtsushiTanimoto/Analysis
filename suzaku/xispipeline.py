import subprocess


if __name__=="__main__":
    print("Please enter observation identification number.")
    obsid = input()
    subprocess.run("aepipeline clobber=yes entry_stage=1 exit_stage=2 indir=../suzaku/{0:s} instrument=XIS outdir=. steminputs=ae{0:s}".format(obsid), shell=True)