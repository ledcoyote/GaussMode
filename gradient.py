# gradient.py
# compute the gradient of a function w.r.t. a given point and increments (that
# is, the sizes and signs of the differentials dp1, dp2, ...)
# Charlie J Keith 2018

from numpy import zeros
from inspect import signature

def grad(f, p0, inc):
    """ Compute the gradient of f about p0.
    
    p0 and inc must be lists of length equal to the arity of f.
    """

    arity = len(signature(f).parameters)

    if (len(p0) != arity) or (len(inc) != arity):
        raise ValueError('incorrect length of p0 or inc')

    f0 = f(*p0)
    
    g = zeros(len(inc))
    for i in range(len(inc)):
        p = list(p0)
        p[i] = p[i] + inc[i]
        g[i] = f(*p) - f0

    return g

