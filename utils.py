import datetime


# YYYY-MM-DD  to   M/D/YYYY
def parse_transaction_date(date):
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    new_date = '{0}/{1}/{2}'.format(new_date.month, new_date.day, new_date.year)
    return new_date
