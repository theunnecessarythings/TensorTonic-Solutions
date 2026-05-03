def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    x1, y1, x2, y2 = box_a
    a = max(0, y2 - y1) * max(0, x2 - x1)
    x1, y1, x2, y2 = box_b
    b = max(0,y2 - y1) * max( 0, x2 - x1)

    x1 = max(box_a[0], box_b[0])
    y1 = max(box_a[1], box_b[1])
    x2 = min(box_a[2], box_b[2])
    y2 = min(box_a[3], box_b[3])

    i = max(0, y2 - y1) * max(0, x2 - x1)

    return i / (a + b - i)
    
    