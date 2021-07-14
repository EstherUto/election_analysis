# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

# -------------------------------------------------

import csv
import os

# Variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Create empty list for candidates
candidate_options = []

# Empty dictionary to assign candidate votes to candidate name
candidate_votes = {}

# County list and county votes dictionary
county_list = []
county_turnout = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest county and county votor turnout
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0

# --- LOADING election_results FILE --- #
# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1 # total_votes = total_votes + 1

        # County name index
        county_name = row[1]

        # Extracting county name
        if county_name not in county_list:
            # Add the county name to the county list.
            county_list.append(county_name)
            # Begin tracking that county's vote count.
            county_turnout[county_name] = 0

        # Candidate name index
        candidate_name = row[2]

        # Candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    
        # Add a vote to that county's count.
        county_turnout[county_name] += 1
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# ------- Save the results to text file ------- #
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    county_votes_header = ("County Votes:\n")
    print(county_votes_header)
    txt_file.write(county_votes_header)

    # Determine the percentage of votes for each county by looping through the counts.
    for county_name in county_turnout:
        # Retrieve vote count of a county.
        county_votes = county_turnout[county_name]
        # Calculate the percentage of votes.
        county_vote_percentage = float(county_votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
        print(county_results)
        #  Save the candidate results to text file.
        txt_file.write(county_results)

        # Determine winning vote count and candidate
        if (county_votes > winning_county_votes) and (county_vote_percentage > winning_county_percentage):
            winning_county_votes = county_votes
            winning_county_percentage = county_vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_county = county_name
    # Output winning candidate
    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
    print(winning_county_summary)
    # Save winning candidate to text file
    txt_file.write(winning_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #  Save the candidate results to text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # Output winning candidate
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate to text file
    txt_file.write(winning_candidate_summary)


# ---------- close files ----------- #
election_data.close()
txt_file.close()

