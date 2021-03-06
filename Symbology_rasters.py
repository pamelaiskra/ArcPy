import arcpy
mxd = arcpy.mapping.MapDocument(r"E:/E_ArcGis_Projects/my_project.mxd")
df = mxd.activeDataFrame
sourceLayer = arcpy.mapping.Layer(r"F:/Rainfall_colorscale_2.lyr")
for lyr in arcpy.mapping.ListLayers(mxd,""):
    arcpy.ApplySymbologyFromLayer_management(lyr, sourceLayer)
    lyr.visible = True
mxd.save()