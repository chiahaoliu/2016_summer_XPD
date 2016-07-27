.. current module:: 2016_summer_XPD.documentation

Documentation
=============

This documentation will provide a description of the modules
which were created to practice proper workflow techniques.

The two modules created are name ``package`` and ``not_package``.

.. code-block:: python

    from __future__ import division, absolute_import, print_function

    import os

    from matplotlib.pyplot import plot, show

    import package.Caleb
    import not_package.Hello_World

    def caleb1(a):
    	    r""" A function that tests if a number is even or odd.

	    Parameters
	    ----------
	    a: float, integer
	       This value can be any integer or float value that
	       can reasonably be computed by python. The number
	       must be of integer value however.

	     Examples
	     --------
	     >>>caleb1(1.5)
	     Please input integer value

	     >>>caleb1(1.0)
	     No, this is not an even number

	     >>>caleb1(2)
	     Yes


	     """
	     pass

    def caleb2(a):
            r"""This function takes some value and then returns it
	    after processing.

	    Parameters
	    ----------

	    a: float, integer
	       This value can be anything that the hardware can
	       compute

	    Examples
	    --------

	    >>>caleb2(3)
	    16

	    >>>caleb2(0.5)
	    26

	    """
	    pass

    def Hello_World():
            r""" This program prints out a common programming statement.

	    Parameters
	    ----------

	    None

	    Examples
	    --------

	    >>>Hello_World()
	    Hello, World!

	    """
	    pass
