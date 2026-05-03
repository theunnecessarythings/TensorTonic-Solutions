def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    import math
    h = 0
    for i, probs in enumerate(prob_distributions):
        pi = probs[actual_tokens[i]]
        h += math.log(pi)

    return math.exp(-h / len(actual_tokens))