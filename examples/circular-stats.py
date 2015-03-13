import arcpy
from scipy.stats import morestats

raster_path = "data/aspect_raster.tif"
r = arcpy.RasterToNumPyArray(raster_path)

# can't take a log of 0, offset values
r += 0.01

print("""Circular Mean:\t\t\t{}
Circular Std. Dev.:\t\t\t{}
Circular Variance:\t\t\t{}
""".format(
    morestats.circmean(r),
    morestats.circstd(r),
    morestats.circvar(r)))
