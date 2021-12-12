import numpy as np
import pandas as pd

def cgauss_file(f, a, b, file):
    '''
    Implementation of the Gauss Quadrature for to
    solve the value of the integral of a function
    in an interval [a,b], by using a file with the 
    roots and weights of the polynomials
    
    Parameters:
    -----------
    f: function to integrate
    a, b: integration limits
    file: .dat with roots and weights
    
    Returns:
    --------
    r: result of the integral
    '''
    
    data = pd.read_table(file, names=['raices', 'pesos'], delim_whitespace=True, header=None)
    pd.set_option('display.precision', 16)
    
    w = np.asarray(data['pesos'].values.tolist())
    x = np.asarray(data['raices'].values.tolist())
    x = ((b-a)*x+a+b)/2
    y = f(x)
    
    r = np.dot(y,w)*(b-a)/2.0
    return r

