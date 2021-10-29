import numpy as np

def crout(n, A):
    
    # Define L and U
    L = np.zeros(shape=(n,n))
    U = np.zeros(shape=(n,n))
    
    # Asign U diagonal to ones
    u = np.ones(n)
    for idx, ui in enumerate(u):
        U[idx][idx] = ui
    
    L[0][0] = np.divide(A[0][0], u[0])
    
    if L[0][0]*U[0][0] == 0:
        return "Impossible factorization"
    
    # Start first row of U and first column of L
    for j in range(1, n):
        U[0][j] = np.divide(A[0][j], L[0][0])
        L[j][0] = np.divide(A[j][0], U[0][0])
    
    # Fill the other rows and colums
    for i in range(1, n-1):
        
        # L diagonal
        z = 0
        for k in range(i):
            z += L[i][k] * U[k][i]
        
        L[i][i] = A[i][i] - z
        
        if L[i][i] * U[i][i] ==0:
            return "Impossible factorization"
                
        for j in range(i + 1, n):
            
            # ith row of U
            z = 0
            for k in range(i):
                z += L[i][k] * U[k][j]
            U[i][j] = (A[i][j] - z) / L[i][i]
            
            # ith column of L
            z = 0
            for k in range(i):
                z += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - z) / U[i][i]
    
    # (n,n) value of L
    z = 0
    for k in range(n):
        z += L[n-1][k] * U[k][n-1]
    L[n-1][n-1] = A[n-1][n-1] - z
    
    return np.asarray(L), np.asarray(U)

def crout_tridiagonal(n, A):
    
    # Define L and U
    L = np.zeros(shape=(n,n))
    U = np.zeros(shape=(n,n))

    # Define U diagonal
    for i in range(n):
        U[i][i] = 1

    # Set initial L11 and U12 values
    L[0][0] = A[0][0]
    U[0][1] = A[0][1] / L[0][0]
    
    for i in range(1, n-1):
        # ith column of L
        L[i][i-1] = A[i][i-1]
        L[i][i] = A[i][i] - L[i][i-1] * U[i-1][i]
        
        # ith row of U
        U[i][i+1] = A[i][i+1] / L[i][i]
    
    # nth row of L
    L[n-1][n-2] = A[n-1][n-2]
    L[n-1][n-1] = A[n-1][n-1] - L[n-1][n-2] * U[n-2][n-1]
    
    return np.asarray(L), np.asarray(U) 










