import os
import bank_statement_parser

from apiclient import discovery
from google.oauth2 import service_account

try:
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets",
              "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    print(secret_file)
    spreadsheet_id = '1vP1Pqq89b6Mjgsg7sPi_9rSa0H8Yn3XNhyRFwTFj1Ig'
    summary_sheet_expenses_planned = 'Summary!D28:D40'
    transaction_expenses_amount = 'Transactions!B5:E30'
    transaction_income_amount = 'Transactions!G5:J30'


    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    # values = [
    #     ['mm', '3224', 'tv i bought', ''],
    #     ['dATe', '23432', '4134']
    #     ['date', 'amount', 'desc', 'categor']
    # ]

    expenses = bank_statement_parser.get_transactions_list()[0]
    income = bank_statement_parser.get_transactions_list()[1]


    expenses_data = {
        'values': expenses
    }

    income_data = {
        'values': income
    }

    # Expenses
    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=expenses_data, range=transaction_expenses_amount,
                                           valueInputOption='USER_ENTERED').execute()
    # Income
    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=income_data, range=transaction_income_amount,
                                           valueInputOption='USER_ENTERED').execute()

    # print(summary_sheet_expenses_planned.)

except OSError as e:
    print(e)

except TypeError:
    print("value in cells should be integers")
