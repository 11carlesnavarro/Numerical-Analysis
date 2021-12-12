def trapezium(f, a, b, n):
    '''
    Aprox the integral of a function f between a and b
    by using the composite trapezoidal rule.
    
    Parameters
    ----------
    f: function to integrate
    int a, b : integral limits
    int n : number of subintervals in (a,b)
    
    Returns
    -------
    float r: Aprox value of the integral
    int e: number of times f has been evaluated
    '''
    h = (b-a) / n
    x0 = f(a) + f(b)
    
    x1 = 0
    x2 = 0
    e = 2
    
    for i in range(1, n):
        x = a + i*h
        x2 += f(x)
        e += 1
    r = h*(x0 + 2*x2) / 2
    
    return r, e