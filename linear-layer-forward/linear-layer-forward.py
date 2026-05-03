def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """


    n, d_in, d_out = len(X), len(W), len(b)
    Y = [[0] * d_out for _ in range(n)]
    
    for i in range(n):
        for j in range(d_out):
            sum = 0
            for k in range(d_in):
                sum += X[i][k] * W[k][j] 
            Y[i][j] = sum + b[j]

    return Y
