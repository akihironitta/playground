from warnings import warn

import torch
from torchvision.datasets import MNIST


def test_dl_false(datadir):
    warn(f"datadir='{datadir}'")
    dataset = MNIST(datadir, download=False)
