import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print (csvreader)
    next(csvreader)
    count = 0
    months = 0
    sum = 0

    # print the csv file and the number of months on report
    for row in csvreader:
        print(row)
        count += 1 

        # calculate the number of months on report
        months += 1

        # calculate the average of changes on report
        # create a new list that contains all the changes
        for monthly_changes in row:
            monthly_changes = []

    print(f"There are {months} months on this budget data.")
    print(f"The net total of the company is ${sum}.")

    # calculate average change over entire time


    # find month with greatest profit over entire time


    # find month with greatest loss over entire time


    # print the results of everything
    