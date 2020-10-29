import torch
from torchvision.datasets import MNIST


def test_dl_false(datadir):
    print(f"datadir -> {datadir}")
    dataset = MNIST(datadir, download=True)
