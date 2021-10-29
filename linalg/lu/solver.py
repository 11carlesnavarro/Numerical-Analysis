import numpy as np

def lu_solver(L, U, b, n):
    y = np.zeros(7)
    x = np.zeros(7)
    
    y[0] = b[0] / L[0][0]
    for i in range(1, n):
        z = 0
        for j in range(i):
            z += L[i][j] * y[j]
        y[i] = (b[i] - z) / L[i][i]
    
    
    x[n-1] = y[n-1] / U[n-1][n-1]
        
    for i in range(n-2,-1, -1):
        z = 0        
        for j in range(n-1, i, -1):
            z += U[i][j] * x[j]
        x[i] = (y[i] - z) / U[i][i]
        
    return y, x
    
def complex_lu_solver(L, U, b, n):
    y = np.zeros(7, dtype=np.complex)
    x = np.zeros(7, dtype=np.complex)
    
    y[0] = b[0] / L[0][0]
    for i in range(1, n):
        z = 0
        for j in range(i):
            z += L[i][j] * y[j]
        y[i] = (b[i] - z) / L[i][i]
    
    
    x[n-1] = y[n-1] / U[n-1][n-1]
        
    for i in range(n-2,-1, -1):
        z = 0        
        for j in range(n-1, i, -1):
            z += U[i][j] * x[j]
        x[i] = (y[i] - z) / U[i][i]
        
    return y, x
