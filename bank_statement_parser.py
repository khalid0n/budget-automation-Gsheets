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



lss = [['9/1/2020', '-77.2',
        'Credit Card Settlement at INTERNET BANKING RIB, ,  Credit Card  520431xxxxxx6705,  Reference :SD1297348,  Transaction Time :14:15:14',
        'testCateg'], ['9/1/2020', '-22.00',
                       'Credit Card Settlement at INTERNET BANKING RIB, ,  Credit Card  520431xxxxxx6705,  Reference :SD1300444,  Transaction Time :14:18:56',
                       'testCateg'], ['9/1/2020', '-67.00',
                                      'E-Commerce Purchase : 601001210, jahez, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  67 Rate: 1,  Charges : SAR 0.00, Transaction Time : 15:15:03 ,Reference : SD1357003',
                                      'testCateg'],
       ['9/1/2020', '4580.00', 'Transfer via anbnetOwn Account Transfer -ANB', 'testCateg'], ['9/2/2020', '-334.3',
                                                                                              'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 451904220030, TAMIMI MARKETS  S160, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  334.3 Rate: 1,  Charges : SAR 0.00, Transaction Time : 10:31:10',
                                                                                              'testCateg'],
       ['9/2/2020', '-15.25',
        'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 801578000450, Aldawaa PH-243, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  15.25 Rate: 1,  Charges : SAR 0.00, Transaction Time : 10:40:38',
        'testCateg'],
       ['9/3/2020', '6,828.27', 'شركةالاتصالات السعودية رواSABBREM2024600PE   SARNB20246000003رواتب شركة الاتصالات الس',
        'testCateg'], ['9/5/2020', '-210.09', 'SADAD Saudi Telecom Internet051049485391309633835', 'testCateg'],
       ['9/5/2020', '-228.15', 'SADAD Saudi Telecom Internet020200101611309633839', 'testCateg'],
       ['9/5/2020', '-330.00', 'RIB2040886176/ANB 0108062734750034KHALED NASSER R AL SAHALI0108062734750034',
        'testCateg'], ['9/5/2020', '-4000.00',
                       'ATM Cash withdrawal at OP0101ND01055812, RIYADH,  mada Card  XXXXXXXXXXXX4750,  Amount:  4000 SAR,  Rate: 1,  Reference: SD5921264, Transaction Time: 20:45:15',
                       'testCateg'], ['9/6/2020', '-84.39',
                                      'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 451906160013, TAMIMI MARKETS  S160, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  84.39 Rate: 1,  Charges : SAR 0.00, Transaction Time : 11:19:43',
                                      'testCateg'], ['9/7/2020', '-81.08',
                                                     'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 100100045143, ANWAR AL LULU RESTAU, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  81.08 Rate: 1,  Charges : SAR 0.00, Transaction Time : 22:41:44',
                                                     'testCateg'], ['9/8/2020', '-1150.00',
                                                                    'Outgoing Transfer-SARIE at INTERNET BANKING RIB,  Beneficiary:مرام ناصر السهلي,  Beneficiary Bank:بنك الإنماء, Charges:0.00,  Reference:SD8542522,Transaction Time :13:00:15',
                                                                    'testCateg'], ['9/8/2020', '-2200.00',
                                                                                   'ATM Cash withdrawal at OP0101ND01055812, RIYADH,  mada Card  XXXXXXXXXXXX4750,  Amount:  2200 SAR,  Rate: 1,  Reference: SD8818680, Transaction Time: 18:55:54',
                                                                                   'testCateg'], ['9/8/2020', '-101.00',
                                                                                                  'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 771100093986, ALI OMAR ALJADI EST, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  101 Rate: 1,  Charges : SAR 0.00, Transaction Time : 19:18:01',
                                                                                                  'testCateg'],
       ['9/9/2020', '-83.95',
        'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 201017538085, Motor Vehicles Perio, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  83.95 Rate: 1,  Charges : SAR 0.00, Transaction Time : 09:02:34',
        'testCateg']]

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
