import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print (csvreader)
    next(csvreader)

    # initialize variables and lists
    count = 0
    months = 0
    total_profits = 0
    profit_list = []

    # print the csv file and the number of months on report
    for row in csvreader:
        print(row)
        count += 1 

        # calculate the number of months on report
        months += 1

        # calculate the total profit/loss, and store on a list
        total_profits += int(row[1])
        profit_list.append(int(row[1]))

        # calculate the average of changes on report
    profit_changes = []
    for i in range((months)-1):
        profit_changes.append((profit_changes[i+1])-(profit_list[i]))

    print(f"There are {months} months on this budget data.")
    print(f"The net total of the company is ${total_profits}.")

    # calculate average change over entire time


    # find month with greatest profit over entire time


    # find month with greatest loss over entire time


    # print the results of everything
    