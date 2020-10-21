import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

# open the csv file and initialize variables
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print (csvreader)
    next(csvreader)
    votes = 0
    candidates = []
    candidate_C = 0
    candidate_K = 0
    candidate_L = 0
    candidate_O = 0
    

    # begin gathering information from csv reader
    for row in csvreader:

        # calculate the number of votes on report
        votes += 1

        # create a list of all candidates
        if row[2] not in candidates:
            candidates.append(row[2])

        # tally up the total votes for each candidate
        if row[2] == 'Correy':
            candidate_C +=1
        if row[2] == 'Khan':
            candidate_K +=1
        if row[2] == 'Li':
            candidate_L +=1
        if row[2] == "O'Tooley":
            candidate_O +=1
        # calculate the percentage of vote that each candidate received

    print(f"There are {votes} total votes on this election data.")
    print(candidates)
    print(f"Correy received {candidate_C} votes.")
    print(f"Khan received {candidate_K} votes.")
    print(f"Li received {candidate_L} votes.")
    print(f"O'Tooley received {candidate_O} votes.")

        # print the winner of the election