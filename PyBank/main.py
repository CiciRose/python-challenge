import os
import csv

# CSV file location
budget_data = os.path.join("Resources", "budget_data.csv")

# Create list to store and sort values required for calculation from the CSV
all_months = []
all_money = []

# Open file and assign a variable
with open(budget_data) as csvfile:

    # Read file and separate the values
    csvreader = csv.reader(csvfile, delimiter=",")

    # Separate the head
    csv_header = next(csvreader)

    # Go through every row in the file
    for row in csvreader:

        # Add values to respective lists
        all_months.append(row[0])
        all_money.append(float(row[1]))

        # Calculations based on lists
        total_months = len(all_months)
        total_money = sum(all_money)
        average_change = round(total_money/total_months, 2)

        # Find maximum and minimum values and their respective dates
        money_max = max(all_money)
        money_min = min(all_money)
        increase_month = all_money.index(money_max)
        decrease_month = all_money.index(money_min)

# Print to terminal
print(f'''Financial Analysis
------------------------------
Total Months: {total_months}
Total: ${total_money}
Average Change: ${average_change}
Greatest Increase in Profits: {all_months[increase_month]} (${money_max})
Greatest Decrease in Profits: {all_months[decrease_month]} (${money_min})
''')

# File path to create text file
output_file = os.path.join("Analysis", "Financial_Analysis.txt")

# Information to write into new text file
with open(output_file, "w") as results:
    results.write(f'''Financial Analysis
------------------------------
Total Months: {total_months}
Total: ${total_money}
Average Change: ${average_change}
Greatest Increase in Profits: {all_months[increase_month]} (${money_max})
Greatest Decrease in Profits: {all_months[decrease_month]} (${money_min})
''')
