#!/bin/bash
#SBATCH --job-name=pbmc6k_profile
#SBATCH --output=logs/pbmc6k_%j.out
#SBATCH --error=logs/pbmc6k_%j.err
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

set -euo pipefail

cd ..
source bmi500/bin/activate

/usr/bin/time -v python scanpy_pbmc.py \
  --data-dir data \
  --data-set pbmc6k \
  --out-dir profiling_output \
  --num-threads "${SLURM_CPUS_PER_TASK:-1}"