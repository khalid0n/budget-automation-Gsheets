import os
import bank_statement_parser
import json
from apiclient import discovery
from google.oauth2 import service_account

try:
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets",
              "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    with open('config.json') as config_file:
        json_data = json.load(config_file)
        spreadsheet_id = json_data["sheetId"]

    expenses_cell_range = 'Transactions!B5:E1000'
    income_cell_range = 'Transactions!G5:J1000'

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    expenses = bank_statement_parser.get_transactions_list()[0]
    income = bank_statement_parser.get_transactions_list()[1]

    expenses_data = {
        'values': expenses
    }

    income_data = {
        'values': income
    }

    # Expenses
    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=expenses_data, range=expenses_cell_range,
                                           valueInputOption='USER_ENTERED').execute()
    # Income
    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=income_data, range=income_cell_range,
                                           valueInputOption='USER_ENTERED').execute()

except OSError as e:
    print(e)

except TypeError:
    print("value in cells should be integers")
