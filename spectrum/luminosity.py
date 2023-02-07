import numpy
import os
import xspec


if __name__=="__main__":
    masses          = [8.91, 0.00, 7.61, 0.00, 0.00, 8.52, 7.30, 8.99, 0.00, 0.00, 8.21, 0.00, 9.23, 0.00, 9.25, 0.00, 0.00, 0.00, 0.00, 8.50, 8.04, 0.00, 8.05, 0.00, 0.00, 0.00, 0.00, 7.61,
                       8.12, 0.00, 0.00, 7.81, 0.00, 8.21, 0.00, 8.14, 8.77, 8.45, 8.35, 0.00, 7.85, 0.00, 7.61, 8.17, 9.15, 8.41, 0.00, 0.00, 0.00, 7.41, 0.00, 0.00, 8.15, 9.04, 8.36, 8.24,
                       8.60, 7.75, 8.33, 0.00, 6.99, 0.00, 7.90, 8.99, 7.03, 7.52, 8.54, 8.51, 0.00, 0.00, 0.00, 8.54, 8.87, 0.00, 0.00, 0.00, 0.00, 8.66, 0.00, 0.00, 9.82, 0.00, 7.96, 8.23,
                       0.00, 0.00, 0.00, 0.00, 0.00, 8.39, 0.00, 8.81, 0.00, 9.15, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 8.11, 0.00, 0.00, 0.00, 0.00, 7.84, 0.00, 8.99, 9.80, 8.69, 0.00, 0.00]
    objects         = ["2MASX J00091156--0036551",  "2MASX J00253292+6821442",                 "Mrk 0348", "2MASX J01073963--1139117",   "Mrk 0975",                "NGC 0454E",       "IC 1657",      "NGC 0612",                "NGC 0678",       "MCG --01--05--047",                "NGC 0788",        "IC 1816", "2MASX J02420381+0510061",                 "FGC 0351",                "NGC 1142", "PKS 0326--288", "SARS 059.33488-30.34397",                   "3C 105", "2MASX J04234080+0408017",  "2MASX J04332716--5843346",     "UGC 03157", "2MASX J04500193--5512404", "ESO 553--G043",        "MCG --02--15--004", "IRAS 05581+0006",           "ESO 426--G002",           "ESO 121--IG028",              "VII Zw 073",
                        "2MASX J06411806+3249313", "2MASX J07262635--3554214", "2MASX J07394469--3143024",               "UGC 03995A",   "Mrk 1210",         "MCG +02--21--013", "CGCG 031--072",   "Fairall 272",               "4C +29.30", "2MASX J08434495+3549421",        "MCG +11--11--032",       "NGC 2655",                "Mrk 0018", "2MASX J09034285--7414170", "2MASX J09112999+4528060", "CGCG 312--012",              "VII Zw 292",                 "NGC 3081",                  "3C 234",             "ESO 263--G013", "ESO 374--G044",            "ESO 317--G038",      "NGC 3281",         "MCG +12--10--067",        "Mrk 0417", "2MASX J10523297+1036205",            "CGCG 291--028",                "NGC 3588",
                                        "IC 0751",            "CGCG 187--022",                  "Was 49b",           "ESO 505--IG030",   "NGC 4388",                 "NGC 4500",      "NGC 4507", "ESO 506--G027",                "NGC 4941",                "NGC 4939",                "NGC 4992", "NGC 5100 NED02",       "MCG --03--34--064",             "PKS 1329-049",           "ESO 383--G018",      "Mrk 0268",                "NGC 5283", "SDSS J135329.05+132757.2",                "Mrk 0477", "WISE J144850.99--400845.6",      "IC 4518A",                 "NGC 5899", "CGCG 319--007", "2MASX J16052330--7253565",   "CGCG 367--009",                "Mrk 1498",  "2MASX J16303265+3923031", "2MASX J16531506+2349431", 
                                       "NGC 6300",            "CGCG 300--062",  "2MASX J18212680+5955209",                  "IC 4709", "VII Zw 800",  "2MASX J18305065+0928414", "ESO 103--G035", "ESO 231--G026", "2MASX J19301380+3410495",                  "3C 403", "2MASX J20063331+5620364",   "PKS 2014--55", "2MASX J20214907+4400399",                "II Zw 083",        "IRAS 20247--7542", "ESO 234--G050",          "ESO 234--IG063",                  "IC 5063",               "4C +50.55",   "2MASX J21561518+1722525",        "3C 445",            "ESO 533--G050",      "NGC 7319",                   "3C 452",       "UGC 12282",               "UGC 12741",             "PKS 2356--61"]
    satelites       = [  "Swift", "Chandra",  "Suzaku",   "Swift", "Chandra", "Chandra", "Chandra",  "Suzaku", "Chandra",  "Suzaku",  "Suzaku", "Chandra",  "Newton",   "Swift",  "Suzaku",  "Suzaku",   "Swift",  "Suzaku", "Chandra",   "Swift",   "Swift",   "Swift",   "Swift",   "Swift",   "Swift",  "Newton",   "Swift",  "Newton",
                       "Chandra",  "Newton",  "Newton", "Chandra",  "Suzaku", "Chandra", "Chandra",  "Newton",  "Newton", "Chandra",   "Swift",  "Suzaku",  "Suzaku",   "Swift",  "Suzaku",   "Swift",  "Suzaku",  "Newton",  "Newton",  "Suzaku",   "Swift",   "Swift",  "Suzaku",   "Swift",  "Suzaku",  "Newton", "Chandra", "Chandra",
                        "Newton",   "Swift", "Chandra",   "Swift",  "Newton", "Chandra",  "Suzaku",  "Suzaku",  "Suzaku", "Chandra",  "Suzaku",   "Swift",  "Newton",   "Swift",  "Newton",  "Newton", "Chandra", "Chandra",  "Newton",  "Newton",  "Suzaku", "Chandra",   "Swift",   "Swift",   "Swift",  "Suzaku",  "Suzaku",  "Newton", 
                        "Suzaku",   "Swift",   "Swift",   "Swift",  "Newton", "Chandra",  "Suzaku",   "Swift",  "Newton",  "Suzaku",   "Swift", "Chandra", "Chandra",   "Swift",   "Swift", "Chandra",   "Swift",  "Suzaku",  "Suzaku",   "Swift",  "Suzaku", "Chandra",  "Newton",  "Suzaku",   "Swift",  "Suzaku",  "Suzaku",  "Suzaku"] 

    for i in range(111):
        os.chdir("/Users/tanimoto/analysis/data/0006/")
        print("{0:s}/analysis/".format(sorted(os.listdir())[i]))
        os.chdir("{0:s}/analysis/".format(sorted(os.listdir())[i]))

        if satelites[i]=="Chandra" or satelites[i]=="Swift" or i==36:
            xspec.Xset.restore      ("0001.xcm")
            xspec.AllModels.calcFlux(" 2.0 10.0")
            flux01      = round(numpy.log10(xspec.AllData(1).flux[0]), 1)
            xspec.AllModels.calcFlux("10.0 50.0")
            flux02      = round(numpy.log10(xspec.AllData(2).flux[0]), 1)
        else:
            xspec.Xset.restore      ("0001.xcm")
            xspec.AllModels.calcFlux(" 2.0 10.0")
            flux01      = round(numpy.log10(xspec.AllData(2).flux[0]), 1)
            xspec.AllModels.calcFlux("10.0 50.0")
            flux02      = round(numpy.log10(xspec.AllData(3).flux[0]), 1)

        gamma       = xspec.AllModels(1)(7) .values[0]
        cutoff      = xspec.AllModels(1)(8) .values[0]
        redshift    = xspec.AllModels(1)(9) .values[0]
        norm        = xspec.AllModels(1)(10).values[0]

        xspec.Model("zcutoffpl")
        xspec.AllModels(1)(1).values = gamma
        xspec.AllModels(1)(2).values = cutoff
        xspec.AllModels(1)(3).values = redshift
        xspec.AllModels(1)(4).values = norm

        if satelites[i]=="Chandra" or satelites[i]=="Swift" or i==36:
            xspec.AllModels.calcLumin(" 2.0 10.0 {0:.6f}".format(redshift))
            luminosity01 = round(44+numpy.log10(xspec.AllData(1).lumin[0]), 1)
            xspec.AllModels.calcLumin("10.0 50.0 {0:.6f}".format(redshift))
            luminosity02 = round(44+numpy.log10(xspec.AllData(2).lumin[0]), 1)
        else:
            xspec.AllModels.calcLumin(" 2.0 10.0 {0:.6f}".format(redshift))
            luminosity01 = round(44+numpy.log10(xspec.AllData(2).lumin[0]), 1)
            xspec.AllModels.calcLumin("10.0 50.0 {0:.6f}".format(redshift))
            luminosity02 = round(44+numpy.log10(xspec.AllData(3).lumin[0]), 1)
        
        eddington    = round(luminosity01-36.80-masses[i], 2)
        
        if masses[i]==0.00:
            with open("/Users/tanimoto/luminosity.txt", mode="a") as fout: 
                fout.write("{:<80}".format("{0:s}".format(objects[i]))          +"& "    )
                fout.write("{:<78}".format("\\nodata")                          +"&\n"   )
                fout.write("{:<80}".format("${0:0<4}$".format(flux01))          +"& "    )
                fout.write("{:<78}".format("${0:0<4}$".format(flux02))          +"&\n"   )
                fout.write("{:<80}".format("$ {0:0<4}$".format(luminosity01))   +"& "    )
                fout.write("{:<78}".format("$ {0:0<4}$".format(luminosity02))   +"&\n"   )
                fout.write("{:<80}".format("")                                  +"& "    )
                fout.write("{:<78}".format("")                                  +"\\\\\n")
        else:
            with open("/Users/tanimoto/luminosity.txt", mode="a") as fout: 
                fout.write("{:<80}".format("{0:s}".format(objects[i]))          +"& "    )
                fout.write("{:<78}".format("${0:0<4}$".format(eddington))       +"&\n"   )
                fout.write("{:<80}".format("${0:0<4}$".format(flux01))          +"& "    )
                fout.write("{:<78}".format("${0:0<4}$".format(flux02))          +"&\n"   )
                fout.write("{:<80}".format("$ {0:0<4}$".format(luminosity01))   +"& "    )
                fout.write("{:<78}".format("$ {0:0<4}$".format(luminosity02))   +"&\n"   )
                fout.write("{:<80}".format("")                                  +"& "    )
                fout.write("{:<78}".format("")                                  +"\\\\\n")
        
        os.chdir("../../")
