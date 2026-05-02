import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """

    X = np.asarray(X)
    mu = X.mean(axis=0)
    N = len(X)
    if N == 1 or X.ndim != 2: return None
    X_centered = X - mu

    return 1 / (N - 1) * X_centered.T @ X_centered