import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    m, n = len(A), len(A[0])

    res = np.zeros((n, m))

    for i in range(m):
        for j in range(n):
            res[j][i] = A[i][j]

    return res