import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.asarray(x)
    var = 1 / (len(x) - 1) * ((x - x.mean()) ** 2).sum()

    return var, np.sqrt(var)