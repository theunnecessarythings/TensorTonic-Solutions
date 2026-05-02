def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """

    count = len(set(recommended[:k]).intersection(relevant))

    return [count / k, count / len(relevant)]