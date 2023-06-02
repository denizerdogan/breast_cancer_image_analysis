# read in a csv file as a pandas dataframe
# count the unique values in a column and their frequencies


import csv
import os
import sys
import pandas as pd
import numpy as np


# get the path to the directory containing the csv files
csv_path = "QC/combined_df.csv"

# read csv into pandas dataframe
df = pd.read_csv(csv_path)

# get the unique values and their frequencies in the column "super_classification"
unique_values = df["super_classification"].value_counts()

print(unique_values)
