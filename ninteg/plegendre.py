import numpy as np

def plegendre(n):
    """
    Generator of Legendre polynomial coefficients of 
    degree n.
    
    Parameters:
    ----------
    n: degree of the polynomial
    
    Returns:
    --------
    c: coefficients
    """
    
    if n <= 0:
        c = np.array([1])
    elif n == 1:
        c = np.array([1,0])
    else:
        a = list(plegendre(n-1))
        a.append(0)
        a = np.array(a)
 
        c = list(plegendre(n-2))
        b = [0,0]
        b.extend(c)
        b = np.array(b)
 
        c = ((2*n-1)*a+(n-1)*b)/float(n)
 
    return c
