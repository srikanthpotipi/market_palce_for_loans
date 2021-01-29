# market_palce_for_loans
Design a marketplace for loans. In this marketplace, different lenders sell and buy loans. Buying a loan is an auction process where buyer bids the participating amount and the percentage of participating amount at which he wants to buy a loan. The participating amount must be less than or equal to the original loan amount. Loan will not be closed on platform until the entire loan amount is sold

# How to run the program?
python loan_market_place.py

# sample output

# Problem statement analysis

# constraints
1) The participating amount must be less than or equal to the original loan amount
2) Loan will not be closed on platform until the entire loan amount is sold
3) sell loan in max 3 parts(bids)

# Requirement analysis

# Assumptions 

# test cases
## 1) different participation amount & percentage lengths 
200 
100 90 30 200 80 100
99 100 99 98.9 100 
out: enter valid values

## other cases
1) Input:
200
100 90 30 200 80 100
99 99 98 99.8 100 99
Output:
[3]

2) Input:
200
100 90 30 200 80 100
99 100 99 98.9 100 99
Output:
[1,2,4]

3) Input:
200
100 90 30 200 80 100
100 99 99 98.9 100 99
Output:
[0,5]

# Solution Analysis

# Potential improvements:
