#!/bin/bash
number=`ls ../../`
nupipeline indir=../../$number outdir=. saamode=optimized steminputs=nu$number tentacle=yes
