# ArcPy
ArcPy codes for visualitation of WRF outputs using ArcMap

One is to apply a colour palette to several files

The other is to process WRF outputs (NetCDF format) 

------------------------------------

For domain 1 (54 km), that calculates rainfall from layers RAINC (convective) and RAINNC (non-convective)
For RAINC:
1) Reads file of accumulated rainfall from t=0 to t=i 
2) Reads file of accumulated rainfall from t=0 to t=i+1
3) Raster calculator (step 2 minus step 1)

For RAINNC:
4) Reads file of accumulated rainfall from t=0 to t=i 
5) Reads file of accumulated rainfall from t=0 to t=i+1
6) Raster calculator (step 5 minus step 4)

Raster calculator (step 3 plus step 6)

--------------------------------------

For domain 4 (2 km), that calculates rainfall from layer RAINNC (non-convective = convection-permitting)
1) Reads file of accumulated rainfall from t=0 to t=i 
2) Reads file of accumulated rainfall from t=0 to t=i+1
3) Raster calculator (step 2 minus step 1)

