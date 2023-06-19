import sys
import os.path
import argparse
import glob
import pandas as pd
from pathlib import Path
import SPACE2

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Run SPACE2 clustering on .pdb files in a folder.')
parser.add_argument('-i', '--inputfile', help='File containing the full path location of all the .pdb files', required=True)
parser.add_argument('-t', '--tag', help='File containing the full path location of all the .pdb files', required=False, default='spa2')
parser.add_argument("-r", "--refresh",     help="refresh", action="store_true")
parser.add_argument("-d", "--debug",     help="debug", action="store_true")
parser.add_argument("-v", "--verbose",     help="verbose", action="store_true")

args = parser.parse_args()

# Start program
sys.stderr.write("# inputfile is %s\n" % args.inputfile)

(dirname,filename) = os.path.split(args.inputfile)
(filebasename,file_extension) = os.path.splitext(filename)

outfile = dirname + '/' + filebasename + '.' + args.tag + '.csv'
if not args.refresh:
    p = Path(outfile)
    if (p.exists()) and (os.stat(outfile).st_size>180):
        print(outfile)
        sys.exit(0)

# Get the list of .pdb files in the specified folder
# Read the file paths from input.txt
with open(args.inputfile, 'r') as file:
    sys.stderr.write("# reading %s\n" % args.inputfile)
    file_paths = file.read().splitlines()

# Run agglomerative clustering
df = SPACE2.agglomerative_clustering(file_paths, cutoff=1.25)


#antibody_models = glob.glob(folder_path + '/*.pdb')
## Run agglomerative clustering
#df = SPACE2.agglomerative_clustering(antibody_models, cutoff=1.25)

# Print the DataFrame to a CSV file
df.to_csv(outfile, index=False)
