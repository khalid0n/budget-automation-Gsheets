import os
import pandas as pd
from utils import parse_transaction_date, is_negative

bank_statement_path = os.path.join(os.getcwd(), 'bank_statement.xls')
df = pd.read_excel(bank_statement_path, header=None)
date_dimensions = ''
amount_dimensions = ''
desc_dimensions = ''

# print(df.shape)     #(25, 10)



for row in range(df.shape[0]):
    for col in range(df.shape[1]):
        if df.iat[row, col] == 'Date':
            date_dimensions = (row, col)
        elif df.iat[row, col] == 'Amount':
            amount_dimensions = (row, col)
        elif df.iat[row, col] == 'Description ':
            desc_dimensions = (row, col)
    if date_dimensions and amount_dimensions and desc_dimensions:
        # print("found them all")
        break

# print(df.head())


# print(desc_dimensions)
# #  df.shape   returns a tuple dimensions of df  (row, col)



# from YYYY-MM-DD  to   M/D/YYYY


def get_transactions_list():
    single_transaction = []
    transactions = []
    for row in range(date_dimensions[0] + 1, df.shape[0]):
        single_transaction.clear()
        if parse_transaction_date(df.loc[row, date_dimensions[1]]) is None:
            continue
        single_transaction.insert(0, parse_transaction_date(df.loc[row, date_dimensions[1]]))
        single_transaction.insert(1, df.loc[row, amount_dimensions[1]])
        single_transaction.insert(2, df.loc[row, desc_dimensions[1]])
        single_transaction.insert(3, 'testCateg')
        # print(single_transaction)
        transactions.append(single_transaction.copy())
    return transactions

print(get_transactions_list())


# for row in range(amount_dimensions[0] + 1, df.shape[0]):
#     print(df.loc[row, amount_dimensions[1]])
#
# for row in range(desc_dimensions[0] + 1, df.shape[0]):
#     print(df.loc[row, desc_dimensions[1]])

# Example of reading 'Amount' Column
# start row from (amount_dimensions[0], df.shape[0])

# def get_transaction_values():
#     transactions = []
#
#

#
# class Transaction:
#     def __init__(self):
#
