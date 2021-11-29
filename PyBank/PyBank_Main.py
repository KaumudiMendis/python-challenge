# Creating a Python script that analyzes the records to calculate each of the following:

import os
import csv


#Creations of variables

Input_file = os.path.join('..', 'PyBank', 'PyBank_Resources', 'budget_data.csv')
Output_file=os.path.join("..", 'PyBank', 'PyBank_Analysis', 'PyBank_Budget_Analysis.txt')


Total_months=0
Total=0
Previous_profitnloss=0
Profitnlosschange=0
Total_Profitnlosschange=0
Profitnlosschange_list=[]
Month_movement=[]
Greatest_increase=["",0]
Greatest_decrease=["",99999999999999999999999]


with open(Input_file) as Financial_data:
    
    # Input_file_reader specifies delimiter and variable that holds contents
    
    csv_reader = csv.reader(Financial_data, delimiter=',')   
    # Reading the header row
    
    csv_header = next(csv_reader)
    
    for row in csv_reader:    
    
    #The total number of months included in the dataset
        Total_months=Total_months+1

    #The net total amount of "Profit/Losses" over the entire period
        Total=Total+int(row[1])

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
   

        Profitnlosschange = int(row[1])-Previous_profitnloss
        Previous_profitnloss = int(row[1])
        Profitnlosschange_list = Profitnlosschange_list+[Profitnlosschange]
        Month_movement = Month_movement+[row[0]]
        Average_profitnlosschange = sum(Profitnlosschange_list)/len(Profitnlosschange_list)   
        
#The greatest increase in profits (date and amount) over the entire period
        if Profitnlosschange>Greatest_increase[1]:
            Greatest_increase[0]=row[0]
            Greatest_increase[1]=Profitnlosschange
            
#The greatest decrease in profits (date and amount) over the entire period
        if Profitnlosschange<Greatest_decrease[1]:
            Greatest_decrease[0]=row[0]
            Greatest_decrease[1]=Profitnlosschange


Analysis_output=(
    f"\nFinancial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {Total_months}\n"
    f"Total: ${Total}\n"
    f"Average Change: ${Average_profitnlosschange}\n"
    f"Greatest Increase in Profits:{Greatest_increase[0]}(${Greatest_increase[1]}\n"
    f"Greatest Decrease in Profits:{Greatest_decrease[0]}(${Greatest_decrease[1]}\n")
    

#Print the Analysis to Terminal.
print(Analysis_output)
    
#Export text file with the result.
with open(Output_file, 'w') as Print_to_Text_file:
        Print_to_Text_file.write(Analysis_output)
    