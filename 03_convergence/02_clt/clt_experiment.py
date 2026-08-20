import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
from typing import Literal

options = {
    'uniform': [
        np.random.uniform,
        0.5,
        1 / np.sqrt(12)
    ],
    'exponential': [
        np.random.exponential,
        1,
        1
    ],
    'poisson': [
        np.random.poisson,
        1,
        1
    ],
    'laplace': [
        np.random.laplace,
        0,
        np.sqrt(2)
    ],
    'cauchy': [
        np.random.standard_cauchy,
        None,
        None
    ]
}

def experiment(
        dist: Literal['uniform', 'exponential', 'poisson', 'laplace', 'cauchy'],
        image_name: str|None = None,
        n_max: int = 50
) -> None:
    
    if image_name is None:
        image_name = "03_convergence/02_clt/figures/" + dist + ".gif"

    images = []

    f, mu, sigma = options[dist]

    for n in range(1, n_max + 1):

        x = np.array([f(size=n).mean() for _ in range(10000)])

        fig, ax = plt.subplots()
        ax.hist(x, bins=30, density=True, alpha=0.6)

        if sigma is not None:
            _sigma = sigma / np.sqrt(n)
            xx = np.linspace(mu - 4*_sigma, mu + 4*_sigma, 500)
            pdf = (1 / (_sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((xx - mu) / _sigma)**2)
            ax.plot(xx, pdf, linewidth=2)

        ax.set_title(f"{dist.capitalize()} n = {n}")
        ax.set_xlabel("Sample mean")
        ax.set_ylabel("Density")

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)

        images.append(Image.open(buffer).copy())

        plt.close(fig)

    # Create GIF
    images[0].save(
        image_name,
        save_all=True,
        append_images=images[1:],
        duration=300,
        loop=0
    )

experiment('uniform')
experiment('exponential')
experiment('poisson')
experiment('laplace')
experiment('cauchy')
