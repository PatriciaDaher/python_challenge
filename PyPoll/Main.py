# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("..", "PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  
cand_votes = {} 

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row (assuming candidate's name is in the second column)
        cand_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if cand_name not in cand_votes:
            cand_votes[cand_name] = 0  

        # Add a vote to the candidate's count
        cand_votes[cand_name] += 1
print(f" Election Results\n-------------------------------------------")
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}\n-------------------------------------------")

    txt_file.write(f"Total Votes: {total_votes}\n")

    # Initialize variables to track the winning candidate
    win_cand = ""
    win_count = 0

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in cand_votes.items():
        # Calculate the percentage of votes
        vote_percentage = (votes / total_votes) * 100

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

        # Update the winning candidate if this one has more votes
        if votes > win_count:
            win_count = votes
            win_cand = candidate

    # Generate and print the winning candidate summary
    print("-------------------------------------------")
    win_percent = (win_count / total_votes) * 100
    print(f"Winner: {win_cand} with {win_percent:.3f}% ({win_count})")
    print("-------------------------------------------")
    txt_file.write(f"Winner: {win_cand} with {win_percent:.3f}% ({win_count})\n")
