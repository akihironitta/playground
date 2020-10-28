import torch
import torchvision


def main():
    try:
        ds = torchvision.datasets.MNIST(".cache/datasets", download=False)
    except:
        ds = torchvision.datasets.MNIST(".cache/datasets", download=True)


if __name__ == '__main__':
    main()
