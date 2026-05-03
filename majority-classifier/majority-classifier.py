import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    unique, counts = np.unique(y_train, return_counts=True)

    max_ct = counts.max()

    return  np.ones(len(X_test)) * unique[counts == max_ct][0]