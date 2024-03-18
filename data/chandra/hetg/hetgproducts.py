import subprocess


if __name__=="__main__":
    print("Please enter the output filename")
    filename = input()
    subprocess.run("combine_grating_spectra add_plusminus=yes arf=@hetgarf.txt infile=@hetgpha.txt out={0:s} rmf=@hetgrmf.txt".format(filename), shell=True)