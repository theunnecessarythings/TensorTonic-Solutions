import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    e = np.asarray(y_true) - np.asarray(y_pred)
    return np.where(np.abs(e) <= delta, 1/2 * e * e, delta * (np.abs(e) - 1/2 * delta)).mean()