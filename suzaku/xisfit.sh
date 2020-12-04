#!/bin/bash
echo "Are there xis2 files?"
read xis


if test $xis = "yes" ; then
addascaspec xisbi.dat xibsrc.pha xibsrc.rsp xibbkg.pha
addascaspec xisf1.dat xifsrc.pha xifsrc.rsp xifbkg.pha


else
addascaspec xisbi.dat xibsrc.pha xibsrc.rsp xibbkg.pha
addascaspec xisf2.dat xifsrc.pha xifsrc.rsp xifbkg.pha
fi


mv xibsrc.rsp	../../../analysis/
mv xibbkg.pha	../../../analysis/
mv xibsrc.pha	../../../analysis/
mv xifsrc.rsp	../../../analysis/
mv xifbkg.pha	../../../analysis/
mv xifsrc.pha	../../../analysis/
