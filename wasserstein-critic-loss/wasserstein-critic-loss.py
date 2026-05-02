import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    return np.asarray(fake_scores).mean() - np.asarray(real_scores).mean()