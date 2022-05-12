import subprocess


if __name__=="__main__":
    filename = input()
    subprocess.run("combine_grating_spectra add_plusminus=yes arf=@arf.txt infile=@pha.txt out={0:s} rmf=@rmf.txt".format(filename), shell=True)