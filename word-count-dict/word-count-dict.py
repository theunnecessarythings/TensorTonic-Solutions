def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    res = {}
    for s in sentences:
        for x in s:
            if x in res: res[x]+=1
            else: res[x] = 1

    return res