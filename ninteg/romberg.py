from trapezium import trapezium
import numpy as np

def romberg(f, a, b, p):
    '''
    Implementation of the Romberg method
    
    Parametes:
    ----------
    f: function to integrate
    a, b: integration limits
    p: number of rows of the Romberg table
    '''
    I = np.zeros((p,p))
    for k in range(0, p):
        # Trapezium method
        r, e = trapezium(f, a, b, 2**k)
        I[k, 0] = r
        
        # Romberg formula
        for j in range(0, k):
            I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)
        
    return I