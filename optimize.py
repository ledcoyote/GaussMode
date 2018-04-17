# optimize.py
# Optimize the the mode overlap integral between image intensity data from 
# a beam profiling camera and a Gaussian mode.
# Charlie J Keith 2018

from matplotlib.pyplot import imread
from mode_overlap_integral import curModeOverlap
from numpy import pi, array
from opt_methods import hillclimb_shifts

def hc_optimize(image,p0):
    mo_fun = curModeOverlap(image)
    p = p0
    shifts = [array([[0,1,0,0,0],        # shift centers
                     [1,1,0,0,0],
                     [1,0,0,0,0],
                     [1,-1,0,0,0],
                     [0,-1,0,0,0],
                     [-1,-1,0,0,0],
                     [-1,0,0,0,0],
                     [-1,1,0,0,0]]),
              array([[0,0,0,0,pi/36],    # shift rotation angle
                     [0,0,0,0,-pi/36]]),
              array([[0,0,0,1,0],        # shift widths
                     [0,0,1,1,0],
                     [0,0,1,0,0],
                     [0,0,1,-1,0],
                     [0,0,0,-1,0],
                     [0,0,-1,-1,0],
                     [0,0,-1,0,0],
                     [0,0,-1,1,0]])]
    for i in range(len(shifts)):
        p = hillclimb_shifts(mo_fun,p,shifts[i])
    
    mo_max = mo_fun(*p)
    return mo_max, p

if __name__ == '__main__':
    image = imread('image1.bmp')

    # center of image, fairly small, 0 degree rotation
    initial_guess = [160, 128, 20, 10, 0]
    mo_max, p = hc_optimize(image, initial_guess)
    
    print('\nFinal result:')
    print('Overlap Integral = ' + str(mo_max))
    print('Parameters = ' + str(p))
