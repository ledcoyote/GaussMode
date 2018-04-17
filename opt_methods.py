# opt_methods.py
# Optimization methods
# Charlie J Keith 2018


def hillclimb_shifts(fun,p_init,p_shifts):
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

def hillclimb_gradient(fun, p_init, inc):
    pass

