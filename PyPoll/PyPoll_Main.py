# Creating a Python script that analyzes the records to calculate each of the following:

import os
import csv



Input_file = os.path.join('..', 'PyPoll', 'PyPoll_Resources', 'election_data.csv')
Output_file = os.path.join("..", 'PyPoll', 'PyPoll_Analysis', 'PyPoll_Analysis.txt')

#Creating a dictonary to find the candidate names and total vote count.

Pypoll={}
total_votes=0
candidates=[]
candidate_votes=[]
vote_percentage=[]
winner_list=[]


with open(Input_file) as election_data:
    
    # Input_file_reader specifies delimiter and variable that holds contents
    # Reading the header row
    
    reader = csv.reader(election_data, delimiter=',')   
    
    # Read the header skipping the headings
    header = next(reader)

    #Create a Dictonary to use in candidate name and vote count. 
    for row in reader: 
        total_votes=total_votes+1
        if row[2] in Pypoll.keys():
            Pypoll[row[2]] = Pypoll[row[2]] + 1
        else:
            Pypoll[row[2]]=1
#----------------------
#Create empty list for candidates and their vote count.
#Take the key values to the list.

for key, value in Pypoll.items():
    candidates.append(key)
    candidate_votes.append(value)
#    
#--------------------   
# Calculate percentage

for n in candidate_votes:
    vote_percentage.append(round(n/total_votes*100,3))

#made a touple with candidates,candidate_votes,vote_percentage.

candidate_data=list(zip(candidates,candidate_votes,vote_percentage))

#---------------
#
#find the winner create winner list

for candidate_name in candidate_data:

    if max (candidate_votes)==candidate_name[1]:
        winner_list.append(candidate_name[0])

winner = winner_list[0]
    

with open(Output_file, 'w') as txtfile:
    txtfile.writelines(f"\n___________________________\n"
        'Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in candidate_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(Output_file, 'r') as readfile:
    print(readfile.read())
    
 