#######################################################################################################################################################
# 
# Name: Minh Anh Nguyen
# SID: 740099319
# Exam Date: Thursday March 27, 2025
# Module: Programming for Business Analytics
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-mn548
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []

sid = [7, 9] # sid: 740099319

for i in sid:
    start_location = customer_feedback.find(key_comments[i])
    end_location = start_location + len(key_comments[i])
    my_list.append((start_location, end_location))

print(my_list)
[(129, 136), (82, 87)]

# OUTPUT 
##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 19

# Write your code for Operating Profit Margin
def net_profit_margin(net_profit, total_revenue):
    if total_revenue != 0:
        net_profit_margin = (net_profit / total_revenue) * 100
    else:
        net_profit_margin = 0
    return net_profit_margin

# Write your code for Revenue per Customer
def revenue_per_customer(total_revenue, total_customers):
    if total_customers != 0:
        revenue_per_customer = total_revenue / total_customers
    else:
        revenue_per_customer = 0
    return revenue_per_customer

# Write your code for Customer Churn Rate
def customer_churn_rate(total_customers, lost_customers):
    if total_customers != 0:
        customer_churn_rate = (lost_customers / total_customers) * 100
    else:
        customer_churn_rate = 0
    return customer_churn_rate

# Write your code for Average Order Value
def average_order_value(total_revenue, total_orders):
    if total_orders != 0:
        average_order_value = total_revenue / total_orders
    else:
        average_order_value = 0
    return average_order_value

# Call your designed functions here
value1 = 74
value2 = 19
print (net_profit_margin(value1, value2))
print (revenue_per_customer(value1, value2))
print (customer_churn_rate(value1, value2))
print (average_order_value(value1, value2))

# OUTPUT
389.4736842105263
3.8947368421052633
25.675675675675674
3.8947368421052633

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
# Write your code here
# Importing necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Demand and Price Data
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

model = LinearRegression()
model.fit(prices, demand)

m = model.coef_[0]
b = model.intercept_

optimal_price = -b/(2*m)

demand_at_52 = model.predict([[52]])[0]

print(f"Optimal price: £{optimal_price:.2f}")
print(f"Predicted demand at £52: {demand_at_52:.0f} units")

# OUTPUT
Optimal price: £44.55
Predicted demand at £52: 173 units

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()

# Debug the code and provide comments on the errors identified and corrections made.

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: ")) # Corrected interger () by int() to convert input to integer
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markeredgecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue') # Corrected markercolor to markeredgecolor, lable to label (typo error)
plt.title("Line Chart of 100 Random Numbers") # Corrected missing quotation marks
plt.xlabel("Index") # Corrected = to () to set xlabel and ylabel
plt.ylabel("Random Number") # Corrected = to () to set xlabel and ylabel
plt.legend() # Corrected '---' to () to show legend
plt.grid(True)
plt.show()

