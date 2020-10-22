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
    dec_C = float((candidate_C / votes) * 100)
    dec_C = round(dec_C, 2)

    dec_K = float((candidate_K / votes) * 100)
    dec_K = round(dec_K, 2)

    dec_L = float((candidate_L / votes) * 100)
    dec_L = round(dec_L, 2)

    dec_O = float((candidate_O / votes) * 100)
    dec_O = round(dec_O, 2)

    # print out all the important information
    #print(candidates)
    print("Here are the election results:")
    print("-------------")
    print(f"There were a total of {votes} votes casted in this election.")
    print("-------------")
    print(f"Correy received {candidate_C} total votes, or {dec_C}%.")
    print(f"Khan received {candidate_K} votes, or {dec_K}%.")
    print(f"Li received {candidate_L} votes, or {dec_L}%.")
    print(f"O'Tooley received {candidate_O} votes, or {dec_O}%.")
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

# create the exporting text file
text_file = os.path.join("Analysis", "poll.txt")

# create and open new text file in read mode
with open(text_file, "w") as txtfile:
    txtfile.write("Here are the election results:" "\n")
    txtfile.write("--------------" "\n")
    txtfile.write(f"There were a total of {votes} votes casted in this election." "\n")
    txtfile.write("--------------" "\n")
    txtfile.write(f"Correy received {candidate_C} total votes, or {dec_C}%." "\n")
    txtfile.write(f"Khan received {candidate_K} votes, or {dec_K}%." "\n")
    txtfile.write(f"Li received {candidate_L} votes, or {dec_L}%." "\n")
    txtfile.write(f"O'Tooley received {candidate_O} votes, or {dec_O}%." "\n")
    txtfile.write("-------------" "\n")
    txtfile.write(f"And the winner of the election is {winner}! Congratulations {winner}, and good job to the other candidates!")