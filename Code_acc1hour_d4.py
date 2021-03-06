#=============start actual code=================

import arcgisscripting, sys, string, os, arcpy
from arcpy.sa import *
import arcpy
from arcpy import env

# VARIABLES
folder = "F_Newcastle"
projekt = "NewcWRF21"
simulation = "21"
hora = 17
variablenc = "RAINNC"
variablec = "RAINC"
x_dimension = "XLONG"
y_dimension = "XLAT"
band_dimension = ""
dimension = "Time"
valueSelectionMethod = "BY_VALUE"


#==========================================================================
#==========================================================================
#                               DOMAIN 4
#==========================================================================
#==========================================================================

acc_before = hora + 12 - 1
acc_hour = hora + 12

#=============================================
#         ACUMULADO A LA HORA ANTERIOR
#=============================================

nowFileini = projekt + "_ini"
inNetCDF = r"F:/"+ folder +"/"+ projekt +"/wrfout_d04_2012-06-27_12%3A00%3A00"
nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
dimension_values = nc_FP.getDimensionValue(dimension, acc_before)
dv1 = ["Time", dimension_values]
dimension_values = [dv1]
arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variablenc, x_dimension, y_dimension, nowFileini, band_dimension, dimension_values, valueSelectionMethod)


#=============================================
#          ACUMULADO A LA HORA
#=============================================

nowFilefin = projekt + "_fin"
inNetCDF = r"F:/"+ folder +"/"+ projekt +"/wrfout_d04_2012-06-27_12%3A00%3A00"
nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
dimension_values = nc_FP.getDimensionValue(dimension, acc_hour)
dv1 = ["Time", dimension_values]
dimension_values = [dv1]
arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variablenc, x_dimension, y_dimension, nowFilefin, band_dimension, dimension_values, valueSelectionMethod)

#=============================================
#                 Accumulated
#=============================================

dom_acc = Raster(nowFilefin) - Raster(nowFileini)
dom_accout = r"F:/" + folder + "/" + projekt + "/d4_" + str(hora) + "hr_S" + simulation
dom_acc.save(dom_accout)