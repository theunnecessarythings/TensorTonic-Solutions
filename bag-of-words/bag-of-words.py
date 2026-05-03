import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    bow = np.zeros(len(vocab), dtype=np.int64)
    map = { x: i for i, x in enumerate(vocab) }

    for x in tokens:
        if x not in map: continue
        bow[map[x]] += 1

    return bow