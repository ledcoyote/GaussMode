# mode_overlap_integral.py
# Compute the mode overlap integral between intensity image data and an 
# analytically defined Gaussian mode. Flat phasefronts are assumed, i.e. both
# the image and the analytic mode are defined at their waist.
# Ref. https://www.rp-photonics.com/mode_matching.html
# Charlie J Keith 2018

from numpy import meshgrid, exp, sqrt, zeros, sum, sin, cos

def curModeOverlap(I):
    """ Return a mode overlap integral function curried with image data """
    
    def modeOverlap(Cx, Cy, Wx, Wy, theta):
        """ Compute mode overlap integral given Gaussian beam parameters """

        X, Y = meshgrid(range(I.shape[1]),range(I.shape[0]))
        X = X-Cx # set origin
        Y = Y-Cy
        Xr = X*cos(theta) - Y*sin(theta) # apply rotation
        Yr = X*sin(theta) + Y*cos(theta)
        G = exp(-(2*Xr**2/Wx**2 + 2*Yr**2/Wy**2)) # compute Gaussian
        C = sqrt(G*I)

        mask = zeros(I.shape) # mask to within 1/e^2 (1*Wx,y) area
        mask[G >= exp(-2)] = 1

        return sum(C*mask)**2 / sum(I*mask) / sum(G*mask)

    return modeOverlap

