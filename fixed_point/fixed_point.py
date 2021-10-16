
def fixed_point(g, p0, tol, N0):
    """
    Fixed point iteration
    :param g: function
    :param p0: initial aproximation
    :param tol: tolerance
    :param N0: max number of iterations
    :return: p that makes f(p) = p
    """
    
    i = 1
    p0_matrix = []
    gp0_matrix = []
    error_matrix = []
    
    convergence = False
    while i <= N0:
        p = g(p0)
        
        p0_matrix.append(p0)
        gp0_matrix.append(p)
        error_matrix.append(abs(p-p0))
        
        if abs(p - p0) < tol:
            convergence = True
            break
        i += 1
        p0 = p
        
    data = {'p0_matrix': p0_matrix,
           'gp0_matrix': gp0_matrix,
           'error_matrix': error_matrix}    
    
    if convergence:
        return (p, data, convergence)
    else:
        return ('El método fracasó después de {} iteraciones'.format(N0), data, convergence)