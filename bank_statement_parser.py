import os
import pandas as pd

bank_statement_path = os.path.join(os.getcwd(), 'bank_statement.xls')
df = pd.read_excel(bank_statement_path,header=None)


# print(df.shape[1])

for row in range(df.shape[0]):

    for col in range(df.shape[1]):

        if df.iat[row, col] == 'Date':
            date_dimensions = (row,col)
        elif df.iat[row, col] == 'Amount':
            amount_dimensions = (row,col)
        # elif df.iat[row, col] == 'Description':
        #     desc_dimensions = (row,col)
        # else row_start


# print(date_dimensions)
# # print(desc_dimensions)
# print(amount_dimensions)
# #  df.shape   returns a tuple dimensions of df  (row, col)
#
# print(df.loc[5,3])

for row in range(amount_dimensions[0] + 1, df.shape[0]):
    print(df.loc[row, amount_dimensions[1]])

# Example of reading 'Amount' Column
# start row from (amount_dimensions[0], df.shape[0])




# get first sheet in workbook
# sheet = wb.sheet_by_index(0)

# sheet_row_TEST = sheet.row(7)
# specific_cell_TEST = sheet.cell_value(7,2)
# row_len_TEST = sheet.row_len(7)

# For row 0 and column 0
# sheet.cell_value(0, 0)

# for i in range(sheet.ncols):
#     print(sheet.cell_value(7,i))

# for i in range(sheet.nrows):
#     print(sheet.cell_value(i, 1))

# for i in range(sheet.nrows):
#     for j in range(sheet.ncols):
#         print(sheet.cell_value(i, j))
