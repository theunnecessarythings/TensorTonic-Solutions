import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    se = (np.asarray(y_pred) - np.asarray(y_true)) ** 2
    return se.mean()