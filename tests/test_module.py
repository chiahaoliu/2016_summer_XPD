"""
This file is meant to test the module to ensure it works
"""

from roi.roi_definer import ROI
import unittest


class TestPackage(unittest.TestCase):

    def test_load(self):
        one = ROI
        self.assertRaises(AttributeError, one.load_array(3))

    def test_update_export(self):
        one = ROI(1, 2, 3, 4)
        one.update(2, 2, 3, 4)
        self.assertEqual(one.export(), [2, 2, 3, 4])
