# **ELECTION ANALYSIS**

## **Overview of Election Audit**

The purpose of this project is to audit and submit the election results to the election commission. The commisison requests that the results include total votes, percentage of the total votes  voter turnout for all candidates and counties. Based on the analysis a winner will be declared.

## **Election-Audit Results**

![Election Audit Results](/resources/election_analysis_txt.png)

	- How many votes were cast in this congressional election?
		- 369,711 Total votes were cast in the congressional elecetion.

	-Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
		- From the election results analysis, 306,055 votes were casted in Denver county representing 82.8%. Jefferson had 38,855 votes representing 10.5% and Arapahoe had 24,801 representing 6.7% of the total votes. 

	-Which county had the largest number of votes?
		- Based on the analysis of the election results, Denver county had the largest number of votes with a turnout of 306,055 representing 82.8% of the total votes cast.

	-Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
		- From the image, out of the total votes of 369,711, Raymon Anthony Doane with the least number of votes cast had 11,606 representing 3.1% of total votes count. Followed by Charles Casper Stockham with 85,213 votes representing 23% of total votes cast. Diana Degette came on top with 272,892 votes representing 73.8% of the total votes cast.

	-Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
		-Diana DeGette won the election with votes count of  272,892 representing 73.8% of the total votes cast.

## **Election-Audit Summary**

This script is structured to handle election anaylaysis being it federal,state or county elections perharps with some modidfications based on the outcome expected. For instance this script can be modified to show and track total votes cast in a state provided that information is available in the data. If state name is provided in column E, we can start tracking states = row[3] and use an if statement to count and add to each state. Also the script can be modified to to identify which county each ballot id was casted.