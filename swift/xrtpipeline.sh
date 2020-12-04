#!/usr/bin/env bash
number=`ls ../swift`
xrtpipeline indir=../swift/$number outdir=. plotdevice="ps" srcra=OBJECT srcdec=OBJECT steminputs=sw$number stemoutputs=DEFAULT  