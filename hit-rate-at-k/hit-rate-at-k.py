def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    ct = 0
    for rs, gs in zip(recommendations, ground_truth):
        for r in rs[:k]:
            if r in gs:
                ct += 1
                break

    return ct / len(ground_truth)