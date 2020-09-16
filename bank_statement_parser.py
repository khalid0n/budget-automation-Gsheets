import os
import pandas as pd
from utils import parse_transaction_date

bank_statement_path = os.path.join(os.getcwd(), 'bank_statement.xls')
df = pd.read_excel(bank_statement_path,header=None)


# print(df.shape)     #(25, 10)

for row in range(df.shape[0]):
    for col in range(df.shape[1]):
        if df.iat[row, col] == 'Date':
            date_dimensions = (row,col)
        elif df.iat[row, col] == 'Amount':
            amount_dimensions = (row,col)
        elif df.iat[row, col] == 'Description':
            desc_dimensions = (row,col)
        # else row_start


# print(date_dimensions)
# # print(desc_dimensions)
# print(amount_dimensions)
# #  df.shape   returns a tuple dimensions of df  (row, col)
#
# print(df.loc[5,3])


for row in range(date_dimensions[0] + 1, df.shape[0]):
    print(df.loc[row, date_dimensions[1]])

# Example of reading 'Amount' Column
# start row from (amount_dimensions[0], df.shape[0])

def get_transaction_values():
    transactions = []



#
# class Transaction:
#     def __init__(self):
#

