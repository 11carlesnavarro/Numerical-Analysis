import numpy as np

def order(pn, raiz):
    """
    Compute the logarithm of the e(n) and e(n+1) errors of a functional iteration method.
    :param pn: value of the approximation p at iteration n
    :param raiz: true value at which the succession converges
    
    :returns (e(n), e(n+1)): a tuple with the lists of log of errors
    """
    
    e = abs(pn - raiz)   
    return np.log(e[:-2]), np.log(e[1:-1])