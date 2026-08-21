import numpy as np
from matplotlib import pyplot as plt

def sample_mean_convergence(distribution, theopretical_mean, picture_path):

    X = distribution(size=10000)

    sample_mean = np.cumsum(X) / np.arange(1, X.shape[0] + 1)

    error = np.abs(sample_mean - theopretical_mean)


    fig, ax = plt.subplots()
    ax.set_title(f"Sample mean convergence")
    ax.set_xlabel("n")
    ax.set_ylabel("Error")
    ax.plot(error)
    ax.hlines(0, 0, X.shape[0])
    fig.savefig(picture_path)


# sample_mean_convergence(lambda size: np.random.normal(2, 3, size=size), 2, '03_convergence/01_lln/figures/sample_mean_convergence.jpeg')

# sample_mean_convergence(np.random.exponential, 1, '03_convergence/01_lln/figures/sample_mean_convergence_exponential.jpeg')


def weak_lln(distribution, theoretical_mean, n: int = 100000, N: int = 1000, epsilon : float = 0.01):

    X = distribution(size=(n, N))

    X_bar = np.cumsum(X, axis=0) / np.arange(1, X.shape[0] + 1)[:, None]

    error = np.abs(X_bar - theoretical_mean)

    probability = np.mean(error > epsilon, axis=1)

    return probability

def save_weak_lln_plot(prob, picture_path, title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("n")
    ax.set_ylabel("Prob(|X_n - mu| > eps)")
    ax.plot(prob)
    ax.hlines(0, 0, prob.shape[0], color='b', linestyles='--')
    fig.savefig(picture_path)


prob = weak_lln(np.random.exponential, 1)
save_weak_lln_plot(prob, '03_convergence/01_lln/figures/exponential_dist_weak_lln.jpeg', title="Weak LLN - Exponential")


prob = weak_lln(lambda size: np.random.binomial(5, 0.2, size), 1)
save_weak_lln_plot(prob, '03_convergence/01_lln/figures/binomial_dist_weak_lln.jpeg', title="Weak LLN - Binomial")


