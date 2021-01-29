# market_palce_for_loans
Design a marketplace for loans. In this marketplace, different lenders sell and buy loans. Buying a loan is an auction process where buyer bids the participating amount and the percentage of participating amount at which he wants to buy a loan. The participating amount must be less than or equal to the original loan amount. Loan will not be closed on platform until the entire loan amount is sold

# How to run the program?
python loan_market_place.py

# sample output
py .\loan_market_place.py

Enter your value:

200
Enter your partiiation:

100 90 30 30 80 100

Enter your percentages:

99 100 99 98.9 100 99

max amount for the seller is: 199.7
indeces for seller max profit: [1, 4, 2]

# Problem statement analysis
1) lenders should be able to BUY & SELL loans in the marker place
2) Buying a loan --> auction process --> buyer bids participating amount & percentage of participating amount

# constraints
1) The participating amount must be less than or equal to the original loan amount --> handled
2) Loan will not be closed on platform until the entire loan amount is sold --> handled
3) sell loan in max 3 parts(bids) --> handled

# Requirement analysis
1) Max profit for the seller 
2) given input --> loan amount from seller, particiaption amount array and percentages array
3) output --> indeces of the participations that giove the max profit to seller 

# Assumptions 
1) percentages would be less than 100
2) all the values enterd are non-negative

These assumptions are made to focus on the logic instaed of complicating the constraints verification logic

# test cases
### 1) different participation amount & percentage lengths 
200 

100 90 30 200 80 100

99 100 99 98.9 100 

out: enter valid values

### 2) Emtpy loan amount or participation or percentages ---> not valid

## other cases
### 1) Input:

200

100 90 30 200 80 100

99 99 98 99.8 100 99

Output:
[3]

### 2) Input:

200

100 90 30 200 80 100

99 100 99 98.9 100 99

Output:
[1,2,4]

### 3) Input:

200

100 90 30 200 80 100

100 99 99 98.9 100 99

Output:
[0,5]

# Solution Analysis
#### The majot things to consider are:
1) sorting done in sortedBids() --> time : O(n*logn) ; space : O(1)
2) logic from max_seller_profit() --> time: O(n*n) ; space : O(1)

#### overall complexity : time: O(n^2) ; space : O(1)
For ret of the functions, the performance(spaec and time) is not dependent of the size of the input
Note: The space required for creating objects is ignored here . Instead of storing in 2 arrays, we are storing a single array of objects. This wouldn't effect the logic complexity. The intermediate arrays used for storing result, etc. are not proportinal to the size of the input. Hence O(1)

# Potential improvements
1) the block that compares sum of bids with max bid amount and constructing result array is repeated. This can be moved to a seperate function. Idea is not to overwhelm with many functions. So it is left like that 
2) Right now codes vlaidates the emptyness of the whole participation or percentages. Good to have the check for individual values as well
3) There is always a better solution. But it comes at cost. O(n2) can be reduced at an expense of space
4) A DEBUG flag can be passed and logging can be enabled

# code walk through 
I am NOT adding anything here on purpose. 
Ideally if the naming convenstions,code oorganization is proper and comments are appropriately used, this section wouldn't be needed.
