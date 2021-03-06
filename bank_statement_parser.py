import os
import pandas as pd
from utils import parse_transaction_date, is_negative

bank_statement_path = os.path.join(os.getcwd(), 'bank_statement.xls')
df = pd.read_excel(bank_statement_path, header=None)
date_dimensions = ''
amount_dimensions = ''
desc_dimensions = ''

# to find the coordinates (head) of each column
for row in range(df.shape[0]):
    for col in range(df.shape[1]):
        if df.iat[row, col] == 'Date':
            date_dimensions = (row, col)
        elif df.iat[row, col] == 'Amount':
            amount_dimensions = (row, col)
        elif df.iat[row, col] == 'Description ':
            desc_dimensions = (row, col)
    if date_dimensions and amount_dimensions and desc_dimensions:
        break


def get_transactions_list():
    single_transaction = []  # [date, amount, description, category]
    transactions = []
    expenses = []
    income = []
    for row in range(date_dimensions[0] + 1, df.shape[0]):
        single_transaction.clear()
        if parse_transaction_date(df.loc[row, date_dimensions[1]]) is None:
            continue  # skip row if no date provided

        if not is_negative(df.loc[row, amount_dimensions[1]]):
            single_transaction.insert(0, parse_transaction_date(df.loc[row, date_dimensions[1]]))
            single_transaction.insert(1, df.loc[row, amount_dimensions[1]])
            single_transaction.insert(2, df.loc[row, desc_dimensions[1]])
            single_transaction.insert(3, 'testCateg')
            income.append(single_transaction.copy())    # positive transaction, so addition will be in Income
        else:
            single_transaction.insert(0, parse_transaction_date(df.loc[row, date_dimensions[1]]))
            single_transaction.insert(1, df.loc[row, amount_dimensions[1]])
            single_transaction.insert(2, df.loc[row, desc_dimensions[1]])
            single_transaction.insert(3, 'testCateg')
            expenses.append(single_transaction.copy())  # negative transaction, so addition will be in expense
    transactions.insert(0, expenses)
    transactions.insert(1, income)
    return transactions


