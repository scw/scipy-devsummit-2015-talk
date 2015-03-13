# A single sample test taken from:
# https://github.com/EsriOceans/btm/tree/master/tests

import arcpy
import os
import sys
import unittest

try:
    from tempdir import TempDir
    from scripts import bpi
    from scripts import utils
except:
    print("Example only, see full testing suite for operational code.")
    sys.exit()

class TestBpi(unittest.TestCase):

    def testBpiImport(self):
        """Is there a 'main' method in the bpi script?"""
        self.assertTrue('main' in vars(bpi))

    def testBpiRun(self):
        """Execute the BPI script with a raster and verify the results."""
        # set up a 'context', or a temporary environment. Here,
        # we use this to create a temporary directory that will automatically
        # be destroyed when the test is finished.
        with TempDir() as d:
            # set up our output raster and input
            input_raster = os.path.join('data', 'input_raster.tif')
            # what's the full path of our expected output BPI raster?
            output_raster = os.path.join(d, 'test_run_bpi.tif')

            # run the BPI calculation on this raster
            bpi.main(bathy=input_raster, inner_radius=10,
                     outer_radius=30, out_raster=output_raster)
            
            # our first test -- make sure the raster output exists
            #                   at the expected location
            self.assertTrue(raster_fn in os.listdir(d))

            # test -- does our raster match the mean
            #         and standard deviation we expect?
            # NOTE: AlmostEqual used here because these are floating point values
            self.assertAlmostEqual(
                utils.raster_properties(output_raster, "MEAN"), 0.295664335664)
            self.assertAlmostEqual(
                utils.raster_properties(bpi_raster, "STD"), 1.65611606614)
