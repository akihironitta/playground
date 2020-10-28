import torch
import torchvision


def main():
    ds = torchvision.datasets.MNIST(".cache/datasets", download=True)


if __name__ == '__main__':
    main()
