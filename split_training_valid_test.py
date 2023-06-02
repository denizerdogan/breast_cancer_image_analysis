# Split the csv file into training, validation and test sets with a ratio of 70:10:20 
# with similar "super_classification" ratio representation in each set.

import csv
import os

import pandas as pd

csv_file = "QC/combined_df_correct_labels.csv"

# read csv into pandas dataframe
df = pd.read_csv(csv_file)

# get the unique values and their frequencies in the column "super_classification"
unique_values = df["super_classification"].value_counts()

print(unique_values)

# separate the dataframe into 4 dataframes according to the values in the column "super_classification"
df_1 = df[df["super_classification"] == 1]
df_2 = df[df["super_classification"] == 2]
df_3 = df[df["super_classification"] == 3]
df_4 = df[df["super_classification"] == 4]

# split the dataframes into training, validation and test sets with a ratio of 70:10:20
df_1_train = df_1.sample(frac=0.7, random_state=0)
df_1_valid = df_1.drop(df_1_train.index)
df_1_test = df_1_valid.sample(frac=0.66, random_state=0)
df_1_valid = df_1_valid.drop(df_1_test.index)

df_2_train = df_2.sample(frac=0.7, random_state=0)
df_2_valid = df_2.drop(df_2_train.index)
df_2_test = df_2_valid.sample(frac=0.66, random_state=0)
df_2_valid = df_2_valid.drop(df_2_test.index)

df_3_train = df_3.sample(frac=0.7, random_state=0)
df_3_valid = df_3.drop(df_3_train.index)
df_3_test = df_3_valid.sample(frac=0.66, random_state=0)
df_3_valid = df_3_valid.drop(df_3_test.index)

df_4_train = df_4.sample(frac=0.7, random_state=0)
df_4_valid = df_4.drop(df_4_train.index)
df_4_test = df_4_valid.sample(frac=0.66, random_state=0)
df_4_valid = df_4_valid.drop(df_4_test.index)

# combine the training, validation and test sets into one dataframe
df_train = pd.concat([df_1_train, df_2_train, df_3_train, df_4_train])
df_valid = pd.concat([df_1_valid, df_2_valid, df_3_valid, df_4_valid])
df_test = pd.concat([df_1_test, df_2_test, df_3_test, df_4_test])

# shuffle the dataframes
df_train = df_train.sample(frac=1, random_state=0)
df_valid = df_valid.sample(frac=1, random_state=0)
df_test = df_test.sample(frac=1, random_state=0)

# print their lengths
print(len(df_train))
print(len(df_valid))
print(len(df_test))

# write the dataframes to csv files
df_train.to_csv("QC/df_train.csv", index=False)
df_valid.to_csv("QC/df_valid.csv", index=False)
df_test.to_csv("QC/df_test.csv", index=False)

