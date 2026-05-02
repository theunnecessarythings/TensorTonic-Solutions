import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    res = 0

    for i in range(len(fpr) - 1):
        res += (tpr[i] + tpr[i+1]) * (fpr[i+1] - fpr[i])

    return 0.5 * res