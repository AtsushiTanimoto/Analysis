#!/bin/sh
number=`ls ../suzaku/`
aepipeline clobber=yes entry_stage=1 exit_stage=2 indir=../suzaku/$number instrument=XIS outdir=. steminputs=ae$number
