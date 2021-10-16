import numpy as np    
import pandas as pd

def newton(f, df, p0, tol, N0):
    """
    Newthon-Rapson method
    :param f: function
    :param df: derivative of f
    :param p0: initial aproximation
    :param tol: tolerance
    :param N0: max number of iterations
    :return: zero of the function or not convergence error
    """
    p0_matrix = []
    p_matrix = []
    f_matrix = []
    df_matrix = []
    error_matrix = []
    data = {}
    convergence = False
    i = 0
    while i <= N0:
        p = p0 - (f(p0) / df(p0))
        
        p0_matrix.append(p0)
        p_matrix.append(p)
        f_matrix.append(f(p0))
        df_matrix.append(df(p0))
        error_matrix.append(p-p0)
        
        if abs(p - p0) >= tol:
            i += 1
            p0 = p
        else:
            convergence = True
            break
    
    data = {'p0_matrix': p0_matrix,
           'p_matrix': p_matrix,
           'f_matrix': f_matrix,
           'df_matrix': df_matrix,
           'error_matrix': error_matrix}
    n_iters = i + 1
    
    if convergence:        
        return (p, data, convergence) 
    
    return ("El método fracasó después de {} iteraciones".format(N0) , data, convergence)