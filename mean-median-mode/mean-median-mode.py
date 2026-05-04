import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """

    x = np.asarray(x)
    vals, counts = np.unique(x, return_counts=True)
    mode = vals[np.argmax(counts)]
    return x.mean(), np.median(x), mode