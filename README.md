# Election_Analysis

##  Project Overview

The Colorado Board of Elections has asked me to complete an audit of their local congressional election. I used Visual Studio Code and Python to analyze the data from the election.

**Audit Tasks**

1. Calculate the total number of votes.
  
2. Compile the list of counties where citizens voted.
  
3. Compile the list of candidates who received votes.
  
4. Calculate the total number and percentage of votes per county.
  
5. Determine the county with largest turnout.
  
6. Calculate the total number and percentage of vote per candidate.
  
7. Determine the winner of the election based on the popular vote.

## Resources

1.	Data: election_results.csv
2.	Software: Python 3.9.7, Visual Studio Code 1.64.2 

## Summary

#### Election-Audit Results:

![results](https://github.com/stephperillo/Election_Analysis/blob/main/Resources/election_results.png)

The analysis of this election shows that:

- There were 369,711 votes cast in the election.
- The candidates were:

	•	Charles Casper Stockham
  
	•	Diana DeGette
  
	•	Raymon Anthony Doane

- The candidate results were:

	•	Charles Casper Stockham received 23.0% of the vote, for a total of 85,213 votes.
  
	•	Diana DeGette received 73.8% of the vote, for a total of 272,892 votes.
  
	•	Raymon Anthony Doane received 3.1% of the vote, for a total of 11,606 votes.

- The winner of the election was:

  •	Diana DeGette 

- The voter turnout for each county was:

	•	Jefferson produced 10.5% of voters, for a total of 38,855 voters.
  
	•	Denver produced 82.8% of voters, for a total of 306,055 voters.
  
	•	Arapahoe produced 6.7% of voters, for a total of 24,801 voters.
  
- The county with the highest turnout was: 

	•	Denver, which produced 82.8% of voters, for a total of 306,055 voters.

## Election-Audit Summary

This script can be used for any election with the appropriate modifications. For example, it can easily be used for a federal election by specifying states instead of counties. It can also be used to audit and analyze state propositions by allocating the variables to the desired propositions. Instead of candidates, the analysis could examine which initiatives won in each county. With this given dataset, the script can be further modified in order to determine the percentages of votes that each candidate received in each county. Another useful addition to this script would be to add each candidate’s party affiliation (if applicable). In election reports, candidates' party affiliations are typically included. It would also be helpful to know the approximate number of voting-eligible residents in each county at the time of the election. 
