import os
import shutil
import argparse
import torchvision.transforms as transforms
from torchvision import datasets
from torchvision.utils import save_image
import numpy as np

def save_cifar10(origin_dataset_dir, seed = 42):
    transform = transforms.ToTensor()
    train_dataset = datasets.CIFAR10(root=origin_dataset_dir,train=True,download=True,transform=transform)
    test_dataset = datasets.CIFAR10(root=origin_dataset_dir,train=False,download=True,transform=transform)
    return train_dataset, test_dataset

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dataset_dir", type=str, default="dataset")
    parser.add_argument("--temp_dir", type=str, default="/tmp")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    origin_dataset_dir = os.path.join(args.dataset_dir, "cifar10")
    temp_dataset_dir = os.path.join(args.temp_dir, "cifar10")
    if args.force:
        if os.path.exists(origin_dataset_dir):
            shutil.rmtree(origin_dataset_dir)

    if not args.force and (os.path.exists(origin_dataset_dir)):
        print("Dataset already exists")
        exit()

    if not os.path.exists(origin_dataset_dir):
        os.makedirs(origin_dataset_dir)
        os.makedirs(temp_dataset_dir)

    train_dataset, test_dataset = save_cifar10(temp_dataset_dir, args.seed)
    shutil.copytree(temp_dataset_dir, origin_dataset_dir)
    shutil.rmtree(temp_dataset_dir)
    print("Prepare dataset Done")