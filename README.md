# Election Audit

## Table of Contents

- [Overview of Election Audit](#overview-of-election-audit)
- [Election Results](#election-results)
  * [Votes by County](#votes-by-county)
  * [Votes by Candidate](#votes-by-candidate)
  * [Text Output](#text-output)
- [Election Audit Summary](#election-audit-summary)

## Overview of Election Audit

The purpose of this audit is to assist a Colarado Board of Election employee (hereby known as "client") in determining the winner of an election in the US Congresional Precinct in Colarado. The client has requested the audit be done in python rather than excel so determining the winner is automated.

The votes from three counties in the state, Jefferson, Denver and Arapahoe, were tabulated and provided by the client. Please refer to `Resources/election_results.csv` to find the full data used in the audit. The client had also requested that the county with th highest voter turnout should be one of the outputs.

The candidates for the election are:
1. Charles Casper Stockham
2. Diana DeGette
3. Raymon Anthony Doane

## Election Results

*Please Note: `PyPoll_Challenge.py` holds the code used for the audit. Please reference file for full code.*

Prior to starting the audit, the goals for the code were noted at the beginning, as shown in the code block below, so as the help the client and all thrird parties have basic understanding of the code outline. 

```
# Open the data file.
# Get the total votes cast for the election.
# Write down the names of all the candidates and counties.
# Add a vote count for each candidate and county.
# Get the voter turnout for each county
# Get the total votes for each candidate.
# Determine the county with highest voter turn out
# Determine the winner fo the election
# -------------------------------------------------
```

The first course of action was to determine the total amount of votes casted for the election. Python found the total amounts of votes to be `369,711`.

### Votes by County

The total votes by county and it's percentage in respect to total votes are shown in the table below

| County Name | County Votes | % Vote |
| ----------- | :----------: | ------ |
| Jefferson | 38,855 | 10.5% |
| Denver  | 306,055 | 82.8% |
| Arapahoe | 24,801 | 6.7% |

The audit showed **Denver County** had a significant voter turnout almost overshadowing the other counties with over 80% of the votes coming from that county. This maybe due to many factors such as population size, but it is obvious the people of Denver were the true deciding vote for the elections.

### Votes by Candidate

The total votes by candidate and their percentage vote in respect to total votes are shown in the table below

| Candidate Name | Candidate Votes | % Vote |
| -------------- | :-------------: | ------ |
| Charles Casper Stockham | 85,213 | 23.0% |
| Diana DeGette  | 272,892 | 73.8% |
| Raymon Anthony Doane | 11,606 | 3.1% |

The table shows the obvious winner of the election to be **Candidate Diana DeGette** who won by a landslide with over 70% of the votes.

### Text Output

The client requested the election results be outputted into a `.txt` file for those in management who may not have access to python. All outputs printed out into the terminal were also printed out into the `election_results.txt` which can be found in the `analysis` folder. For reader ease, the output has been provided as an image shown below.

<img width="296" alt="election_results" src="https://user-images.githubusercontent.com/86085601/125560566-b02f86bd-638d-4b0b-bbe2-07f4028c14ec.png">

## Election Audit Summary

Conduting election audit can be very tasking and time consuming. Fortunately, the code used for this particular election audit can be used for other election data. However, it is important that the following notes are taken into account to make use of the `PyPoll_Challenge`

- It is **_very important_** the following code is at the top of the file:
```
import csv
import os
```
- The election data file must be put in the `Resources` folder. The `Resources` folder should also be in the same folder the `PyPoll_Challenge.py` file, if not the code wouldn't run.
    - It would be best practice to have the file with the raw data named `election_results.csv`. If not possible, please change the following from `election_results.csv` to whatever the name of the file that has the raw data is
    ```
    # Variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
    ```
- The file used for this audit had **County name** in *index 1* (i.e. column 2) and **Candidate name** in *index 2* (i.e. column 3). If the new election data is not in this format, please make the proper changes to the following code.
```
# Print each row in the CSV file.
for row in file_reader:
.
.
.
    # County name index
        county_name = row[1]
.
.
.
    # Candidate name index
        candidate_name = row[2]
```
- Please create an `analysis` folder in the same folder the `PyPoll_Challenge.py` file is in. This would help with the outpu showing the results. In the current code, it would be named `election_results.txt`.
- If the election is done by state, everywhere `county` shows up in the code can be changed to `state` as long as the index is changed as per bullet point 3.
    - It is important the following code should also be changed for the sake of the output
    ```
    # Output winning candidate
    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
    print(winning_county_summary)
    # Save winning candidate to text file
    txt_file.write(winning_county_summary)
    ```

With this, the code should be of use for furture audits.

