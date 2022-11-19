import matplotlib
import numpy
import seaborn
import statistics
import subprocess
import xspec


def PlotSpectrum(satelite):
    seaborn.set        ()
    seaborn.set_context("poster")

    if satelite=="Chandra":
        seaborn.set_palette("hls", 3)
        energy0101  = xspec.Plot.x(1)
        energy0102  = xspec.Plot.xErr(1)
        energy0201  = xspec.Plot.x(2)
        energy0202  = xspec.Plot.xErr(2)
        energy0301  = xspec.Plot.x(3)
        energy0302  = xspec.Plot.xErr(3)
        counts0101  = xspec.Plot.y(1)
        counts0102  = xspec.Plot.yErr(1)
        counts0201  = xspec.Plot.y(2)
        counts0202  = xspec.Plot.yErr(2)
        counts0301  = xspec.Plot.y(3)
        counts0302  = xspec.Plot.yErr(3)
        models0101  = xspec.Plot.model(1)
        models0201  = xspec.Plot.model(2)
        models0301  = xspec.Plot.model(3)
        fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16,9))
        fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
        matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-08, 1.00e+00])
        matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Chandra/ACIS", linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="NuSTAR/FPM",   linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0301, xerr=energy0302, y=counts0301, yerr=counts0302, elinewidth=2, label="Swift/BAT",    linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0301, models0301, linewidth=2, markersize=0)
        matplotlib.pyplot.legend    (loc="upper right")
        matplotlib.pyplot.xlabel    ("Energy (keV)")
        matplotlib.pyplot.xscale    ("log")
        matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
        matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
        matplotlib.pyplot.yscale    ("log")
        matplotlib.pyplot.savefig   ("0001.pdf")
        matplotlib.pyplot.close     ()
    elif satelite=="Newton":
        seaborn.set_palette("hls", 4)
        energy0101  = xspec.Plot.x(1)
        energy0102  = xspec.Plot.xErr(1)
        energy0201  = xspec.Plot.x(2)
        energy0202  = xspec.Plot.xErr(2)
        energy0301  = xspec.Plot.x(3)
        energy0302  = xspec.Plot.xErr(3)
        energy0401  = xspec.Plot.x(4)
        energy0402  = xspec.Plot.xErr(4)
        counts0101  = xspec.Plot.y(1)
        counts0102  = xspec.Plot.yErr(1)
        counts0201  = xspec.Plot.y(2)
        counts0202  = xspec.Plot.yErr(2)
        counts0301  = xspec.Plot.y(3)
        counts0302  = xspec.Plot.yErr(3)
        counts0401  = xspec.Plot.y(4)
        counts0402  = xspec.Plot.yErr(4)
        models0101  = xspec.Plot.model(1)
        models0201  = xspec.Plot.model(2)
        models0301  = xspec.Plot.model(3)
        models0401  = xspec.Plot.model(4)
        fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16,9))
        fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
        matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-08, 1.00e+00])
        matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Newton/MOS", linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="Newton/PN",  linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0301, xerr=energy0302, y=counts0301, yerr=counts0302, elinewidth=2, label="NuSTAR/FPM", linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0401, xerr=energy0402, y=counts0401, yerr=counts0402, elinewidth=2, label="Swift/BAT",  linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0301, models0301, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0401, models0401, linewidth=2, markersize=0)
        matplotlib.pyplot.legend    (loc="upper right")
        matplotlib.pyplot.xlabel    ("Energy (keV)")
        matplotlib.pyplot.xscale    ("log")
        matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
        matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
        matplotlib.pyplot.yscale    ("log")
        matplotlib.pyplot.savefig   ("0001.pdf")
        matplotlib.pyplot.close     ()
    elif satelite=="Swift":
        seaborn.set_palette("hls", 3)
        energy0101  = xspec.Plot.x(1)
        energy0102  = xspec.Plot.xErr(1)
        energy0201  = xspec.Plot.x(2)
        energy0202  = xspec.Plot.xErr(2)
        energy0301  = xspec.Plot.x(3)
        energy0302  = xspec.Plot.xErr(3)
        counts0101  = xspec.Plot.y(1)
        counts0102  = xspec.Plot.yErr(1)
        counts0201  = xspec.Plot.y(2)
        counts0202  = xspec.Plot.yErr(2)
        counts0301  = xspec.Plot.y(3)
        counts0302  = xspec.Plot.yErr(3)
        models0101  = xspec.Plot.model(1)
        models0201  = xspec.Plot.model(2)
        models0301  = xspec.Plot.model(3)
        fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16,9))
        fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
        matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-08, 1.00e+00])
        matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Swift/XRT",  linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="NuSTAR/FPM", linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0301, xerr=energy0302, y=counts0301, yerr=counts0302, elinewidth=2, label="Swift/BAT",  linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0301, models0301, linewidth=2, markersize=0)
        matplotlib.pyplot.legend    (loc="upper right")
        matplotlib.pyplot.xlabel    ("Energy (keV)")
        matplotlib.pyplot.xscale    ("log")
        matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
        matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
        matplotlib.pyplot.yscale    ("log")
        matplotlib.pyplot.savefig   ("0001.pdf")
        matplotlib.pyplot.close     ()
    elif satelite=="Suzaku":
        seaborn.set_palette("hls", 4)
        energy0101  = xspec.Plot.x(1)
        energy0102  = xspec.Plot.xErr(1)
        energy0201  = xspec.Plot.x(2)
        energy0202  = xspec.Plot.xErr(2)
        energy0301  = xspec.Plot.x(3)
        energy0302  = xspec.Plot.xErr(3)
        energy0401  = xspec.Plot.x(4)
        energy0402  = xspec.Plot.xErr(4)
        counts0101  = xspec.Plot.y(1)
        counts0102  = xspec.Plot.yErr(1)
        counts0201  = xspec.Plot.y(2)
        counts0202  = xspec.Plot.yErr(2)
        counts0301  = xspec.Plot.y(3)
        counts0302  = xspec.Plot.yErr(3)
        counts0401  = xspec.Plot.y(4)
        counts0402  = xspec.Plot.yErr(4)
        models0101  = xspec.Plot.model(1)
        models0201  = xspec.Plot.model(2)
        models0301  = xspec.Plot.model(3)
        models0401  = xspec.Plot.model(4)
        fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16,9))
        fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
        matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-08, 1.00e+00])
        matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Suzaku/BIXIS", linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="Suzaku/FIXIS", linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0301, xerr=energy0302, y=counts0301, yerr=counts0302, elinewidth=2, label="NuSTAR/FPM",   linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.errorbar  (x=energy0401, xerr=energy0402, y=counts0401, yerr=counts0402, elinewidth=2, label="Swift/BAT",    linewidth=0, marker="o", markersize=4)
        matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0301, models0301, linewidth=2, markersize=0)
        matplotlib.pyplot.plot      (energy0401, models0401, linewidth=2, markersize=0)
        matplotlib.pyplot.legend    (loc="upper right")
        matplotlib.pyplot.xlabel    ("Energy (keV)")
        matplotlib.pyplot.xscale    ("log")
        matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
        matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
        matplotlib.pyplot.yscale    ("log")
        matplotlib.pyplot.savefig   ("0001.pdf")
        matplotlib.pyplot.close     ()


def SpectralAnalysis(column, redshift, satelite, simultaneous, gaussian, apec):
    subprocess.run("rm 0001.fits", shell=True)
    subprocess.run("rm 0001.xcm" , shell=True)

    xspec.Fit.query         = "yes"
    xspec.Fit.statMethod    = "chi"
    xspec.Plot.area         = True
    xspec.Plot.xAxis        = "keV"
    xspec.Xset.abund        = "angr"
    xspec.Xset.cosmo        = "70.0, 0.00, 0.70"
    xspec.Xset.xsect        = "vern"

    if satelite=="Chandra":
        xspec.AllData       ("1:1 acsgrp.pha")
        xspec.AllData       ("2:2 fpmgrp.pha")
        xspec.AllData       ("3:3 batgrp.pha")
        xspec.AllData.ignore("1:**-1.00   8.0-**")
        xspec.AllData.ignore("2:**-8.00  25.0-**")
        xspec.AllData.ignore("3:        100.0-**")
    elif satelite=="Newton":
        xspec.AllData       ("1:1 mosgrp.pha")
        xspec.AllData       ("2:2 epngrp.pha")
        xspec.AllData       ("3:3 fpmgrp.pha")
        xspec.AllData       ("4:4 batgrp.pha")
        xspec.AllData.ignore("1:**-0.50   8.0-**")
        xspec.AllData.ignore("2:**-0.50  10.0-**")
        xspec.AllData.ignore("3:**-8.00  60.0-**")
        xspec.AllData.ignore("4:        100.0-**")
    elif satelite=="Swift":
        xspec.AllData       ("1:1 xrtgrp.pha")
        xspec.AllData       ("2:2 fpmgrp.pha")
        xspec.AllData       ("3:3 batgrp.pha")
        xspec.AllData.ignore("1:**-1.00   6.0-**")
        xspec.AllData.ignore("2:**-4.00  30.0-**")
        xspec.AllData.ignore("3:        100.0-**")
    elif satelite=="Suzaku":
        xspec.AllData       ("1:1 xibgrp.pha")
        xspec.AllData       ("2:2 xifgrp.pha")
        xspec.AllData       ("3:3 fpmgrp.pha")
        xspec.AllData       ("4:4 batgrp.pha")
        xspec.AllData.ignore("1:**-0.50   8.0-**")
        xspec.AllData.ignore("2:**-0.50  10.0-**")
        xspec.AllData.ignore("3:**-8.00  60.0-**")
        xspec.AllData.ignore("4:        100.0-**")
    
    xspec.Model("constant*phabs*(constant*cabs*zphabs*zcutoffpl+constant*zcutoffpl+atable{/Users/tanimoto/analysis/model/xclumpy/xclumpy_v01_RC.fits}+atable{/Users/tanimoto/analysis/model/xclumpy/xclumpy_v01_RL.fits}+zgauss+apec)")
    
    if satelite=="Chandra" and simultaneous==True:
        xspec.AllModels(1)(1) .values   = 1.10e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 1.00e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00
        xspec.AllModels(3)(3) .frozen   = True
    elif satelite=="Chandra" and simultaneous==False:
        xspec.AllModels(1)(1) .values   = 1.10e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 1.00e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(2)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(2)(3) .frozen   = False
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00
        xspec.AllModels(3)(3) .frozen   = True
    elif satelite=="Newton" and simultaneous==True:
        xspec.AllModels(1)(1) .values   = 1.00e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 0.90e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(4)(1) .values   = 1.00e+00
        xspec.AllModels(4)(1) .frozen   = True
        xspec.AllModels(4)(3) .values   = 1.00e+00
        xspec.AllModels(4)(3) .frozen   = True
    elif satelite=="Newton" and simultaneous==False:
        xspec.AllModels(1)(1) .values   = 1.00e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 0.90e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(3)(3) .frozen   = False
        xspec.AllModels(4)(1) .values   = 1.00e+00
        xspec.AllModels(4)(1) .frozen   = True
        xspec.AllModels(4)(3) .values   = 1.00e+00
        xspec.AllModels(4)(3) .frozen   = True
    elif satelite=="Swift" and simultaneous==True:
        xspec.AllModels(1)(1) .values   = 1.05e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 1.00e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00
        xspec.AllModels(3)(3) .frozen   = True
    elif satelite=="Swift" and simultaneous==False:
        xspec.AllModels(1)(1) .values   = 1.05e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 1.00e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(2)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(2)(3) .frozen   = False
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00
        xspec.AllModels(3)(3) .frozen   = True
    elif satelite=="Suzaku" and simultaneous==True:
        xspec.AllModels(1)(1) .values   = 0.90e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 0.95+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(4)(1) .values   = 1.00e+00
        xspec.AllModels(4)(1) .frozen   = True
        xspec.AllModels(4)(3) .values   = 1.00e+00
        xspec.AllModels(4)(3) .frozen   = True
    elif satelite=="Suzaku" and simultaneous==False:
        xspec.AllModels(1)(1) .values   = 0.90e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
        xspec.AllModels(2)(1) .values   = 0.95e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(3)(3) .frozen   = False
        xspec.AllModels(4)(1) .values   = 1.00e+00
        xspec.AllModels(4)(1) .frozen   = True
        xspec.AllModels(4)(3) .values   = 1.00e+00
        xspec.AllModels(4)(3) .frozen   = True
    
    xspec.AllModels(1)(2) .values   = column
    xspec.AllModels(1)(2) .frozen   = True
    xspec.AllModels(1)(6) .values   = redshift
    xspec.AllModels(1)(6) .frozen   = True
    xspec.AllModels(1)(7) .values   = 2.00e+00, 1.00e-02, 1.00e+00, 1.00e+00, 3.00e+00, 3.00e+00
    xspec.AllModels(1)(7) .frozen   = False
    xspec.AllModels(1)(8) .values   = 3.70e+02
    xspec.AllModels(1)(8) .frozen   = True
    xspec.AllModels(1)(9) .values   = redshift
    xspec.AllModels(1)(9) .frozen   = True
    xspec.AllModels(1)(10).values   = 1.00e-04, 1.00e-04, 1.00e-04, 1.00e-04, 1.00e+00, 1.00e+00
    xspec.AllModels(1)(10).frozen   = False
    xspec.AllModels(1)(11).values   = 1.00e-04, 1.00e-04, 1.00e-04, 1.00e-04, 1.00e+00, 1.00e+00
    xspec.AllModels(1)(11).frozen   = False
    xspec.AllModels(1)(16).values   = 1.00e-01, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
    xspec.AllModels(1)(16).frozen   = False
    xspec.AllModels(1)(17).values   = 1.00e+01, 1.00e-01, 1.00e+01, 1.00e+01, 9.00e+01, 9.00e+01
    xspec.AllModels(1)(17).frozen   = False
    xspec.AllModels(1)(18).values   = 3.00e+01, 1.00e-01, 3.00e+01, 3.00e+01, 8.70e+01, 8.70e+01
    xspec.AllModels(1)(18).frozen   = False

    if gaussian==True:
        xspec.AllModels(1)(30).values   = 6.40e+00
        xspec.AllModels(1)(30).frozen   = False
        xspec.AllModels(1)(31).values   = 0.00e+00
        xspec.AllModels(1)(31).frozen   = True
        xspec.AllModels(1)(32).values   = redshift
        xspec.AllModels(1)(32).frozen   = True
        xspec.AllModels(1)(33).values   = 1.00e-04
        xspec.AllModels(1)(33).frozen   = False
    else:
        xspec.AllModels(1)(30).values   = 6.40e+00
        xspec.AllModels(1)(30).frozen   = True
        xspec.AllModels(1)(31).values   = 0.00e+00
        xspec.AllModels(1)(31).frozen   = True
        xspec.AllModels(1)(32).values   = redshift
        xspec.AllModels(1)(32).frozen   = True
        xspec.AllModels(1)(33).values   = 0.00e+00
        xspec.AllModels(1)(33).frozen   = True

    if apec==True:
        xspec.AllModels(1)(34).values   = 1.00e+00
        xspec.AllModels(1)(34).frozen   = False
        xspec.AllModels(1)(35).values   = 1.00e+00
        xspec.AllModels(1)(35).frozen   = True
        xspec.AllModels(1)(36).values   = redshift
        xspec.AllModels(1)(36).frozen   = True
        xspec.AllModels(1)(37).values   = 1.00e-04
        xspec.AllModels(1)(37).frozen   = False
    else:
        xspec.AllModels(1)(34).values   = 1.00e+00
        xspec.AllModels(1)(34).frozen   = True
        xspec.AllModels(1)(35).values   = 1.00e+00
        xspec.AllModels(1)(35).frozen   = True
        xspec.AllModels(1)(36).values   = redshift
        xspec.AllModels(1)(36).frozen   = True
        xspec.AllModels(1)(37).values   = 0.00e+00
        xspec.AllModels(1)(37).frozen   = True

    xspec.AllModels(1)(4) .link     = "100.0*p16*exp(-(p18-90.0)**2.0/p17**2.0)"
    xspec.AllModels(1)(5) .link     = "p04"
    xspec.AllModels(1)(12).link     = "p07"
    xspec.AllModels(1)(13).link     = "p08"
    xspec.AllModels(1)(14).link     = "p09"
    xspec.AllModels(1)(15).link     = "p10"
    xspec.AllModels(1)(19).link     = "p07"
    xspec.AllModels(1)(20).link     = "p08"
    xspec.AllModels(1)(21).link     = "p09"
    xspec.AllModels(1)(22).link     = "p10"
    xspec.AllModels(1)(23).link     = "p16"
    xspec.AllModels(1)(24).link     = "p17"
    xspec.AllModels(1)(25).link     = "p18"
    xspec.AllModels(1)(26).link     = "p19"
    xspec.AllModels(1)(27).link     = "p20"
    xspec.AllModels(1)(28).link     = "p21"
    xspec.AllModels(1)(29).link     = "p22"

    xspec.Fit.perform()
    xspec.Fit.steppar("17 10 90 80")
    xspec.AllChains.defBurn         = 5000
    xspec.AllChains.defLength       = 50000
    xspec.AllChains.defWalkers      = 2
    chain                           = xspec.Chain("0001.fits")
    chain.run()

    xspec.AllModels(1)(3) .values   = xspec.AllChains.best()[0]
    xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[1]
    xspec.AllModels(1)(10).values   = xspec.AllChains.best()[2]
    xspec.AllModels(1)(11).values   = xspec.AllChains.best()[3]
    xspec.AllModels(1)(16).values   = xspec.AllChains.best()[4]
    xspec.AllModels(1)(17).values   = xspec.AllChains.best()[5]
    xspec.AllModels(1)(18).values   = xspec.AllChains.best()[6]
    
    xspec.Fit.error("03 07 10 11 16 17 18")
    xspec.Plot     ("eeufspec")
    xspec.Xset.save("0001.xcm")


def WriteTable(satelite, simutaneous, gaussian, apec):
    import astropy.io.fits

    with astropy.io.fits.open("0001.fits") as fin:
        hydrogen    = numpy.zeros(len(fin[1].data))

        for i in range(len(fin[1].data)):
            hydrogen[i]   = fin[1].data[i][4]*numpy.exp(-(fin[1].data[i][6]-90)**2/fin[1].data[i][5]**2)
    
    if satelite=="Chandra" and simultaneous==True:
        with open("parameter.txt", mode="w") as fout:
            fout.write("{0:<80}".format(object)                                                                                                                                                                                                                                                                                         +"& "    )
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(3) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(3) .values[0]-xspec.AllModels(1)(3) .error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(3) .error[1]-xspec.AllModels(1)(3) .values[0]),2))+"}$")+"&\n"   )
            fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(2)(3) .values[0],2))+"$ (linked)")                                                                                                                                                                                                             +"& "    )
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(7) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(7) .values[0]-xspec.AllModels(1)(7) .error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(7) .error[1]-xspec.AllModels(1)(7) .values[0]),2))+"}$")+"&\n"   )
            fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+02*xspec.AllModels(1)(10).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(10).values[0]-xspec.AllModels(1)(10).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(10).error[1]-xspec.AllModels(1)(10).values[0]),2))+"}$")+"& "    )
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+02*xspec.AllModels(1)(11).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(11).values[0]-xspec.AllModels(1)(11).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(11).error[1]-xspec.AllModels(1)(11).values[0]),2))+"}$")+"&\n"   )
            fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e-02*xspec.AllModels(1)(4) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e-02*(statistics.stdev(hydrogen))                                      ,2))+"}^{+"+"{0:0<4}".format(round(1e-02*(statistics.stdev(hydrogen))                                      ,2))+"}$")+"& "    )
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(16).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(16).values[0]-xspec.AllModels(1)(16).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(16).error[1]-xspec.AllModels(1)(16).values[0]),2))+"}$")+"\\\\\n")
            fout.write("{0:<80}".format("")                                                                                                                                                                                                                                                                                             +"& "    )
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(17).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(17).values[0]-xspec.AllModels(1)(17).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(17).error[1]-xspec.AllModels(1)(17).values[0]),2))+"}$")+"&\n"   )
            fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(18).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(18).values[0]-xspec.AllModels(1)(18).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(18).error[1]-xspec.AllModels(1)(18).values[0]),2))+"}$")+"& "    )
            fout.write("{0:<78}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"&\n"   )
            fout.write("{0:<80}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"& "    )
            fout.write("{0:<78}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"&\n"   )
            fout.write("{0:<80}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"& "    )
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(xspec.Fit.statistic/xspec.Fit.dof,2))                                                                                                                                                                                                                          + "$")+"\\\\\n")


if __name__=="__main__":
    columns         = [0.03310, 0.46400, 0.05720, 0.02470, 0.03200, 0.02000, 0.02110, 0.01720, 0.06140, 0.02850, 0.02160, 0.26600, 0.02240, 0.05230, 0.09670, 0.05540, 0.00831, 0.00859, 0.10300, 0.12600,
                       0.01170, 0.17100, 0.00979, 0.03370, 0.08470, 0.23100, 0.03340, 0.03820, 0.06930, 0.15800]
    objects         = ["2MASX J00091156--0036551", "2MASX J00253292+6821442", "Mrk 0348", "2MASX J01073963-1139117", "Mrk 0975", "NGC 0454E", "IC 1657", "NGC 0612", "NGC 0678", "MCG --01--05--047", "NGC 0788", "\\lbrack HB89 \\rbrack \ 0212+735", "IC 1816" , "2MASX J02420381+0510061", "FGC 0351", "NGC 1142" , "PKS 0326--288", "SARS 059.33488-30.34397", "3C 105"  , "2MASX J04234080+0408017"]
    redshifts       = [0.07333, 0.01165, 0.01503, 0.04746, 0.04963, 0.01213, 0.01195, 0.02977, 0.00946, 0.01669, 0.01360, 2.36700, 0.01695, 0.06120, 0.05185, 0.02885, 0.10877, 0.09727, 0.10308, 0.04610,
                       0.10230, 0.01541, 0.03306, 0.02776, 0.02897, 0.11470, 0.02243, 0.04052, 0.04133, 0.08245]
    
    index           = 1
    column          = columns[index]
    object          = objects[index]
    redshift        = redshifts[index]
    satelite        = "Chandra"
    simultaneous    = False
    gaussian        = False
    apec            = False
    
    SpectralAnalysis(column, redshift, satelite, simultaneous, gaussian, apec)
    PlotSpectrum(satelite)
    WriteTable(satelite, simultaneous, gaussian, apec)