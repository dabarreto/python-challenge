# -------------------------------------------------------------------------------------------------------------------------
# PyBank
# -------------------------------------------------------------------------------------------------------------------------
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.
#
# Your task is to create a Python script that analyzes the records to calculate each of the following:
#   The total number of months included in the dataset.
#   The net total amount of "Profit/Losses" over the entire period.
#   Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes.
#   The greatest increase in profits (date and amount) over the entire period.
#   The greatest decrease in losses (date and amount) over the entire period.
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# -------------------------------------------------------------------------------------------------------------------------

# Import dependecies
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join("/Users/anadb/Desktop/adbr_bootcamp_2021/homework_repo/python-challenge/PyBank/Resources/budget_data.csv")
#csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

with open(pybank_csv) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
#    print(f"CSV Header:\n{csv_header}")
#    print("CSV Contents:\n")

    # Read each row of data after the header
#    for row in csvreader:
#        print(row)

    # Lists to store data
    months = []
    profit_losses = []
    difference = []
    total_profit_loss = 0
   
    # Read each row of data after the header
    for row in csvreader:
    
        # Calculate total months
        month = row[0]
        months.append(month)
        month_count = len(months)
#        print(month_count)

        profit_loss = row[1]
        profit_losses.append(profit_loss)
        
    
    for i in range(0,len(profit_losses)):
        
        # Calculate total "Profit/Losses"
        total_profit_loss +=int(profit_losses[i])
#        print(total_profit_loss)

    
    for i in range(1, len(profit_losses)):
        current = int(profit_losses[i])
        previo = int(profit_losses [i - 1])
        difference.append((current-previo))

        # Average "Profit/Losses" over the entire period
        average = (sum(difference) / len(difference))
#        print(average)

        # Gratest increase/deacrease in "Profit/Losses" and their dates
        max_change = max(difference)
#        print (max_change)

        max_date = months[difference.index(max(difference))+1]
#        print(max_date)

        min_change = min(difference)
#        print(min_change)
        
        min_date = months[difference.index(min(difference))+1]
#        print(min_date)
        
# Print Analysis in terminal:
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {month_count}')
print(f'Total : ${total_profit_loss}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {max_date} (${max_change})')
print(f'Greatest Decrease in Profits: {min_date} (${min_change})')

# Export file in txt:
analysis_output = os.path.join('/Users/anadb/Desktop/adbr_bootcamp_2021/homework_repo/python-challenge/PyBank/Analysis/analysis.txt')

with open(analysis_output, "w") as txt_file:
    txt_file.write('Financial Analysis \n')
    txt_file.write('---------------------------- \n')
    txt_file.write(f'Total Months: {month_count} \n')
    txt_file.write(f'Total : ${total_profit_loss} \n')
    txt_file.write(f'Average Change: ${average} \n')
    txt_file.write(f'Greatest Increase in Profits: {max_date} (${max_change}) \n')
    txt_file.write(f'Greatest Decrease in Profits: {min_date} (${min_change}) \n')


