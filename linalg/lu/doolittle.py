import numpy as np

def doolittle(n, A):
    # Define L and U
    L = np.zeros(shape=(n,n))
    U = np.zeros(shape=(n,n))
    
    # Asign U diagonal to ones
    l = np.ones(n)
    for idx, li in enumerate(l):
        L[idx][idx] = li
    
    U[0][0] = np.divide(A[0][0], l[0])
    
    if L[0][0]*U[0][0] == 0:
        return "Impossible factorization"

    # Start first row of U and first column of L
    for j in range(1, n):
        U[0][j] = np.divide(A[0][j], L[0][0])
        L[j][0] = np.divide(A[j][0], U[0][0])

    # Fill the other rows and colums
    for i in range(1, n-1):
        
        # U diagonal
        z = 0
        for k in range(i):
            z += L[i][k] * U[k][i]
        
        U[i][i] = A[i][i] - z
        
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
    U[n-1][n-1] = A[n-1][n-1] - z

    return np.asarray(L), np.asarray(U)