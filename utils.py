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


[
    [
        ['9/1/2020', '-77.2',
   'Credit Card Settlement at INTERNET BANKING RIB, ,  Credit Card  520431xxxxxx6705,  Reference :SD1297348,  Transaction Time :14:15:14',
   'testCateg'], ['9/1/2020', '-22.00',
                  'Credit Card Settlement at INTERNET BANKING RIB, ,  Credit Card  520431xxxxxx6705,  Reference :SD1300444,  Transaction Time :14:18:56',
                  'testCateg'], ['9/1/2020', '-67.00',
                                 'E-Commerce Purchase : 601001210, jahez, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  67 Rate: 1,  Charges : SAR 0.00, Transaction Time : 15:15:03 ,Reference : SD1357003',
                                 'testCateg'], ['9/2/2020', '-334.3',
                                                'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 451904220030, TAMIMI MARKETS  S160, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  334.3 Rate: 1,  Charges : SAR 0.00, Transaction Time : 10:31:10',
                                                'testCateg'], ['9/2/2020', '-15.25',
                                                               'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 801578000450, Aldawaa PH-243, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  15.25 Rate: 1,  Charges : SAR 0.00, Transaction Time : 10:40:38',
                                                               'testCateg'],
  ['9/5/2020', '-210.09', 'SADAD Saudi Telecom Internet051049485391309633835', 'testCateg'],
  ['9/5/2020', '-228.15', 'SADAD Saudi Telecom Internet020200101611309633839', 'testCateg'],
  ['9/5/2020', '-330.00', 'RIB2040886176/ANB 0108062734750034KHALED NASSER R AL SAHALI0108062734750034', 'testCateg'],
  ['9/5/2020', '-4000.00',
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
                                                                              'testCateg'], ['9/9/2020', '-83.95',
                                                                                             'POS  MADA PAY- Apple Pay  Local Transaction through machine  : 201017538085, Motor Vehicles Perio, RIYADH,  mada Card : XXXXXXXXXXXX4750,  Amount : SAR  83.95 Rate: 1,  Charges : SAR 0.00, Transaction Time : 09:02:34',
                                                                                             'testCateg']],
 [
     ['9/1/2020', '4580.00', 'Transfer via anbnetOwn Account Transfer -ANB', 'testCateg'],
  ['9/3/2020', '6,828.27', 'شركةالاتصالات السعودية رواSABBREM2024600PE   SARNB20246000003رواتب شركة الاتصالات الس',
   'testCateg']
 ]
]
