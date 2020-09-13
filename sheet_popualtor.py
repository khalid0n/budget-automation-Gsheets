import os
import httplib2

from apiclient import discovery
from google.oauth2 import service_account


try:
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    spreadsheet_id = '1vP1Pqq89b6Mjgsg7sPi_9rSa0H8Yn3XNhyRFwTFj1Ig'
    summary_sheet_expenses_planned = 'Summary!D28:D40'

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    values = [
        ['42342']
    ]

    data = {
        'values': values
    }

    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=data, range=summary_sheet_expenses_planned, valueInputOption='USER_ENTERED').execute()

    # print(summary_sheet_expenses_planned.)

except OSError as e:
    print(e)

except TypeError:
    print("value in cells should be integers")




