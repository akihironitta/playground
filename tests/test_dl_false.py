import torch
from torchvision.datasets import MNIST


def test_dl_false(datadir):
    raise Exception(f"datadir -> {datadir}")
    dataset = MNIST(datadir, download=False)
