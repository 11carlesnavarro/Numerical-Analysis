import numpy as np

def choleski(n, A):
    
    # Define L and U
    L = np.zeros(shape=(n,n), dtype = np.complex)
    U = np.zeros(shape=(n,n), dtype = np.complex)

    L[0][0] = np.sqrt(A[0][0])
    
    for j in range(1, n):
        L[j][0] = A[j][0] / L[0][0]
    
    for i in range(1, n-1):
        z = 0
        for k in range(i):
            z += L[i][k] ** 2
            
        L[i][i] = np.sqrt(A[i][i] - z)
    
        
        for j in range(i + 1, n):
            z = 0
            for k in range(i):
                z += L[j][k] * L[i][k]
            L[j][i] = (A[i][j] - z) / L[i][i]
    
    z = 0
    for k in range(n):
        z += L[n-1][k]**2
    
    L[n-1][n-1] = np.sqrt(A[n-1][n-1] - z)
    
    return L

def choleski_modified(n, A):
    
    # Define L and U
    L = np.zeros(shape=(n,n))
    U = np.zeros(shape=(n,n))

    L[0][0] = np.sqrt(A[0][0])
    U[0][0] = np.sqrt(A[0][0])
    
    for j in range(1, n):
        L[j][0] = A[j][0] / L[0][0]
        U[0][j] = A[0][j] / L[0][0]
        
    for i in range(1, n-1):
        z = 0
        for k in range(i):
            z += L[i][k]*U[k][i]
        L[i][i] = U[i][i] = np.sqrt(A[i][i] - z)
        
        for j in range(i+1, n):
            z1 = 0
            z2 = 0
            for k in range(i):
                z1 += L[j][k] * U[i][k]
                z2 += L[i][k] * U[k][j]
                
            L[j][i] = (A[j][i] - z1) / L[i][i]
            U[i][j] = (A[i][j]) / L[i][i]
    z = 0
    for k in range(n):
        z += L[n-1][k] * U[k][n-1]
        
    L[n-1][n-1] = U[n-1][n-1] = np.sqrt(A[n-1][n-1] - z)
            
    return L, U