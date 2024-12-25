import heasoftpy


if __name__=="__main__":
    xisrmfgen   = heasoftpy.HSPTask("xisrmfgen")
    xisrmfgen(phafile="xis0src.pha", outfile="xis0src.rmf", noprompt=True, verbose=True)
    xisrmfgen(phafile="xis1src.pha", outfile="xis1src.rmf", noprompt=True, verbose=True)
    xisrmfgen(phafile="xis2src.pha", outfile="xis2src.rmf", noprompt=True, verbose=True)
    xisrmfgen(phafile="xis3src.pha", outfile="xis3src.rmf", noprompt=True, verbose=True)