# optimize.py
# Optimize the the mode overlap integral between image intensity data from 
# a beam profiling camera and a Gaussian mode.
# Charlie J Keith 2018

from traits.api import HasTraits
from threading import Thread

class GaussOptimizer:
    """ Optimizes the fit of a Gaussian mode to an intensity image """

