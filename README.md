# Election Audit

## Table of Contents

- [Overview of Election Audit](#overview-of-election-audit)
- [Election Audit](#election-audit)
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

Please Note: `PyPoll_Challenge.py` holds the code used for the audit. Please reference file for full code.

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

The first course of action was to determine the total amount of votes casted for the election. Python found the total amounts of votes to be 369,711.

### Votes by County

The total votes by county and it's percentage in respect to total votes are shown in the table below

| County Name | County Votes | % Vote |
| ----------- | ------------ | ------ |
| Jefferson | 38,855 | 10.5% |
| Denver  | 306,055 | 82.8% |
| Arapahoe | 24,801 | 6.7% |

### Votes by Candidate



### Text Output



## Election Audit Summary



