
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
    phat_matrix = []
    error_matrix = []
    
    convergence = False
    while i <= N0:
        p1 = g(p0)
        p2 = g(p1)
        phat = p0 - (p1-p0)**2/(p2-2*p1+p0)
        
        p0_matrix.append(p0)
        
        error_matrix.append(abs(phat-p0))
        
        if abs(p1 - p0) < tol:
            convergence = True
            break
        if abs(phat - p0) >= tol:
            phat_matrix.append(phat)
            
        i += 1
        p0 = phat
        
    data = {'p0_matrix': p0_matrix,
           'phat_matrix': phat_matrix,
           'error_matrix': error_matrix}    
    
    
    if convergence:
        return (phat, data, convergence)
    else:
        return ('El método fracasó después de {} iteraciones'.format(N0), data, convergence)