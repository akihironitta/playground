from warnings import warn

import torch
import torchvision


def main():
    try:
        ds = torchvision.datasets.MNIST("datasets", download=False)
        warn("cache found.")
    except:
        warn("cache not found.")
        ds = torchvision.datasets.MNIST("datasets", download=True)


if __name__ == '__main__':
    main()
