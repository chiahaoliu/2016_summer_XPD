"""
This file is meant to test the module to ensure it works
"""

from 2016_summer_XPD.roi.roi_definer import ROI
import unittest


class TestPackage(unittest.TestCase):

    def test_init(self):

        with self.assertRaises(TypeError):
            one = ROI(3, 4, 5)

    def test_update_export(self):
        one = ROI(1, 2, 3, 4)
        one.update(2, 2, 3, 4)
        self.assertEqual(one.export(), [2, 2, 3, 4])

