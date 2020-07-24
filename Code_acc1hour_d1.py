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
#                               DOMAIN 1
#==========================================================================
#==========================================================================

acc_before = hora + 12 - 1
acc_hour = hora + 12

#=============================================
#         ACUMULADO A LA HORA ANTERIOR
#=============================================

#----------1) RAINNC 28 June 2012-----------------

nowFile1nc = projekt + "_d1nc15"
inNetCDF = r"F:/"+ folder +"/"+ projekt +"/wrfout_d01_2012-06-27_12%3A00%3A00"
nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
dimension_values = nc_FP.getDimensionValue(dimension, acc_before)
dv1 = ["Time", dimension_values]
dimension_values = [dv1]
arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variablenc, x_dimension, y_dimension, nowFile1nc, band_dimension, dimension_values, valueSelectionMethod)

#----------2) RAINC 15:00 28 June 2012-----------------

nowFile1c = projekt + "_d1c15"
inNetCDF = r"F:/"+ folder +"/"+ projekt +"/wrfout_d01_2012-06-27_12%3A00%3A00"
nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
dimension_values = nc_FP.getDimensionValue(dimension, acc_before)
dv1 = ["Time", dimension_values]
dimension_values = [dv1]
arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variablec, x_dimension, y_dimension, nowFile1c, band_dimension, dimension_values, valueSelectionMethod)

#---------3) SUM RAINC+RAINNC for domain 1 

# 1. Domain 1
NowFileini = Raster(nowFile1nc) + Raster(nowFile1c)


#=============================================
#         ACUMULADO A LA HORA
#=============================================

#----------1) RAINNC 28 June 2012-----------------

nowFile2nc = projekt + "_d1nc17"
inNetCDF = r"F:/"+ folder +"/"+ projekt +"/wrfout_d01_2012-06-27_12%3A00%3A00"
nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
dimension_values = nc_FP.getDimensionValue(dimension, acc_hour)
dv1 = ["Time", dimension_values]
dimension_values = [dv1]
arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variablenc, x_dimension, y_dimension, nowFile2nc, band_dimension, dimension_values, valueSelectionMethod)

#----------2) RAINC 28 June 2012-----------------

nowFile2c = projekt + "_d1c17"
inNetCDF = r"F:/"+ folder +"/"+ projekt +"/wrfout_d01_2012-06-27_12%3A00%3A00"
nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
dimension_values = nc_FP.getDimensionValue(dimension, acc_hour)
dv1 = ["Time", dimension_values]
dimension_values = [dv1]
arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variablec, x_dimension, y_dimension, nowFile2c, band_dimension, dimension_values, valueSelectionMethod)

#---------3) SUM RAINC+RAINNC for domain 1 

NowFilefin = Raster(nowFile2nc) + Raster(nowFile2c)

#=============================================
#                 Accumulated
#=============================================

dom_acc = NowFilefin - NowFileini
dom_accout = r"F:/"+ folder +"/"+ projekt +"/dom1_" + str(hora) + "hr_s" + simulation
dom_acc.save(dom_accout)