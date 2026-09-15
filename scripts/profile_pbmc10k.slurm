#!/bin/bash
#SBATCH --job-name=pbmc10k_profile
#SBATCH --output=logs/pbmc10k_%j.out
#SBATCH --error=logs/pbmc10k_%j.err
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

set -euo pipefail

cd ..
source bmi500/bin/activate

/usr/bin/time -v python scanpy_pbmc.py \
  --data-dir data \
  --data-set pbmc10k \
  --out-dir profiling_output \
  --num-threads 1