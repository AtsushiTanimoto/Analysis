#!/bin/bash

#addascaspec
addascaspec xrt.dat xrtsrc.pha xrtsrc.rsp xrtbkg.pha

#move
mv xrtsrc.pha	../../../analysis/
mv xrtbkg.pha	../../../analysis/
mv xrtsrc.rsp	../../../analysis/