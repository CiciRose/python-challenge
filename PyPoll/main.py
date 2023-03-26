# Required modules
import os
import csv

# CSV file location
election_data = os.path.join("Resources", "election_data.csv")

# Create list to store and sort values required for calculation from CSV
ballot_ID = []
candidate = []

# Open file and assign a variable
with open(election_data) as csvfile:

    # Read file and separate the values
    csvreader = csv.reader(csvfile, delimiter=",")

    # Separate the head
    csv_header = next(csvreader)

    # Go through every row in the file
    for row in csvreader:

        # Add values to respective lists
        ballot_ID.append(row[0])
        candidate.append(row[2])

        # Calculations based on lists, grouped separately for an easier read
        total_votes = len(ballot_ID)

        charles_count = candidate.count("Charles Casper Stockham")
        diana_count = candidate.count("Diana DeGette")
        raymon_count = candidate.count("Raymon Anthony Doane")

        charles_percentage = round((charles_count/total_votes * 100), 3)
        diana_percentage = round((diana_count/total_votes * 100), 3)
        raymon_percentage = round((raymon_count/total_votes * 100), 3)

        # If statement to determine highest value among the candidates
        if charles_count > diana_count and charles_count > raymon_count:
            winner = "Charles Casper Stockham"
        elif diana_count > charles_count and diana_count > raymon_count:
            winner = "Diana DeGette"
        elif raymon_count > charles_count and raymon_count > diana_count:
            winner = "Raymon Anthony Doane"

# Print to terminal
print(f'''Election Results
------------------------------
Total Votes: {total_votes}
------------------------------
Charles Casper Stockham: {charles_percentage}% ({charles_count})
Diana DeGette: {diana_percentage}% ({diana_count})
Raymon Anthony Doane: {raymon_percentage}% ({raymon_count})
------------------------------
Winner: {winner}
------------------------------
''')

# File path to create text file
output_file = os.path.join("Analysis", "Election_Results.txt")

# Information to write into new text file
with open(output_file, "w") as results:
    results.write(f'''Election Results
------------------------------
Total Votes: {total_votes}
------------------------------
Charles Casper Stockham: {charles_percentage}% ({charles_count})
Diana DeGette: {diana_percentage}% ({diana_count})
Raymon Anthony Doane: {raymon_percentage}% ({raymon_count})
------------------------------
Winner: {winner}
------------------------------
''')
