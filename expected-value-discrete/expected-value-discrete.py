import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """

    exp = 0.0
    if abs(sum(p) - 1) >= 1e-8:
        raise ValueError("")

    for i in range(len(x)):
        exp += x[i] * p[i]

    return exp