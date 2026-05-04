def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    ids = []
    for p in points:
        min_i = len(centroids)
        min_d = 1e25
        for i, c in enumerate(centroids):
            dist = sum((p[d] - c[d]) ** 2 for d in range(len(c)))
            if dist < min_d:
                min_d = dist
                min_i = i

        ids.append(min_i)

    return ids