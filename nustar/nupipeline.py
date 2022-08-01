import subprocess


if __name__=="__main__":
    print("Please enter obsid.")
    obsid = input()
    subprocess.run("nupipeline indir=../../{0:s} outdir=. saamode=optimized steminputs=nu{0:s} tentacle=yes".format(obsid), shell=True)