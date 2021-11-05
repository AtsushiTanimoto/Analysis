import subprocess


def main():
    print("Please enter ObsID.")
    obsid = input()
    subprocess.call("nupipeline indir=../../{0:s} outdir=. saamode=optimized steminputs=nu{0:s} tentacle=yes".format(obsid), shell=True)


if __name__="__main__":
    main()