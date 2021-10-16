
def steffensen(g, p0, tol, N0):
    """
    Aitken method for accelerated convergence
    :param p0: initial aprox
    :param tol: tolerance
    :param N0: max number of iterations
    :return: aproximate solution phat
    """
    
    i = 1
    
    p0_matrix = []
    p1_matrix = []
    p2_matrix = []
    error_matrix = []
    
    convergence = False
    while i <= N0:
        p1 = g(p0)
        p2 = g(p1)
        phat = p0 - (p1-p0)**2/(p2-2*p1+p0)
        
        p0_matrix.append(p0)
        p1_matrix.append(p1)
        p2_matrix.append(p2)
        error_matrix.append(abs(phat-p0))
        
        if abs(phat - p0) < tol:
            convergence = True
            break
        
        i += 1
        p0 = phat
        
    data = {'p0_matrix': p0_matrix,
           'p1_matrix': p1_matrix,
            'p2_matrix': p2_matrix,
           'error_matrix': error_matrix}    
    
    
    if convergence:
        return (phat, data, convergence)
    else:
        return ('El método fracasó después de {} iteraciones'.format(N0), data, convergence)