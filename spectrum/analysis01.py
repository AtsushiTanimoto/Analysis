import matplotlib
import seaborn
import subprocess
import xspec


if __name__=="__main__":
    subprocess.run("rm 01.fits", shell=True)
    subprocess.run("rm 01.xcm" , shell=True)

    xspec.Fit .query  = "yes"
    xspec.Plot.device = "/xs"
    xspec.Plot.xAxis  = "keV"
    xspec.Xset.abund  = "angr"
    xspec.Xset.cosmo  = "70.0, 0.00, 0.70"
    xspec.Xset.xsect  = "vern"
    
    xspec.AllData       ("1:1 acsgrp.pha")
    xspec.AllData       ("2:2 fpmgrp.pha")
    xspec.AllData       ("3:3 batgrp.pha")
    xspec.AllData.ignore("1:**-0.50   8.0-**")
    xspec.AllData.ignore("2:**-8.00  20.0-**")
    xspec.AllData.ignore("3:        100.0-**")
    
    xspec.Model("constant*phabs*(constant*cabs*zphabs*zcutoffpl+constant*zcutoffpl+atable{/Users/tanimoto/analysis/model/xclumpy/xclumpy_v01_RC.fits}+atable{/Users/tanimoto/analysis/model/xclumpy/xclumpy_v01_RL.fits}+zgauss+apec)")
    xspec.AllModels(1)(1) .values = 1.10e+00
    xspec.AllModels(1)(1) .frozen = True
    xspec.AllModels(1)(2) .values = 0.464000
    xspec.AllModels(1)(2) .frozen = True
    xspec.AllModels(1)(3) .values = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
    xspec.AllModels(1)(3) .frozen = False
    xspec.AllModels(1)(6) .values = 0.011650
    xspec.AllModels(1)(6) .frozen = True
    xspec.AllModels(1)(7) .values = 2.00e+00, 1.00e-02, 1.00e+00, 1.00e+00, 3.00e+00, 3.00e+00
    xspec.AllModels(1)(7) .frozen = False
    xspec.AllModels(1)(8) .values = 3.70e+02
    xspec.AllModels(1)(8) .frozen = True
    xspec.AllModels(1)(9) .values = 0.011650
    xspec.AllModels(1)(9) .frozen = True
    xspec.AllModels(1)(10).values = 1.00e-04
    xspec.AllModels(1)(10).frozen = False
    xspec.AllModels(1)(11).values = 1.00e-02, 1.00e-04, 0.00e+00, 0.00e+00, 1.00e+00, 1.00e+00
    xspec.AllModels(1)(11).frozen = False
    xspec.AllModels(1)(16).values = 1.00e-01, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
    xspec.AllModels(1)(16).frozen = False
    xspec.AllModels(1)(17).values = 1.00e+01, 1.00e-01, 1.00e+01, 1.00e+01, 9.00e+01, 9.00e+01
    xspec.AllModels(1)(17).frozen = False
    xspec.AllModels(1)(18).values = 3.00e+01, 1.00e-01, 3.00e+01, 3.00e+01, 8.70e+01, 8.70e+01
    xspec.AllModels(1)(18).frozen = False
    xspec.AllModels(1)(30).values = 6.40e+00
    xspec.AllModels(1)(30).frozen = True
    xspec.AllModels(1)(31).values = 0.00e+00
    xspec.AllModels(1)(31).frozen = True
    xspec.AllModels(1)(32).values = 0.011650
    xspec.AllModels(1)(32).frozen = True
    xspec.AllModels(1)(33).values = 0.00e+00
    xspec.AllModels(1)(33).frozen = True
    xspec.AllModels(1)(34).values = 1.00e+00
    xspec.AllModels(1)(34).frozen = True
    xspec.AllModels(1)(35).values = 1.00e+00
    xspec.AllModels(1)(35).frozen = True
    xspec.AllModels(1)(36).values = 0.011650
    xspec.AllModels(1)(36).frozen = True
    xspec.AllModels(1)(37).values = 0.00e+00
    xspec.AllModels(1)(37).frozen = True
    xspec.AllModels(2)(1) .values = 1.00e+00
    xspec.AllModels(2)(1) .frozen = True
    xspec.AllModels(2)(3) .values = 1.00e+00, 1.00e-02, 1.00e-01, 1.00e-01, 1.00e+01, 1.00e+01
    xspec.AllModels(2)(3) .frozen = False
    xspec.AllModels(3)(1) .values = 1.00e+00
    xspec.AllModels(3)(1) .frozen = True
    xspec.AllModels(3)(3) .values = 1.00e+00
    xspec.AllModels(3)(3) .frozen = True
    xspec.AllModels(1)(4) .link   = "100.0*p16*exp(-(p18-90.0)**2.0/p17**2.0)"
    xspec.AllModels(1)(5) .link   = "p04"
    xspec.AllModels(1)(12).link   = "p07"
    xspec.AllModels(1)(13).link   = "p08"
    xspec.AllModels(1)(14).link   = "p09"
    xspec.AllModels(1)(15).link   = "p10"
    xspec.AllModels(1)(19).link   = "p07"
    xspec.AllModels(1)(20).link   = "p08"
    xspec.AllModels(1)(21).link   = "p09"
    xspec.AllModels(1)(22).link   = "p10"
    xspec.AllModels(1)(23).link   = "p16"
    xspec.AllModels(1)(24).link   = "p17"
    xspec.AllModels(1)(25).link   = "p18"
    xspec.AllModels(1)(26).link   = "p19"
    xspec.AllModels(1)(27).link   = "p20"
    xspec.AllModels(1)(28).link   = "p21"
    xspec.AllModels(1)(29).link   = "p22"

    xspec.Fit.perform()
    xspec.Fit.steppar("17 10 90 80")
    xspec.AllChains.defBurn       = 5000
    xspec.AllChains.defLength     = 50000
    chain                         = xspec.Chain("01.fits")
    chain.run()

    xspec.AllModels(1)(3) .values = xspec.AllChains.best()[0]
    xspec.AllModels(1)(7) .values = xspec.AllChains.best()[1]
    xspec.AllModels(1)(10).values = xspec.AllChains.best()[2]
    xspec.AllModels(1)(11).values = xspec.AllChains.best()[3]
    xspec.AllModels(1)(16).values = xspec.AllChains.best()[4]
    xspec.AllModels(1)(17).values = xspec.AllChains.best()[5]
    xspec.AllModels(1)(18).values = xspec.AllChains.best()[6]
    xspec.AllModels(2)(3) .values = xspec.AllChains.best()[7]
    
    xspec.Fit.error("03 07 10 11 16 17 18 40")
    xspec.Plot     ("ldata delchi")
    xspec.Xset.save("01.xcm")

    with open("parameter.txt", mode="w") as fout:
        fout.write("{0:<80}".format("2MASX J00253292+6821442")                                                                                                                                                                                                                                                                      +"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(3) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(3) .values[0]-xspec.AllModels(1)(3) .error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(3) .error[1]-xspec.AllModels(1)(3) .values[0]),2))+"}$")+"&\n"   )
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(2)(3) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(2)(3) .values[0]-xspec.AllModels(2)(3) .error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(2)(3) .error[1]-xspec.AllModels(2)(3) .values[0]),2))+"}$")+"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(7) .values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(7) .values[0]-xspec.AllModels(1)(7) .error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(7) .error[1]-xspec.AllModels(1)(7) .values[0]),2))+"}$")+"&\n"   )
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+02*xspec.AllModels(1)(10).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(10).values[0]-xspec.AllModels(1)(10).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(10).error[1]-xspec.AllModels(1)(10).values[0]),2))+"}$")+"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+02*xspec.AllModels(1)(11).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(11).values[0]-xspec.AllModels(1)(11).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+02*(xspec.AllModels(1)(11).error[1]-xspec.AllModels(1)(11).values[0]),2))+"}$")+"&\n"   )
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e-02*xspec.AllModels(1)(4) .values[0],2))+"$")                                                                                                                                                                                                                      +"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(16).values[0],2))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(16).values[0]-xspec.AllModels(1)(16).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(16).error[1]-xspec.AllModels(1)(16).values[0]),2))+"}$")+"\\\\\n")
        fout.write("{0:<80}".format("")                                                                                                                                                                                                                                                                                             +"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(17).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(17).values[0]-xspec.AllModels(1)(17).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(17).error[1]-xspec.AllModels(1)(17).values[0]),2))+"}$")+"&\n"   )
        fout.write("{0:<80}".format("$"+"{0:0<4}".format(round(1e+00*xspec.AllModels(1)(18).values[0],1))+"_{-"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(18).values[0]-xspec.AllModels(1)(18).error[0]),2))+"}^{+"+"{0:0<4}".format(round(1e+00*(xspec.AllModels(1)(18).error[1]-xspec.AllModels(1)(18).values[0]),2))+"}$")+"& "    )
        fout.write("{0:<78}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"&\n"   )
        fout.write("{0:<80}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"& "    )
        fout.write("{0:<78}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"&\n"   )
        fout.write("{0:<80}".format("\\nodata")                                                                                                                                                                                                                                                                                     +"& "    )
        fout.write("{0:<78}".format("$"+"{0:0<4}".format(round(xspec.Fit.statistic/xspec.Fit.dof,2))                                                                                                                                                                                                                          + "$")+"\\\\\n")