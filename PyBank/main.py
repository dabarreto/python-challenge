# ---------------------------------------------------------------------------------------------------------
# PyBank
# ---------------------------------------------------------------------------------------------------------
# Your task is to create a Python script that analyzes the records to calculate each of the following:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in losses (date and amount) over the entire period

# import dependecies
import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join("/Users/anadb/Desktop/adbr_bootcamp_2021/homework_repo/python-challenge/PyBank/Resources/budget_data.csv")

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

