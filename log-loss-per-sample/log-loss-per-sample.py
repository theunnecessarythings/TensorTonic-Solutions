import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """

    res = [0] * len(y_true)

    for i in range(len(res)):
        p_hat = min(1 - eps, max(eps, y_pred[i]))
        res[i] = -(y_true[i] * math.log(p_hat) + (1 - y_true[i]) * math.log(1 - p_hat))

    return res
