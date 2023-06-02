# script to manipulate and combine csv files

import csv
import os
import sys
import pandas as pd

# get the path to the directory containing the csv files
csv_path = "QC/csv"
outdir = "QC"



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


# get_filename("deneme.csv", outdir)


# #  do this for all csv files in the directory
# for filename in os.listdir(csv_path):
#     if filename.endswith(".csv"):
#         get_filename(filename, outdir)
#     else:
#         continue



# read in a csv file as a pandas dataframe
df = pd.read_csv("QC/combined_df.csv")

# change the values in column "super_classification" according to the following rules:
# 1. if the value is "tumor_any", change it to "1"
# 2. if the value is "sTIL", change it to "2"
# 3. if the value is "nonTIL_stromal", change it to "3"
# 4. if the value is "AMBIGUOUS" or "other_nucleus", change it to "4"

df["super_classification"] = df["super_classification"].replace("tumor_any", "1")
df["super_classification"] = df["super_classification"].replace("sTIL", "2")
df["super_classification"] = df["super_classification"].replace("nonTIL_stromal", "3")
df["super_classification"] = df["super_classification"].replace("AMBIGUOUS", "4")
df["super_classification"] = df["super_classification"].replace("other_nucleus", "4")

# write the dataframe to a new csv file
df.to_csv(os.path.join(outdir, "combined_df_correct_labels.csv"), index=False)




