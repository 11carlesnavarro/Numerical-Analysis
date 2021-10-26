
def bisection(f, a, b, tol, N0):
    """
    Bisection method
    :param f: function 
    :param a: left side of the interval
    :param b: right side of the interval
    :param tol: tolerance
    :param N0: max number of iterations
    :return: p that makes f(p) = 0
    """
    i = 1
    FA = f(a)
    
    a_matrix = []
    b_matrix = []
    p_matrix = []
    f_matrix = []
    error_matrix = []
    
    convergence = False
    while i <= N0:
        p = a + (b-a) / 2
        FP = f(p)
        
        a_matrix.append(a)
        b_matrix.append(b)
        p_matrix.append(p)
        f_matrix.append(f(p))
        error_matrix.append(p - a)
        
        if FP == 0 or (b-a)/2 < tol:
            convergence = True
            break
        
        i += 1
        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p
    
    data = {'a_matrix': a_matrix,
           'b_matrix': b_matrix,
           'p_matrix': p_matrix,
           'f_matrix': f_matrix,
           'error_matrix': error_matrix}

    if convergence:
        return (p, data, convergence)
    else:
        return ('El método fracasó después de {} iteraciones'.format(N0), data, convergence)
            