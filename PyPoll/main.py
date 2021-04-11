# -------------------------------------------------------------------------------------------------------------------------
# PyPoll
# -------------------------------------------------------------------------------------------------------------------------
#  Create a Python script that analyzes the votes and calculates each of the following:
#   - The total number of votes cast
#   - A complete list of candidates who received votes
#   - The percentage of votes each candidate won
#   - The total number of votes each candidate won
#   - The winner of the election based on popular vote.
#  Your final script should both print the analysis to the terminal and export a text file with the results.
# -------------------------------------------------------------------------------------------------------------------------

# Import module to create file paths across operating systems
import os

# Import module to read CSV files
import csv

pypoll_csv = os.path.join('/Users/anadb/Desktop/adbr_bootcamp_2021/homework_repo/python-challenge/PyPoll/Resources/election_data.csv')
#csvpath = os.path.join('python-challenge', 'PyPoll', 'Resources', 'election_data.csv')


with open(pypoll_csv) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)


    # Lists to store data
    candidates = []
    votes = []
    percentage_total = []
    total_votes = 0
 
   
    # Read each row of data after the header
    for row in csvreader:
    
        # Calculate total votes, percentage and winner from candidates
        # vote counter: add 1 row
        total_votes +=  1
#        print(f'Total Votes: {total_votes}')
        if row[2] not in candidates:
                candidates.append(row[2])
                index = candidates.index(row[2])
                votes.append(1)
        else:
                index = candidates.index(row[2])
                votes[index] += 1
        
        for vote in votes:
                percentage = (vote/total_votes) * 100
                percentage = "{:.3f}".format(percentage)
                percentage_total.append(percentage)

        
                winner_votes = max(votes)
                index = votes.index(winner_votes)
                winner_name = candidates[index]

         
# Print Analysis in terminal:
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

for i in range (len(candidates)):
        print(f'{candidates[i]}: {percentage_total[i]}% ({votes[i]})')

print('-------------------------')
print(f'Winner: {winner_name}')

# Export file in txt:
results_output = os.path.join('/Users/anadb/Desktop/adbr_bootcamp_2021/homework_repo/python-challenge/PyPoll/Analysis/results.txt')

with open(results_output, "w") as txt_file:
    txt_file.write(f'Election Results \n')
    txt_file.write(f'------------------------- \n')
    txt_file.write(f'Total Votes: {total_votes} \n')
    txt_file.write(f'------------------------- \n')

    for i in range (len(candidates)):
            txt_file.write(f'{candidates[i]}: {percentage_total[i]}% ({votes[i]}) \n')

    txt_file.write(f'------------------------- \n')
    txt_file.write(f'Winner: {winner_name} \n')
    txt_file.write(f'-------------------------')


# Data sources:
# https://thepythonguru.com/python-string-formatting/
