import argparse
import glob
import pandas as pd
import SPACE2

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Run SPACE2 clustering on .pdb files in a folder.')
parser.add_argument('-d', '--folder', help='Folder path containing .pdb files', required=True)
args = parser.parse_args()

# Get the folder path from command-line argument
folder_path = args.folder

# Get the list of .pdb files in the specified folder
antibody_models = glob.glob(folder_path + '/*.pdb')

# Run agglomerative clustering
df = SPACE2.agglomerative_clustering(antibody_models, cutoff=1.25)

# Print the DataFrame to a CSV file
df.to_csv(folder_path + 'output.csv', index=False)
