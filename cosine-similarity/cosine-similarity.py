import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a)
    b = np.asarray(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9)