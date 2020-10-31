# Q1: Create a Pandas dataframe with 3 columns: User, Fruit and Quantity.
# Insert Junaid, Tom, Dick, Harry as Users. 
# Insert Apple, Oranges, Bananas, Mango as Fruit
# Insert 4, 3, 11, 7 as Quantity
# Each user should have their own row, this table should have 4 rows, you may name this dataframe what you like.
import pandas as pd
import numpy as np

df = pd.DataFrame({'Users': ['Junaid', 'Tom', 'Dick', 'Harry'], 'Fruit' : ['Apple', 'Oranges', 'Bananas', 'Mango'], 'Quantity': [4,3,11,7]})
df

# Q2: Read in the transactions CSV file into Python, call this df and print the first 5 rows
df = pd.read_csv('transactions.csv')
df.head(5)

# Q3: List the column names in the df dataframe. Express the answer as a list
list(df.columns)

# Q4: Count the number of rows in the dataframe
len(df)

# Q5: How many unique customer ids do we have?
len(df['customer_id'].unique())

# Q6: What is the minimum value, maximum value, mean value and median value for the price column
df['price'].describe()

# Q7: Filter the dataframe so that only the transactions for customer_id 'ABC' are returned. Call this ABC_df
ABC_df = df[(df.customer_id == 'ABC')]

# Q8: Filter the dataframe so that only the transactions with quantity more than 10 are returned and occurred later than the 1st of January
df[(df.quantity > 10) & (df.date >= '02/01/2020')]

# Q9: How many rows are there in df where the price more than £10? Note: Pounds only, ignore the pence
len(df[df.price > 10])

# Q10: Add a new column to df where you multiply price and quantity - call this revenue
df['revenue'] = df['price']*df['quantity']

# Q11: Add a new column to df where you report the price in pounds only E.g. 12.05 becomes 12. Round up to the nearest pound - call this price_pounds. Hint: look up ceiling function
import math
df['price_pound'] = df['price'].apply(math.ceil)

# Q12: Create an indicator column where True marks if the quantity is a multiple of 2 and False otherwise - call this quantity_indicator Hint: Look at Numpy Select and or Lambda functions
df['quantity_indicator'] = df['quantity'].apply(lambda x: x % 2 == 0)

# Q13: Sort the dataframe df in ascending order according the price
df.sort_values(by = ['price'])

# Q14: Sort the dataframe df in ascending order according the price and descending order by date
df.sort_values(by = ['price', 'date'], ascending = [True, False])

# Q15: Rename all the columns in the table where the first character of every column name has a capital letter as its first letter
df.columns = ['Transaction_id', 'Date', 'Customer_id', 'Price', 'Quantity', 'Revenue', 'Price_pound', 'Quantity_indicator']

# Q16: Compute the total revenue by customer id and order this grouped table by descending revenue
df.groupby(['Customer_id'], as_index = False).agg({'Revenue': 'sum'}).sort_values(by = 'Revenue', ascending = False)

# Q17: For each day list the 2 top spending customer ids
daily_spenders = df.groupby(['Date', 'Customer_id'], as_index = False).agg({'Revenue': 'sum'}).sort_values(by = ['Date', 'Revenue'], ascending = [True, False])
daily_spenders.groupby('Date').head(2)

# Q18: What is the mean Quantity sold by day?
df.groupby(['Date'], as_index = False).agg({'Quantity': 'mean'})