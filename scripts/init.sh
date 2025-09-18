#!/bin/bash

mkdir -m 777 -p dataset
mkdir -m 777 -p slurm_logs
mkdir -m 777 -p nsight_logs
mkdir -m 777 -p runs
mkdir -m 777 -p runs/default
mkdir -m 777 -p runs/dp_2
mkdir -m 777 -p runs/dp_4

pip install -r requirements.txt

# Our master node has limited power, so we download dataset to /tmp, and then copy to dataset directory.
mkdir -m 777 -p /tmp

python my_lib/init_dataset.py --seed 42 --temp_dir /tmp --dataset_dir dataset