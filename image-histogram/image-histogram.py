def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    import numpy as np
    hist = np.zeros(256)

    for row in image:
        for p in row:
            hist[p]+=1

    return hist.tolist()