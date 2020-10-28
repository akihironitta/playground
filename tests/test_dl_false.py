import torch
from torchvision.datasets import MNIST


def test_dl_false():
    dataset = MNIST("./.cache/datasets/", download=False)
