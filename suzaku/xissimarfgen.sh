#!/bin/bash
echo "Please enter your number."
read number
if test $number = "0" ; then
sourcex=`cat src.reg | cut -sd"(" -f2 | cut -d"," -f1`
sourcey=`cat src.reg | cut -sd"," -f2 | cut -d"," -f1`
xis0att=`ls *att`
xis1att=`ls *att`
xis2att=`ls *att`
xis3att=`ls *att`
xis0gti=`ls ae*xi0_0_3*cl*`
xis1gti=`ls ae*xi1_0_3*cl*`
xis2gti=`ls ae*xi2_0_3*cl*`
xis3gti=`ls ae*xi3_0_3*cl*`
else
sourcex=`cat src.reg | cut -sd"(" -f2 | cut -d"," -f1`
sourcey=`cat src.reg | cut -sd"," -f2 | cut -d"," -f1`
xis0att=`ls *att`
xis1att=`ls *att`
xis2att=`ls *att`
xis3att=`ls *att`
xis0gti=`ls ae*xi0_1_3*cl*`
xis1gti=`ls ae*xi1_1_3*cl*`
xis2gti=`ls ae*xi2_1_3*cl*`
xis3gti=`ls ae*xi3_1_3*cl*`
fi
xissimarfgen instrume=XIS0 pointing=AUTO source_mode=SKYXY source_x=$sourcex source_y=$sourcey num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis0src.arf limit_mode=NUM_PHOTON num_photon=400000 phafile=xis0src.pha detmask=none gtifile=$xis0gti attitude=$xis0att rmffile=xis0src.rmf estepfile=default
xissimarfgen instrume=XIS1 pointing=AUTO source_mode=SKYXY source_x=$sourcex source_y=$sourcey num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis1src.arf limit_mode=NUM_PHOTON num_photon=400000 phafile=xis1src.pha detmask=none gtifile=$xis1gti attitude=$xis1att rmffile=xis1src.rmf estepfile=default
xissimarfgen instrume=XIS2 pointing=AUTO source_mode=SKYXY source_x=$sourcex source_y=$sourcey num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis2src.arf limit_mode=NUM_PHOTON num_photon=400000 phafile=xis2src.pha detmask=none gtifile=$xis2gti attitude=$xis2att rmffile=xis2src.rmf estepfile=default
xissimarfgen instrume=XIS3 pointing=AUTO source_mode=SKYXY source_x=$sourcex source_y=$sourcey num_region=1 region_mode=SKYREG regfile1=src.reg arffile1=xis3src.arf limit_mode=NUM_PHOTON num_photon=400000 phafile=xis3src.pha detmask=none gtifile=$xis3gti attitude=$xis3att rmffile=xis3src.rmf estepfile=default
