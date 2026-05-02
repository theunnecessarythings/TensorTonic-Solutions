def elu(X, alpha):
    """
    Apply ELU activation to each element.
    """
    import math
    return [x if x > 0 else alpha * (math.exp(x) - 1) for x in X]