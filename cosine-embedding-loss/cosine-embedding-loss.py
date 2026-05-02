def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    import numpy as np
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)

    cos = np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))
    return 1 - cos if label == 1 else np.maximum(0, cos - margin) 