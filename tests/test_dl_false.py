from warnings import warn

import torch
from torchvision.datasets import MNIST


def test_dl_false(datadir, tmpdir):
    warn(f"datadir='{datadir}' tmpdir='{tmpdir}'")
    dataset = MNIST(datadir, download=False)

def test_dl_false2(datadir, tmpdir):
    warn(f"datadir='{datadir}' tmpdir='{tmpdir}'")
    dataset = MNIST(datadir, download=False)
