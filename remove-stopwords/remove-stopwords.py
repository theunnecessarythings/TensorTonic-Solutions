def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    sw = set(stopwords)

    res = []

    for x in tokens:
        if x not in sw:
            res.append(x)

    return res