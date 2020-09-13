import os
import httplib2

from apiclient import discovery
from google.oauth2 import service_account


try:
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    spreadsheet_id = '1vP1Pqq89b6Mjgsg7sPi_9rSa0H8Yn3XNhyRFwTFj1Ig'
    summary_sheet_expenses_planned = 'Summary!D28:D40'
    print(summary_sheet_expenses_planned)

except OSError as e:
    print(e)




