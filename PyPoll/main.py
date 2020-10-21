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
    dec_C = (candidate_C / votes)
    pct_C = "{:3%}".format(dec_C)

    dec_K = candidate_K / votes
    pct_K = "{:3%}".format(dec_K)

    dec_L = candidate_L / votes
    pct_L = "{:3%}".format(dec_L)

    dec_O = candidate_O / votes
    pct_O = "{:3%}".format(dec_O)

    # print out all the important information
    print("Here are the election results:")
    print("-------------")
    print(f"There were a total of {votes} votes casted in this election.")
    print("-------------")
    print(f"Correy received {candidate_C} total votes, or {pct_C}.")
    print(f"Khan received {candidate_K} votes, or {pct_K}.")
    print(f"Li received {candidate_L} votes, or {pct_L}.")
    print(f"O'Tooley received {candidate_O} votes, or {pct_O}.")
    print("-------------")

    # print the winner of the election
    if candidate_C > candidate_K and candidate_L and candidate_O:
        winner = 'Correy'
    if candidate_K > candidate_C and candidate_L and candidate_O:
        winner = 'Khan'
    if candidate_L > candidate_C and candidate_K and candidate_O:
        winner = 'Li'
    if candidate_O > candidate_C and candidate_K and candidate_L:
        winner = "O'Tooley"
    print(f"And the winner of the election is {winner}! Congratulations {winner}, and good job to the other candidates!")