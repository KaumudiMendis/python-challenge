# Creating a Python script that analyzes the records to calculate each of the following:

import os
import csv

#Creations of variables
Input_file="PyBank/PyBank_Resources/budget_data.csv"
Output_file="PyBank/PyBank_Analysis/PyBank_Budget_Analysis.txt"
Total_months=0

Input_file = os.path.join('..', 'PyBank', 'PyBank_Resources', 'budget_data.csv')
Output_file=os.path.join("..", 'PyBank', 'PyBank_Analysis', 'PyBank_Budget_Analysis.txt')


with open(Input_file) as PyBank_Revenue:
    
    # Input_file_reader specifies delimiter and variable that holds contents
    Input_file_reader = csv.reader(PyBank_Revenue, delimiter=',')   
    
    Input_file_header = next(PyBank_Revenue)
    
    #The total number of months included in the dataset 
    
    for row in Input_file_reader:    
        Total_months=Total_months+1
    
    
#The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:



Analysis_output=(
    f"\nFinancial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {Total_months}\n")
#   f"Total: ${Grand_Total}\n"
#  f"Average Change: ${Avarage_Change}\n"
#    f"Greatest Increase in Profits:{greatest_increase[0]}(${greatest_increase[1]}\n"
#    f"Greatest Increase in Profits:{greatest_decrease[0]}(${greatest_decrease[1]}\n"
    

#Print the Analysis to Terminal.
print(Analysis_output)
    
#Export text file with the result.
with open(Output_file, 'w') as Print_to_Text_file:
        Print_to_Text_file.write(Analysis_output)
    