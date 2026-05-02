def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    import numpy as np
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    tp = (y_true == y_pred).sum()
    fp = (y_true != y_pred).sum()
    fn = fp

    return 2 * tp / (2 * tp + fp + fn)
    