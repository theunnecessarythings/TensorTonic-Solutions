import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    num =  ((y_pred - y_true) ** 2).sum() 
    denom = ((y_true - y_true.mean()) ** 2).sum()

    if denom == 0:
        return 1.0 if num == 0 else 0.0
    
    return 1 - num / denom