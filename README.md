# aloomasechallenge
Alooma SE Challenge

TOOLS USED
1. Python 3.6
2. PostgreSQL 10.4

WALKTHROUGH
1. Run Alooma Challenge 1.sh to install packages
2. Run Alooma Challenge 2.py to make API call, load returned JSON object into PostgreSQL DB, and determine number of days elapsed between first and last engagement
3. Run Alooma Challenge 3.py to see breakdown of total enagements by type
4. Divide total engagements by type with number of days elapsed between first and last engagement to get Engagements per Day broken down by Type (Alooma Challenge results.txt) 

ISSUES TO RESOLVE
1. Store number of days elapsed between first and last engagement as variable so it can be referenced automatically for any "per day" calculation. Currently, I have to manually read the results of the query for reference later.
2. Using real / floating data type to divide count of engagements by type with number of days elapsed between first and last engagement. Currently, the system returns an integer and it is 0 for all values because all engagements per day broken down by type are less than 1.
