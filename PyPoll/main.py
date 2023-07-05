import os
import csv

#------------- Reading File -------------
election_csv = os.path.join("C:\\Users\\clayt\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#------------- Declaring Variables -------------
    voteCount = 0
    candidateList = {"Candidate":[], "Votes":[]}
    var = 0
    winner = ""

#------------- Looping Through File -------------
    for row in csvreader:
        
#------------- Counting Votes -------------
        voteCount += 1
        
#------------- Recording Unique Candidates and Assigning Vote Index -------------
        if (row[2] not in candidateList["Candidate"]):
            candidateList["Candidate"].append(row[2])
            candidateList["Votes"].append(0)
            
#------------- Counting Votes per Candidate -------------
        for i in range(len(candidateList["Candidate"])):
            if candidateList["Candidate"][i] == row[2]:
                    candidateList["Votes"][i] +=1
                    
#------------- Calculating Winner -------------
    for i in range(len(candidateList["Votes"])):
         if candidateList["Votes"][i] > candidateList["Votes"][i-1]:
              winner = candidateList["Candidate"][i]
              


#------------- Printing to CMD -------------            
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {voteCount}")
    print("-------------------------")
                
#------------- Printing Info for Each Candidate in Dict -------------
    for i in range(len(candidateList["Candidate"])):
        print(f"{candidateList['Candidate'][i]}: {(candidateList['Votes'][i]/voteCount)*100:.3f}% ({candidateList['Votes'][i]})")
    
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

#------------- Writing to Text File -------------
electionResults = os.path.join("C:\\Users\\clayt\\Desktop\\python-challenge\\PyPoll\\analysis","Election Results.txt")
with open(electionResults, 'w') as f:
    f.write("Election Results \n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {voteCount}\n")
    f.write("-------------------------\n")
    for i in range(len(candidateList["Candidate"])):
        f.write(f"{candidateList['Candidate'][i]}: {(candidateList['Votes'][i]/voteCount)*100:.3f}% ({candidateList['Votes'][i]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------")    

 

