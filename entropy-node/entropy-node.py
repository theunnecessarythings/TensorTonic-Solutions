import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    y = np.asarray(y)
    ys, cts = np.unique(y, return_counts=True)

    ent = 0
    for _, ct in zip(ys, cts):
        if ct == 0: continue
        pi = ct / len(y)
        ent += pi * np.log2(pi)

    return float(-ent)