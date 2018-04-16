# optimize.py
# Optimize the the mode overlap integral between image intensity data from 
# a beam profiling camera and a Gaussian mode.
# Charlie J Keith 2018

from matplotlib.pyplot import imread, imshow
from mode_overlap_integral import curModeOverlap
from numpy import pi, array



if __name__ == '__main__':
    image = imread('GAH1732-04_G09_M210.bmp')
    mo_fun = curModeOverlap(image)

    initial_guess = [170, 130, 20, 12, 0]
    
    # optimize center location
    p = initial_guess
    mo_max = mo_fun(*p)
    shifts = array([[0,1,0,0,0],
                    [1,1,0,0,0],
                    [1,0,0,0,0],
                    [1,-1,0,0,0],
                    [0,-1,0,0,0],
                    [-1,-1,0,0,0],
                    [-1,0,0,0,0],
                    [-1,1,0,0,0]])
    while True:
        print('p= ' + str(p))
        mo_new = 0
        p_new = p
        for i in range(shifts.shape[0]):
            mo = mo_fun(*(p+shifts[i]))
            if mo > mo_max:
                mo_new = mo
                p_new = p+shifts[i]
        
        if mo_new > mo_max:
            mo_max = mo_new
            p = p_new
        else:
            break
    
    # optimize rotation
    shifts = array([[0,0,0,0,pi/180],
                    [0,0,0,0,-pi/180]])
    while True:
        print('p= ' + str(p))
        mo_new = 0
        p_new = p
        for i in range(shifts.shape[0]):
            mo = mo_fun(*(p+shifts[i]))
            if mo > mo_max:
                mo_new = mo
                p_new = p+shifts[i]
        
        if mo_new > mo_max:
            mo_max = mo_new
            p = p_new
        else:
            break

    # optimize width
    shifts = array([[0,0,0,0,1],
                    [0,0,0,1,1],
                    [0,0,0,1,0],
                    [0,0,0,1,-1],
                    [0,0,0,0,-1],
                    [0,0,0,-1,-1],
                    [0,0,0,-1,0],
                    [0,0,0,-1,1]])
    while True:
        print('p= ' + str(p))
        mo_new = 0
        p_new = p
        for i in range(shifts.shape[0]):
            mo = mo_fun(*(p+shifts[i]))
            if mo > mo_max:
                mo_new = mo
                p_new = p+shifts[i]
        
        if mo_new > mo_max:
            mo_max = mo_new
            p = p_new
        else:
            break
    
    print('\nFinal result:')
    print('Overlap Integral = ' + str(mo_max))
    print('Parameters = ' + str(p))
