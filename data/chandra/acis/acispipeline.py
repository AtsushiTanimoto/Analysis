import subprocess


if __name__=="__main__":
    print("Please enter the obsid.")
    obsid = input()
    subprocess.run("chandra_repro {0:s} outdir=.".format(obsid), shell=True)