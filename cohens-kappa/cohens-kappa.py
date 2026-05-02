import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """

    r1 = np.asarray(rater1)
    r2 = np.asarray(rater2)

    po = (r1 == r2).mean()
    ks = np.union1d(r1, r2)

    pe = 0
    for k in ks:
        pe += (r1 == k).mean() * (r2 == k).mean()

    if pe == 1.0:
        return 1.0 if po == 1.0 else 0.0

    return (po - pe) / (1 - pe)