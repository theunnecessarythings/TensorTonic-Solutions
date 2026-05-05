def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    import math
    w = (max(values) - min(values)) / num_bins
    bins = [0] * len(values)
    if w == 0: return bins
    for i in range(len(values)):
        bins[i] = min(math.floor((values[i] - min(values))/w), num_bins - 1)
    return bins