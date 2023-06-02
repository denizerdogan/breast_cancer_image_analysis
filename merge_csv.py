# Function : Merge all csv files in a folder into one csv file

import os
import glob
import pandas as pd
import sys

# get the path to the directory containing the csv files
csv_path = "QC/csv_modified"
outdir = "QC/"

# get all csv files in the directory
csv_files = glob.glob(os.path.join(csv_path, "*.csv"))

# loop through the files and read them in with pandas
# append them to the dataframe

df = pd.DataFrame()
for f in csv_files:
    df = df.append(pd.read_csv(f))

# write the dataframe to a new csv file
df.to_csv(os.path.join(outdir, "combined_df.csv"), index=False)


