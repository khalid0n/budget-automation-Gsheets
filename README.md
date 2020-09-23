# Budget Automation with Google Sheets Template
First Project in Python 😄

Automated Monthly Budget Tracking (expenses, income) with Google Sheet template.
the idea is the following:
1. read from your bank statement using [pandas](https://pandas.pydata.org/), fetch transaction values
2. populate these info to a monthly budget sheet on said values.

### Why ?
suppose you want to track your monthly budget. you would -probably- manually log every transaction which can be a tedious task.


### Budget Template Overview
you can find Monthly budget template in [spreadsheet template gallery](https://docs.google.com/spreadsheets/u/0/?ftv=1&folder=0ACoSgW1iveL-Uk9PVA).

here's a short [YouTube video](https://youtu.be/yfGmQl0Sn4c?t=30) to explain how template works

As of now, Automation Processing will be done in **Transactions** sheet



## Steps
- Create your Google Spreadsheet Template, add your *sheet Id* from url to `config.json` 
- `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
- extract your bank statement *in xls format to same dir*. name should be "bank_statement.xls"
#### Auth for Google Spreadsheet
- Create a project in [Google Developer Console](https://console.developers.google.com/) & add [Google Sheets API](https://developers.google.com/sheets/api)
- create service account key from *credentials*
- Role should be **Project > Editor**
- save the resulting private key as JSON. name it "client_secret.json"
- on your Google Sheet, click **share** button. add the *mail* from `client_secret.json`
- run `budget.py


## Limitations
in Transactions sheet, after populating them through the file. You need to manually change the category of each transaction 😄

## Demo
![Demo](demo.gif)

