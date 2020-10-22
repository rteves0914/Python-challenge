import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print (csvreader)
    next(csvreader)

    # initialize variables and lists
    months = 0
    total_profits = 0
    profit_list = []
    profit_changes = []
    date_list = []
    i = 0

    # print the csv file and the number of months on report
    for row in csvreader:
        #print(row)

        # calculate the number of months on report
        months += 1

        # calculate the total profit/loss, and store on a list
        total_profits += int(row[1])
        profit_list.append(int(row[1]))

        # store all the dates on a list
        date_list.append(str(row[0]))

    # create the list that keeps track of all the monthly changes
    for i in range((months)-1):
        profit_changes.append((profit_list[i+1])-(profit_list[i]))

    # calculate the average change per month and print it out
    average_change = round(sum(profit_changes) / (months - 1),  2)

    # find the greatest increase and decrease over the entire time period
    increase_change = max(profit_changes)
    decrease_change = min(profit_changes)

    # find the month and year that the greatest increase and decrease happened
    increase_index = profit_changes.index(increase_change) + 1
    decrease_index = profit_changes.index(decrease_change) + 1
    increase_date = date_list[increase_index]
    decrease_date = date_list[decrease_index]
    
    print("Here is the financial analysis:")
    print("--------------")
    print(f"There are a total of {months} months on this budget data.")
    print("--------------")
    print(f"The net total of the company is ${total_profits}.")
    print(f"The average change per month is ${average_change}.")
    print(f"The greatest increase in revenue is ${increase_change} and occurred in {increase_date}.")
    print(f"The greatest decrease in revenue is ${decrease_change} and occurred in {decrease_date}.")
