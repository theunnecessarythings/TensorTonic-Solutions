def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    recs = []
    for x in recommendations:
        recs.extend(x)
    return len(set(recs)) / n_items