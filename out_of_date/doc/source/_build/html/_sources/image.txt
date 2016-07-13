.. current module:: 2016_summer_XPD.documentation
Image Documentation
===================

This documentation will give a description of the processing_image function
that was created to analyze ``.tif`` files.

The name of the module is ``image``. The only function that is found in this
module is ``processing_image``. The following code block will discuss how to
use this function.

.. code-block:: python

    from __future import division, absolute_import, print_function

    import os

    from tifffile import imread
    from matplotlib.pyplot import show, imshow, plot

    import Image

    def processing_image():
    	     r""" This function allows one to view diffraction patterns.

	     Parameters
	     ----------

	     none

	     Examples
	     --------
	     >>>processing_image()
	     >>>Type 1, 2, or 3
	     <1,2, or 3 here>

	     <Image Appears as .png file>

	     """
	     pass
