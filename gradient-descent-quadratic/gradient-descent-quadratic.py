def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = x0
    for i in range(steps):
        f_x = a * x * x + b * x + c
        grad = 2 * a * x + b
        x -= lr * grad
        
    return x