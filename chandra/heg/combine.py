import subprocess


if __name__=="__main__":
    output = input()
    subprocess.call("combine_grating_spectra add_plusminus=yes arf=@arf.txt infile=@pha.txt out={0:s} rmf=@rmf.txt".format(output), shell=True)