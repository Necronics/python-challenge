import os
import csv

#------------- Reading File -------------
budget_csv = os.path.join("C:\\Users\\clayt\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#------------- Declaring Variables -------------    
    monthCounter = 0
    totalAmount = 0
    prevRow = 0
    currentRow = 0
    change = 0
    totalchange = 0
    biggestIncrease = 0
    biggestIncreaseMonth = ""
    biggestDecrease = 0
    biggestDecreaseMonth = ""

#------------- Looping Through File -------------
    for row in csvreader:
        
#------------- Counting Months -------------
        monthCounter += 1
                
#------------- Calculating Total Profit/Loss -------------
        totalAmount += int(row[1])
                
#------------- Calculating Monthly Change -------------
        prevRow = currentRow
        currentRow = int(row[1])
        change = currentRow - prevRow
                
#------------- Calculating Total Change Exclucing First Row -------------
        if (monthCounter>1):
            totalchange += change
                    
#------------- Assigning Greatest Increase -------------
        if(change > biggestIncrease):
            biggestIncrease = change
            biggestIncreaseMonth = row[0]
            
#------------- Assigning Greatest Decrease -------------
        if(change < biggestDecrease):
            biggestDecrease = change
            biggestDecreaseMonth = row[0]
                
#------------- Printing to CMD -------------
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {monthCounter}")
    print(f"Total: ${totalAmount}")
        
#------------- Calculating Average Change -------------
    print(f"Average Change: $ {totalchange/(monthCounter-1):.3f}")
    
    print(f"Greatest Increase in Profits: {biggestIncreaseMonth} (${biggestIncrease})")
    print(f"Greatest Decrease in Profits: {biggestDecreaseMonth} (${biggestDecrease})")

#------------- Writing to Text File -------------
budgetAnalysis = os.path.join("C:\\Users\\clayt\\Desktop\\python-challenge\\PyBank\\analysis","Budget Analysis.txt")
with open(budgetAnalysis, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {monthCounter}\n")
    f.write(f"Total: ${totalAmount}\n")
    f.write(f"Average Change: $ {totalchange/(monthCounter-1):.3f}\n")
    f.write(f"Greatest Increase in Profits: {biggestIncreaseMonth} (${biggestIncrease})\n")
    f.write(f"Greatest Decrease in Profits: {biggestDecreaseMonth} (${biggestDecrease})")
 
