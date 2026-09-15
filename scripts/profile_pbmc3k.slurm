#!/bin/bash
#SBATCH --job-name=pbmc3k_profile
#SBATCH --output=logs/pbmc3k_%j.out
#SBATCH --error=logs/pbmc3k_%j.err
#SBATCH --time=00:02:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G

set -euo pipefail

cd ..
source bmi500/bin/activate

/usr/bin/time -v python scanpy_pbmc.py \
  --data-dir data \
  --data-set pbmc3k \
  --out-dir profiling_output \
  --num-threads "${SLURM_CPUS_PER_TASK:-1}"