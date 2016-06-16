.. current module:: 2016_summer_XPD.documentation
Image Documentation
===================

This documentation will give a description of the processing_image function
that was created to analyze ``.tif`` files.

The name of the module is ``Analyze``. The first function that is found in this
module is ``processing_image``. The following code block will discuss how to
use this function.

.. code-block:: python

    from __future import division, absolute_import, print_function

    import os

    from tifffile import imread
    from matplotlib.pyplot import show, imshow, plot

    import Analyze

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

The second function ``analyze`` has limited functionality and acted as a
prototype ``analyze2``. It has the ability to pick a ``.tif`` file and
then provide a basic five number statistical set.

.. code-block:: python
    from __future__ import division, absolute_import, print_function

    import os

    import matplotlib.pyplot as plt

    import Analyze

    def analyze():
            r""" A function that creates a five number printout for some
	         .tif image
            Parameters
	    ----------

            none

	    Example
	    -------
	    >>>analyze()
            Please input 1, 2, or 3: 2
	    Input row to begin at: 400
	    Input row to end at: 600
	    Input column to begin at: 400
	    Input column to end at: 600

	    Number of pixels is 40000
	    Average intensity is 11334.554
	    Standard deviation is 4035.787
	    Minimum is 0.00 at 333x454
	    Maximum is 13008.08 at 595x595

            Image is displayed with calculated region marked in black lines
            
	    """
	    pass

The ``analyze2`` function is an advancement from the ``analyze`` function in
that it takes in active user input and prints out statements as required by
user. The buttons are fairly self explanatory. The statistics buttons on
the right side of the screen will print the value to the command line. The
sliders allow the user to select the region they will observe.

.. code-block:: python

     from __future__ import division, absolute_import, print_function

     import os

     import matplotlib.pyplot as plt

     import Analyze

     def analyze2():
             r""" A function that allows real time analysis of a .tif file

	     Parameters
	     ----------

	     None

	     Examples
	     --------
	     >>>analyze2()

	     Image is displayed and users inputs are used to determine user
	     needs

	     """
	     pass
