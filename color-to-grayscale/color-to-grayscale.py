def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """

    for i in range(len(image)):
        for j in range(len(image[0])):
            r, g, b = image[i][j]
            image[i][j] = 0.299 * r + 0.587 * g + 0.114 * b

    return image