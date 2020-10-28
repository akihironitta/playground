import torch
import torchvision


def main():
    try:
        ds = torchvision.datasets.MNIST(".cache/datasets", download=False)
    except:
        print("dataset not found. downloading...")
        ds = torchvision.datasets.MNIST(".cache/datasets", download=True)
        print("dataset downloaded.")


if __name__ == '__main__':
    main()
