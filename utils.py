import datetime
import re


# from YYYY-MM-DD  to   M/D/YYYY
def parse_transaction_date(date):
    try:
        new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        new_date = '{0}/{1}/{2}'.format(new_date.month, new_date.day, new_date.year)
        return new_date
    except ValueError:
        return None


def is_negative(num):
    if re.search("-", str(num)):
        return True
    else:
        return False

