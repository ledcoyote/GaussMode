# optimize.py
# Optimize the the mode overlap integral between image intensity data from 
# a beam profiling camera and a Gaussian mode.
# Charlie J Keith 2018

from matplotlib.pyplot import imread
from mode_overlap_integral import curModeOverlap
from numpy import pi, array

def hillclimb(fun,p_init,p_shifts):
    """ Maximize fun, starting at p_init, iteratively over the set of
    parameter shifts in p_shifts
    """
    f_max = fun(*p_init)
    p = p_init
    while True:
        print('p= ' + str(p))
        f_new = 0
        p_new = p
        for i in range(p_shifts.shape[0]):
            f_val = fun(*(p+p_shifts[i]))
            if f_val > f_max:
                f_new = f_val
                p_new = p+p_shifts[i]
        
        if f_new > f_max:
            f_max = f_new
            p = p_new
        else:
            break
    
    return p

if __name__ == '__main__':
    image = imread('image3.bmp')
    mo_fun = curModeOverlap(image)

    # center of image, fairly small, 0 degree rotation
    initial_guess = [160, 128, 20, 10, 0]
    
    p = initial_guess
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
        p = hillclimb(mo_fun,p,shifts[i])
    
    mo_max = mo_fun(*p)
    
    print('\nFinal result:')
    print('Overlap Integral = ' + str(mo_max))
    print('Parameters = ' + str(p))
