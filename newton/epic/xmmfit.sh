#!/bin/bash

#addascaspec
addascaspec epn.dat epnsrc.pha epnsrc.rsp epnbkg.pha
addascaspec mos.dat mossrc.pha mossrc.rsp mosbkg.pha

#move
mv mossrc.pha	../../../analysis/
mv mosbkg.pha	../../../analysis/
mv mossrc.rsp	../../../analysis/
mv epnsrc.pha	../../../analysis/
mv epnbkg.pha	../../../analysis/
mv epnsrc.rsp	../../../analysis/