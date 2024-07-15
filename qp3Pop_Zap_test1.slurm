#!/bin/bash -e
#SBATCH --account=yh6km
#SBATCH --job-name=qp3Pop_Zap_test1
#SBATCH --cpus-per-task=1
#SBATCH --mem=100G
#SBATCH --partition=yang2

#SBATCH --mail-type=ALL
#SBATCH --mail-user=skyler.he@richmond.edu

#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

echo "I ran on: $SLURM_NODELIST"
echo "Starting at `date`"

##Run command
source activate treemix
export LD_LIBRARY_PATH=/usr/local/sw/anaconda/anaconda3/envs/treemix/lib/
qp3Pop -p zind_prune_i_100_10_2_dfall2.par > output_longname.txt

echo "Finished at `date`"

