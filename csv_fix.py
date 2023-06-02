# script to manipulate and combine csv files

import csv
import os
import sys
import pandas as pd

# get the path to the directory containing the csv files
csv_path = "QC/csv"
outdir = "QC/csv_modified"



# get the filename and make it the first column
def get_filename(filename, outdir):

    file_path = os.path.join(csv_path, filename)

    # read csv into pandas dataframe
    df = pd.read_csv(file_path)

    filename_without_extension = filename.split(".")[0]


    # remove first column
    df.drop(df.columns[0], axis=1, inplace=True)



    # add filename_without_extension to the first column
    df.insert(0, "image_id", filename_without_extension)

    # remove columns named "raw_classification" and "main_classification"
    if "raw_classification" in df.columns:
        df.drop("raw_classification", axis=1, inplace=True)

    if "main_classification" in df.columns:
        df.drop("main_classification", axis=1, inplace=True)

    if "type" in df.columns:
        df.drop("type", axis=1, inplace=True)

    if "coords_x" in df.columns:
        df.drop("coords_x", axis=1, inplace=True)
    
    if "coords_y" in df.columns:
        df.drop("coords_y", axis=1, inplace=True)


    # write the new csv file
    df.to_csv(os.path.join(outdir, filename), index=False)

    return filename


get_filename("deneme.csv", outdir)


#  do this for all csv files in the directory
for filename in os.listdir(csv_path):
    if filename.endswith(".csv"):
        get_filename(filename, outdir)
    else:
        continue