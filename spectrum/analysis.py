import matplotlib
import numpy
import seaborn
import statistics
import subprocess
import xspec


def PlotSpectrum(object, satelite):
    seaborn.set        ()
    seaborn.set_context("poster")

    if satelite=="Chandra" or satelite=="Swift":
        seaborn.set_palette("hls", 2)
        energy0101  = xspec.Plot.x(1)
        energy0102  = xspec.Plot.xErr(1)
        energy0201  = xspec.Plot.x(2)
        energy0202  = xspec.Plot.xErr(2)
        counts0101  = xspec.Plot.y(1)
        counts0102  = xspec.Plot.yErr(1)
        counts0201  = xspec.Plot.y(2)
        counts0202  = xspec.Plot.yErr(2)
        models0101  = xspec.Plot.model(1)
        models0201  = xspec.Plot.model(2)
        
        if satelite=="Chandra":
            fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16, 9))
            fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
            matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-06, 1.00e+02])
            matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Chandra/ACIS", linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="NuSTAR/FPM",   linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
            matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
            matplotlib.pyplot.legend    (loc="upper right")
            matplotlib.pyplot.text      (numpy.logspace(0.00, 2.00, 11)[1], numpy.logspace(-6.00, +2.00, 9)[6], object.replace("--","-"))
            matplotlib.pyplot.xlabel    ("Energy (keV)")
            matplotlib.pyplot.xscale    ("log")
            matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
            matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
            matplotlib.pyplot.yscale    ("log")
            matplotlib.pyplot.savefig   ("0001.png")
            matplotlib.pyplot.close     ()
        else:
            fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16, 9))
            fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
            matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-06, 1.00e+02])
            matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Swift/XRT",  linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="NuSTAR/FPM", linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
            matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
            matplotlib.pyplot.legend    (loc="upper right")
            matplotlib.pyplot.text      (numpy.logspace(0.00, 2.00, 11)[1], numpy.logspace(-6.00, +2.00, 9)[6], object.replace("--","-"))
            matplotlib.pyplot.xlabel    ("Energy (keV)")
            matplotlib.pyplot.xscale    ("log")
            matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
            matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
            matplotlib.pyplot.yscale    ("log")
            matplotlib.pyplot.savefig   ("0001.png")
            matplotlib.pyplot.close     ()
    else:
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
        
        if satelite=="Newton":
            fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16, 9))
            fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
            matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-06, 1.00e+02])
            matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Newton/MOS", linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="Newton/PN",  linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.errorbar  (x=energy0301, xerr=energy0302, y=counts0301, yerr=counts0302, elinewidth=2, label="NuSTAR/FPM", linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
            matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
            matplotlib.pyplot.plot      (energy0301, models0301, linewidth=2, markersize=0)
            matplotlib.pyplot.legend    (loc="upper right")
            matplotlib.pyplot.text      (numpy.logspace(0.00, 2.00, 11)[1], numpy.logspace(-6.00, +2.00, 9)[6], object.replace("--","-"))
            matplotlib.pyplot.xlabel    ("Energy (keV)")
            matplotlib.pyplot.xscale    ("log")
            matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
            matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
            matplotlib.pyplot.yscale    ("log")
            matplotlib.pyplot.savefig   ("0001.png")
            matplotlib.pyplot.close     ()
        else:
            fig         = matplotlib.pyplot.figure(dpi=200, figsize=(16, 9))
            fig.subplots_adjust         (left=0.125, bottom=0.125, right=0.95, top=0.95)
            matplotlib.pyplot.axis      ([1.00e+00, 1.00e+02, 1.00e-06, 1.00e+02])
            matplotlib.pyplot.errorbar  (x=energy0101, xerr=energy0102, y=counts0101, yerr=counts0102, elinewidth=2, label="Suzaku/BIXIS", linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.errorbar  (x=energy0201, xerr=energy0202, y=counts0201, yerr=counts0202, elinewidth=2, label="Suzaku/FIXIS", linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.errorbar  (x=energy0301, xerr=energy0302, y=counts0301, yerr=counts0302, elinewidth=2, label="NuSTAR/FPM",   linewidth=0, marker="o", markersize=4)
            matplotlib.pyplot.plot      (energy0101, models0101, linewidth=2, markersize=0)
            matplotlib.pyplot.plot      (energy0201, models0201, linewidth=2, markersize=0)
            matplotlib.pyplot.plot      (energy0301, models0301, linewidth=2, markersize=0)
            matplotlib.pyplot.legend    (loc="upper right")
            matplotlib.pyplot.text      (numpy.logspace(0.00, 2.00, 11)[1], numpy.logspace(-6.00, +2.00, 9)[6], object.replace("--","-"))
            matplotlib.pyplot.xlabel    ("Energy (keV)")
            matplotlib.pyplot.xscale    ("log")
            matplotlib.pyplot.xticks    (numpy.logspace(0.00, 2.00, 11))
            matplotlib.pyplot.ylabel    ("Count ($\mathrm{s}^{-1} \ \mathrm{keV}^{-1} \ \mathrm{cm}^{-2}$)")
            matplotlib.pyplot.yscale    ("log")
            matplotlib.pyplot.savefig   ("0001.png")
            matplotlib.pyplot.close     ()

    

def SpectralAnalysis(column, redshift, satelite, simultaneous, gaussian, apec, length):
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
        xspec.AllData.ignore("1:**-1.00  8.0-**")
        xspec.AllData.ignore("2:**-4.00 60.0-**")
    elif satelite=="Newton":
        xspec.AllData       ("1:1 mosgrp.pha")
        xspec.AllData       ("2:2 epngrp.pha")
        xspec.AllData       ("3:3 fpmgrp.pha")
        xspec.AllData.ignore("1:**-1.00  8.0-**")
        xspec.AllData.ignore("2:**-1.00 10.0-**")
        xspec.AllData.ignore("3:**-4.00 60.0-**")
    elif satelite=="Swift":
        xspec.AllData       ("1:1 xrtgrp.pha")
        xspec.AllData       ("2:2 fpmgrp.pha")
        xspec.AllData.ignore("1:**-1.00  6.0-**")
        xspec.AllData.ignore("2:**-4.00 60.0-**")
    elif satelite=="Suzaku":
        xspec.AllData       ("1:1 xibgrp.pha")
        xspec.AllData       ("2:2 xifgrp.pha")
        xspec.AllData       ("3:3 fpmgrp.pha")
        xspec.AllData.ignore("1:**-1.00  8.0-**")
        xspec.AllData.ignore("2:**-1.00 10.0-**")
        xspec.AllData.ignore("3:**-4.00 60.0-**")
    
    xspec.Model("constant*phabs*(constant*cabs*zphabs*zcutoffpl+constant*zcutoffpl+atable{/Users/tanimoto/analysis/model/xclumpy/xclumpy_v01_RC.fits}+atable{/Users/tanimoto/analysis/model/xclumpy/xclumpy_v01_RL.fits}+zgauss+apec)")
    
    if satelite=="Chandra":
        xspec.AllModels(1)(1) .values   = 1.10e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(2)(1) .values   = 1.00e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(2)(3) .values   = 1.00e+00
        xspec.AllModels(2)(3) .frozen   = True    
    elif satelite=="Newton":
        xspec.AllModels(1)(1) .values   = 1.00e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(2)(1) .values   = 0.90e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00
        xspec.AllModels(3)(3) .frozen   = True        
    elif satelite=="Swift":
        xspec.AllModels(1)(1) .values   = 1.05e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(2)(1) .values   = 1.00e+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(2)(3) .values   = 1.00e+00
        xspec.AllModels(2)(3) .frozen   = True        
    elif satelite=="Suzaku":
        xspec.AllModels(1)(1) .values   = 0.90e+00
        xspec.AllModels(1)(1) .frozen   = True
        xspec.AllModels(2)(1) .values   = 0.95+00
        xspec.AllModels(2)(1) .frozen   = True
        xspec.AllModels(3)(1) .values   = 1.00e+00
        xspec.AllModels(3)(1) .frozen   = True
        xspec.AllModels(3)(3) .values   = 1.00e+00
        xspec.AllModels(3)(3) .frozen   = True

    if simultaneous==True:
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = True
    else:
        xspec.AllModels(1)(3) .values   = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
        xspec.AllModels(1)(3) .frozen   = False
    
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
    xspec.AllModels(1)(18).values   = 8.70e+01, 1.00e-01, 3.00e+01, 3.00e+01, 8.70e+01, 8.70e+01
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
    xspec.AllChains.defBurn         = length//2
    xspec.AllChains.defLength       = length
    xspec.AllChains.defWalkers      = 10
    chain                           = xspec.Chain("0001.fits")
    chain.run()
    
    if simultaneous==True:
        if gaussian==True and apec==True:
            xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[0]
            xspec.AllModels(1)(10).values   = xspec.AllChains.best()[1]
            xspec.AllModels(1)(11).values   = xspec.AllChains.best()[2]
            xspec.AllModels(1)(16).values   = xspec.AllChains.best()[3]
            xspec.AllModels(1)(17).values   = xspec.AllChains.best()[4]
            xspec.AllModels(1)(18).values   = xspec.AllChains.best()[5]
            xspec.AllModels(1)(30).values   = xspec.AllChains.best()[6]
            xspec.AllModels(1)(33).values   = xspec.AllChains.best()[7]
            xspec.AllModels(1)(34).values   = xspec.AllChains.best()[8]
            xspec.AllModels(1)(37).values   = xspec.AllChains.best()[9]
            xspec.Fit.error("07 10 11 16 17 18 30 33 34 37")
            xspec.Plot     ("eeufspec")
            xspec.Xset.save("0001.xcm")
        elif gaussian==True and apec==False:
            xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[0]
            xspec.AllModels(1)(10).values   = xspec.AllChains.best()[1]
            xspec.AllModels(1)(11).values   = xspec.AllChains.best()[2]
            xspec.AllModels(1)(16).values   = xspec.AllChains.best()[3]
            xspec.AllModels(1)(17).values   = xspec.AllChains.best()[4]
            xspec.AllModels(1)(18).values   = xspec.AllChains.best()[5]
            xspec.AllModels(1)(30).values   = xspec.AllChains.best()[6]
            xspec.AllModels(1)(33).values   = xspec.AllChains.best()[7]            
            xspec.Fit.error("07 10 11 16 17 18 30 33")
            xspec.Plot     ("eeufspec")
            xspec.Xset.save("0001.xcm")
        elif gaussian==False and apec==True:
            xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[0]
            xspec.AllModels(1)(10).values   = xspec.AllChains.best()[1]
            xspec.AllModels(1)(11).values   = xspec.AllChains.best()[2]
            xspec.AllModels(1)(16).values   = xspec.AllChains.best()[3]
            xspec.AllModels(1)(17).values   = xspec.AllChains.best()[4]
            xspec.AllModels(1)(18).values   = xspec.AllChains.best()[5]
            xspec.AllModels(1)(34).values   = xspec.AllChains.best()[6]
            xspec.AllModels(1)(37).values   = xspec.AllChains.best()[7]
            xspec.Fit.error("07 10 11 16 17 18 34 37")
            xspec.Plot     ("eeufspec")
            xspec.Xset.save("0001.xcm")
        else:
            xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[0]
            xspec.AllModels(1)(10).values   = xspec.AllChains.best()[1]
            xspec.AllModels(1)(11).values   = xspec.AllChains.best()[2]
            xspec.AllModels(1)(16).values   = xspec.AllChains.best()[3]
            xspec.AllModels(1)(17).values   = xspec.AllChains.best()[4]
            xspec.AllModels(1)(18).values   = xspec.AllChains.best()[5]
            xspec.Fit.error("07 10 11 16 17 18")
            xspec.Plot     ("eeufspec")
            xspec.Xset.save("0001.xcm")
    else:
        if gaussian==True and apec==True:
            xspec.AllModels(1)(3) .values   = xspec.AllChains.best()[0]
            xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[1]
            xspec.AllModels(1)(10).values   = xspec.AllChains.best()[2]
            xspec.AllModels(1)(11).values   = xspec.AllChains.best()[3]
            xspec.AllModels(1)(16).values   = xspec.AllChains.best()[4]
            xspec.AllModels(1)(17).values   = xspec.AllChains.best()[5]
            xspec.AllModels(1)(18).values   = xspec.AllChains.best()[6]
            xspec.AllModels(1)(30).values   = xspec.AllChains.best()[7]
            xspec.AllModels(1)(33).values   = xspec.AllChains.best()[8]
            xspec.AllModels(1)(34).values   = xspec.AllChains.best()[9]
            xspec.AllModels(1)(37).values   = xspec.AllChains.best()[10]
            xspec.Fit.error("03 07 10 11 16 17 18 30 33 34 37")
            xspec.Plot     ("eeufspec")
            xspec.Xset.save("0001.xcm")
        elif gaussian==True and apec==False:
            xspec.AllModels(1)(3) .values   = xspec.AllChains.best()[0]
            xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[1]
            xspec.AllModels(1)(10).values   = xspec.AllChains.best()[2]
            xspec.AllModels(1)(11).values   = xspec.AllChains.best()[3]
            xspec.AllModels(1)(16).values   = xspec.AllChains.best()[4]
            xspec.AllModels(1)(17).values   = xspec.AllChains.best()[5]
            xspec.AllModels(1)(18).values   = xspec.AllChains.best()[6]
            xspec.AllModels(1)(30).values   = xspec.AllChains.best()[7]
            xspec.AllModels(1)(33).values   = xspec.AllChains.best()[8]
            xspec.Fit.error("03 07 10 11 16 17 18 30 33")
            xspec.Plot     ("eeufspec")
            xspec.Xset.save("0001.xcm")
        elif gaussian==False and apec==True:
            xspec.AllModels(1)(3) .values   = xspec.AllChains.best()[0]
            xspec.AllModels(1)(7) .values   = xspec.AllChains.best()[1]
            xspec.AllModels(1)(10).values   = xspec.AllChains.best()[2]
            xspec.AllModels(1)(11).values   = xspec.AllChains.best()[3]
            xspec.AllModels(1)(16).values   = xspec.AllChains.best()[4]
            xspec.AllModels(1)(17).values   = xspec.AllChains.best()[5]
            xspec.AllModels(1)(18).values   = xspec.AllChains.best()[6]
            xspec.AllModels(1)(34).values   = xspec.AllChains.best()[7]
            xspec.AllModels(1)(37).values   = xspec.AllChains.best()[8]            
            xspec.Fit.error("03 07 10 11 16 17 18 30 33")
            xspec.Plot     ("eeufspec")
            xspec.Xset.save("0001.xcm")
        elif gaussian==False and apec==False:
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


def WriteTable(object, satelite, simultaneous, gaussian, apec):
    import astropy.io.fits

    with astropy.io.fits.open("0001.fits") as fin:
        hydrogen    = numpy.zeros(len(fin[1].data))

        for i in range(len(fin[1].data)):
            hydrogen[i]   = 1e+02*fin[1].data[i][4]*numpy.exp(-(fin[1].data[i][6]-90)**2/fin[1].data[i][5]**2)

    with open("parameter.txt", mode="w") as fout:
        fout.write("{0:<80}".format(object)                                                                                                                                                                                                                                                                                         +"& ")
        
        if simultaneous==True:
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(3) .values[0],2))+"$ (fixed)")                                                                                                                                                                                                              +"&\n")
        else:
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(3) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(3) .values[0]-xspec.AllModels(1)(3) .error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(3) .error[1]-xspec.AllModels(1)(3) .values[0]),2))+"}$")+"&\n")
               
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(7) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(7) .values[0]-xspec.AllModels(1)(7) .error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(7) .error[1]-xspec.AllModels(1)(7) .values[0]),2))+"}$")+"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+02*xspec.AllModels(1)(10).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(10).values[0]-xspec.AllModels(1)(10).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(10).error[1]-xspec.AllModels(1)(10).values[0]),2))+"}$")+"&\n"   )
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+02*xspec.AllModels(1)(11).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(11).values[0]-xspec.AllModels(1)(11).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(11).error[1]-xspec.AllModels(1)(11).values[0]),2))+"}$")+"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e-02*xspec.AllModels(1)(4) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e-02*(1.645*statistics.stdev(hydrogen))                                ,2))+"}^{+"+"{0:0<4}".format(round(1e-02*(1.645*statistics.stdev(hydrogen))                                ,2))+"}$")+"&\n"   )
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(16).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(16).values[0]-xspec.AllModels(1)(16).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(16).error[1]-xspec.AllModels(1)(16).values[0]),2))+"}$")+"& "    )
        fout.write("{0:<78}".format("")                                                                                                                                                                                                                                                                                             +"\\\\\n")
        fout.write("{0:<80}".format("")                                                                                                                                                                                                                                                                                             +"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(17).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(17).values[0]-xspec.AllModels(1)(17).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(17).error[1]-xspec.AllModels(1)(17).values[0]),2))+"}$")+"&\n"   )
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(18).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(18).values[0]-xspec.AllModels(1)(18).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(18).error[1]-xspec.AllModels(1)(18).values[0]),2))+"}$")+"& "    )
        
        if gaussian==True:
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+04*xspec.AllModels(1)(30).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(30).values[0]-xspec.AllModels(1)(30).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(30).error[1]-xspec.AllModels(1)(30).values[0]),2))+"}$")+"&\n")
            fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+04*xspec.AllModels(1)(33).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(33).values[0]-xspec.AllModels(1)(33).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(33).error[1]-xspec.AllModels(1)(33).values[0]),2))+"}$")+"& " )
        else:
            fout.write("{0:<78}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"&\n")
            fout.write("{0:<80}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"& " )
        
        if apec==True:
            fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+04*xspec.AllModels(1)(34).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(34).values[0]-xspec.AllModels(1)(34).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(34).error[1]-xspec.AllModels(1)(34).values[0]),2))+"}$")+"&\n")
            fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+04*xspec.AllModels(1)(37).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(37).values[0]-xspec.AllModels(1)(37).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+04*(xspec.AllModels(1)(37).error[1]-xspec.AllModels(1)(37).values[0]),2))+"}$")+"& " )
        else:
            fout.write("{0:<78}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"&\n")
            fout.write("{0:<80}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"& " )
            
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(xspec.Fit.statistic/xspec.Fit.dof,2))                                                                                                                                                                                                                          + "$")+"\\\\\n")


if __name__=="__main__":
    columns         = [0.03310, 0.46400, 0.05720, 0.02470, 0.03200, 0.02000, 0.02110, 0.01720, 0.06140, 0.02850, 0.02160, 0.02240, 0.05230, 0.09670, 0.05540, 0.00831, 0.00859, 0.10300, 0.12600, 0.01170, 0.17100, 0.00979, 0.03370, 0.08470, 0.23100, 0.03340, 0.03820, 0.06930, 0.15800, 0.28200,
                       0.40700, 0.03520, 0.03860, 0.02170, 0.03760, 0.04520, 0.08100, 0.04560, 0.02980, 0.05190, 0.02340, 0.04650, 0.08160, 0.01320, 0.03030, 0.02080, 0.03940, 0.01620, 0.10800, 0.08710, 0.05400, 0.06590, 0.02840, 0.01910, 0.01790, 0.00674, 0.01420, 0.02290, 0.01220, 0.01140,
                       0.01840, 0.06590, 0.02570, 0.00850, 0.06800, 0.05340, 0.02250, 0.03090, 0.01940, 0.01710, 0.05090, 0.02040, 0.03820, 0.01200, 0.01360, 0.01900, 0.00955, 0.06320, 0.09180, 0.01880, 0.02760, 0.07610, 0.03900, 0.01890, 0.00772, 0.04150, 0.08010, 0.03200, 0.03290, 0.06340,
                       0.05180, 0.17300, 0.05820, 0.05500, 0.15900, 0.13200, 0.18700, 0.19100, 0.04770, 0.82000, 0.05830, 0.06270, 0.02520, 0.02380, 0.05770, 0.94300, 0.05730, 0.04780, 0.01290, 0.06430, 0.08710, 0.09940, 0.06280, 0.01410, 0.01390]
    objects         = ["2MASX J00091156--0036551", "2MASX J00253292+6821442",      "Mrk 0348", "2MASX J01073963-1139117",                "Mrk 0975",     "NGC 0454E",                  "IC 1657",                "NGC 0612",                "NGC 0678",       "MCG --01--05--047",          "NGC 0788",          "IC 1816",  "2MASX J02420381+0510061",                "FGC 0351",       "NGC 1142",            "PKS 0326--288", "SARS 059.33488-30.34397",                    "3C 105", "2MASX J04234080+0408017", "2MASX J04332716--5843346",     "UGC 03157", "2MASX J04500193--5512404",    "ESO 553--G043",        "MCG --02--15--004",          "IRAS 05581+0006",           "ESO 426--G002", "ESO 121--IG028",        "VII Zw 073", "2MASX J06411806+3249313", "2MASX J07262635--3554214",
                       "2MASX J07394469--3143024",              "UGC 03995A",      "Mrk 1210",        "MCG +02--21--013",           "CGCG 031--072",   "Fairall 272", "2MASX J08301655--6725289",               "4C +29.30", "2MASX J08434495+3549421",        "MCG +11--11--032",          "NGC 2655",         "Mrk 0018", "2MASX J09034285--7414170", "2MASX J09112999+4528060",  "CGCG 312--012",               "VII Zw 292",                "NGC 3081",                    "3C 234",           "ESO 263--G013",            "ESO 374--G044", "ESO 317--G038",                 "NGC 3281", "MCG +12--10--067",                 "Mrk 0417",  "2MASX J10523297+1036205",           "CGCG 291--028",       "NGC 3588", "MCG --01--30--041",                 "IC 0751",            "CGCG 187--022",
                                        "Was 49b",          "ESO 505--IG030",      "NGC 4388",                "NGC 4500",                "NGC 4507", "ESO 506--G027",                 "NGC 4941",                "NGC 4939",                "NGC 4992",          "NGC 5100 NED02", "MCG --03--34--064",     "PKS 1329-049",            "ESO 383--G018",                "Mrk 0268",       "NGC 5283", "SDSS J135329.05+132757.2",                "Mrk 0477", "WISE J144850.99--400845.6",                "IC 4518A",                 "NGC 5899", "CGCG 319--007", "2MASX J16052330--7253565",    "CGCG 367--009",                 "Mrk 1498",  "2MASX J16303265+3923031", "2MASX J16531506+2349431",       "NGC 6300",     "CGCG 300--062", "2MASX J18212680+5955209",                  "IC 4709",
                                     "VII Zw 800", "2MASX J18305065+0928414", "ESO 103--G035",           "ESO 231--G026", "2MASX J19301380+3410495",        "3C 403",                 "Cygnus A", "2MASX J20063331+5620364",            "PKS 2014--55", "2MASX J20214907+4400399",         "II Zw 083", "IRAS 20247--7542",            "ESO 234--G050",          "ESO 234--IG063",        "IC 5063",                "4C +50.55", "2MASX J21561518+1722525",                    "3C 445",           "ESO 533--G050",                 "NGC 7319",        "3C 452",                "UGC 12282",        "UGC 12741", "2MASX J23444387--4243124",            "PKS 2356--61"]
    redshifts       = [0.07333, 0.01165, 0.01503, 0.04746, 0.04963, 0.01213, 0.01195, 0.02977, 0.00946, 0.01669, 0.01360, 0.01695, 0.06120, 0.05185, 0.02885, 0.10877, 0.09727, 0.10308, 0.04610, 0.10230, 0.01541, 0.03306, 0.02776, 0.02897, 0.11470, 0.02243, 0.04052, 0.04133, 0.08245, 0.02940,
                       0.02569, 0.01580, 0.01350, 0.03443, 0.03305, 0.02182, 0.03476, 0.06484, 0.05397, 0.03621, 0.00467, 0.01113, 0.09102, 0.02683, 0.02563, 0.05810, 0.00798, 0.18490, 0.03354, 0.02845, 0.01515, 0.01067, 0.03358, 0.03276, 0.08787, 0.04756, 0.02685, 0.01882, 0.03150, 0.02488,
                       0.06353, 0.03971, 0.00842, 0.01038, 0.01180, 0.02502, 0.00372, 0.01038, 0.02515, 0.03194, 0.01654, 2.15000, 0.01241, 0.04035, 0.01014, 0.06332, 0.03689, 0.12300, 0.01626, 0.00864, 0.04400, 0.05151, 0.02392, 0.05470, 0.03046, 0.10344, 0.00370, 0.04202, 0.09769, 0.01690, 
                       0.00200, 0.01947, 0.01329, 0.06254, 0.06290, 0.05900, 0.05607, 0.06495, 0.06063, 0.01700, 0.02914, 0.11430, 0.00877, 0.05375, 0.01135, 0.02000, 0.07874, 0.05588, 0.02644, 0.02251, 0.08100, 0.01699, 0.01743, 0.59732, 0.09631]
    satelites       = [ "Swift", "Chandra",  "Suzaku",   "Swift", "Chandra", "Chandra", "Chandra", "Suzaku", "Chandra",  "Suzaku", "Suzaku", "Chandra",  "Newton",  "Swift",  "Suzaku",  "Suzaku",  "Swift", "Suzaku", "Chandra",   "Swift",  "Swift",  "Swift",  "Swift",  "Swift",  "Swift",  "Newton",   "Swift", "Newton", "Chandra", "Newton",
                       "Newton", "Chandra",  "Suzaku", "Chandra", "Chandra",  "Newton",   "Swift", "Newton", "Chandra",   "Swift", "Suzaku",  "Suzaku",   "Swift", "Suzaku",   "Swift",  "Suzaku", "Newton", "Newton",  "Suzaku",   "Swift",  "Swift", "Suzaku",  "Swift", "Suzaku", "Newton", "Chandra", "Chandra",  "Swift",  "Newton",  "Swift",
                      "Chandra",   "Swift",  "Newton", "Chandra",  "Suzaku",  "Suzaku",  "Suzaku", "Newton",  "Suzaku",   "Swift", "Newton",   "Swift",  "Newton", "Newton", "Chandra", "Chandra", "Newton", "Newton",  "Suzaku", "Chandra",  "Swift",  "Swift",  "Swift", "Suzaku", "Suzaku",  "Newton",  "Suzaku",  "Swift",   "Swift",  "Swift",
                       "Newton", "Chandra",  "Suzaku",   "Swift",  "Newton",  "Suzaku",  "Suzaku",  "Swift", "Chandra", "Chandra",  "Swift",   "Swift", "Chandra",  "Swift",  "Suzaku",  "Suzaku",  "Swift", "Suzaku", "Chandra",  "Newton", "Suzaku",  "Swift", "Suzaku", "Suzaku", "Suzaku"] 
    
    index           = 1
    column          = columns[index-1]
    object          = objects[index-1]
    redshift        = redshifts[index-1]
    satelite        = satelites[index-1]
    simultaneous    = False
    gaussian        = False
    apec            = False
    length          = 50000
    
    SpectralAnalysis(column, redshift, satelite, simultaneous, gaussian, apec, length)
    PlotSpectrum(object, satelite)
    WriteTable(object, satelite, simultaneous, gaussian, apec)