#/bin/bash
rgsproc orders="1 2" bkgcorrect=no withmlambdacolumn=yes spectrumbinning=lambda

cp *R1*EVENLI*FIT r1_evt1.fits
cp *R2*EVENLI*FIT r2_evt1.fits

r1o1src=`ls -1 *R1*SRSPEC1*FIT`
r1o2src=`ls -1 *R1*SRSPEC2*FIT`
r2o1src=`ls -1 *R2*SRSPEC1*FIT`
r2o2src=`ls -1 *R2*SRSPEC2*FIT`

r1o1bkg=`ls -1 *R1*BGSPEC1*FIT`
r1o2bkg=`ls -1 *R1*BGSPEC2*FIT`
r2o1bkg=`ls -1 *R2*BGSPEC1*FIT`
r2o2bkg=`ls -1 *R2*BGSPEC2*FIT`

r1o1rsp=`ls -1 *R1*RSPMAT1*FIT`
r1o2rsp=`ls -1 *R1*RSPMAT2*FIT`
r2o1rsp=`ls -1 *R2*RSPMAT1*FIT`
r2o2rsp=`ls -1 *R2*RSPMAT2*FIT`

fparkey $r1o1bkg $r1o1src BACKFILE
fparkey $r1o1rsp $r1o1src RESPFILE

fparkey $r1o2bkg $r1o2src BACKFILE
fparkey $r1o2rsp $r1o2src RESPFILE

fparkey $r2o1bkg $r2o1src BACKFILE
fparkey $r2o1rsp $r2o1src RESPFILE

fparkey $r2o2bkg $r2o2src BACKFILE
fparkey $r2o2rsp $r2o2src RESPFILE

rgsrmfgen spectrumset=$r1o1src rmfset=r1_o1_rmf.fits evlist=r1_evt1.fits emin=0.4 emax=2.5 rows=4000
rgsrmfgen spectrumset=$r1o2src rmfset=r1_o2_rmf.fits evlist=r1_evt1.fits emin=0.4 emax=2.5 rows=4000
rgsrmfgen spectrumset=$r2o1src rmfset=r2_o1_rmf.fits evlist=r2_evt1.fits emin=0.4 emax=2.5 rows=4000
rgsrmfgen spectrumset=$r2o2src rmfset=r2_o2_rmf.fits evlist=r2_evt1.fits emin=0.4 emax=2.5 rows=4000

rgscombine pha="${r1o1src} ${r2o1src}" rmf='r1_o1_rmf.fits r2_o1_rmf.fits' bkg="${r1o1bkg} ${r2o1bkg}" filepha='rgs12o1src.pha' filermf='rgs12o1src.rmf' filebkg='rgs12o1bkg.fits' rmfgrid=4000
rgscombine pha="${r1o2src} ${r2o2src}" rmf='r1_o2_rmf.fits r2_o2_rmf.fits' bkg="${r1o2bkg} ${r2o2bkg}" filepha='rgs12o2src.pha' filermf='rgs12o2src.rmf' filebkg='rgs12o2bkg.fits' rmfgrid=4000

