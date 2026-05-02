import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.asarray(A)
    s = 0
    for i in range(A.shape[0]):
        s += A[i, i]
    return s