import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print (csvreader)
    next(csvreader)
    count = 0
    votes = 0

    # print the csv file and the number of votes on report
    for row in csvreader:
        #print(row)
        count += 1 

        # calculate the number of votes on report
        votes += 1

        # print all of the candidates that received a vote

        # tally up the total votes for each candidate

        # calculate the percentage of vote that each candidate received

    print(f"There are {votes} total votes on this election data.")

        # print the winner of the election