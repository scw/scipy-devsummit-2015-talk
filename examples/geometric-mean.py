import arcpy
import scipy.stats

raster_path = 'data/input_raster.tif'
raster_as_numpy_array = arcpy.RasterToNumPyArray(raster_path, "", "", "", 0)

# can't take a log of negative numbers, invert the depths to elevtions
raster_as_numpy_array *= -1
raster_as_numpy_array += 0.00001

raster_geometric_mean = scipy.stats.mstats.gmean(
    raster_as_numpy_array, axis=None)

print("Raster geometric mean: {}".format(raster_geometric_mean))
