def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    res = []

    for x in values:
        res.append([x ** i for i in range(degree + 1)])
    return res