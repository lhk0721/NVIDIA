import numpy as np
import pandas as pd
import re
from prettytable import PrettyTable  # 3.3.0 version 설치
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

def prinf_df(df):
    table = PrettyTable(['']+ list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    print(str(table))
    print()

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
np.set_printoptions(precision=3)


df = pd.read_excel(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\salesfunnel.xlsx')
# df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 17 entries, 0 to 16
# Data columns (total 8 columns):
#  #   Column    Non-Null Count  Dtype 
# ---  ------    --------------  ----- 
#  0   Account   17 non-null     int64 
#  1   Name      17 non-null     object
#  2   Rep       17 non-null     object
#  3   Manager   17 non-null     object
#  4   Product   17 non-null     object
#  5   Quantity  17 non-null     int64 
#  6   Price     17 non-null     int64 
#  7   Status    17 non-null     object
# dtypes: int64(3), object(5)
# memory usage: 1.2+ KB

# print(df.head())
#    Account                          Name            Rep       Manager      Product  Quantity  Price     Status
# 0   714466               Trantow-Barrows   Craig Booker  Debra Henley          CPU         1  30000  presented
# 1   714466               Trantow-Barrows   Craig Booker  Debra Henley     Software         1  10000  presented
# 2   714466               Trantow-Barrows   Craig Booker  Debra Henley  Maintenance         2   5000    pending
# 3   737550  Fritsch, Russel and Anderson   Craig Booker  Debra Henley          CPU         1  35000   declined
# 4   146832                  Kiehn-Spinka  Daniel Hilton  Debra Henley          CPU         2  65000        won

## 
pivot_table = df.pivot_table(
	index=['Manager','Rep','Product'],
	values=['Price','Quantity'],
	aggfunc=['sum','mean'],
	margins=True,
)

# print(pivot_table.index)
# MultiIndex([( 'Debra Henley',  'Craig Booker',         'CPU'),
#             ( 'Debra Henley',  'Craig Booker', 'Maintenance'),
#             ( 'Debra Henley',  'Craig Booker',    'Software'),
#             ( 'Debra Henley', 'Daniel Hilton',         'CPU'),
#             ( 'Debra Henley', 'Daniel Hilton',    'Software'),
#             ( 'Debra Henley',    'John Smith',         'CPU'),
#             ( 'Debra Henley',    'John Smith', 'Maintenance'),
#             ('Fred Anderson',   'Cedric Moss',         'CPU'),
#             ('Fred Anderson',   'Cedric Moss', 'Maintenance'),
#             ('Fred Anderson',   'Cedric Moss',    'Software'),
#             ('Fred Anderson',    'Wendy Yule',         'CPU'),
#             ('Fred Anderson',    'Wendy Yule', 'Maintenance'),
#             ('Fred Anderson',    'Wendy Yule',     'Monitor'),
#             (          'All',              '',            '')],
#            names=['Manager', 'Rep', 'Product'])

# print(pivot_table.columns)
# MultiIndex([( 'sum',    'Price'),
#             ( 'sum', 'Quantity'),
#             ('mean',    'Price'),
#             ('mean', 'Quantity')],
#            )

# print(pivot_table)
#                                             sum                   mean          
#                                           Price Quantity         Price  Quantity
# Manager       Rep           Product                                             
# Debra Henley  Craig Booker  CPU           65000        2  32500.000000  1.000000
#                             Maintenance    5000        2   5000.000000  2.000000
#                             Software      10000        1  10000.000000  1.000000
#               Daniel Hilton CPU          105000        4  52500.000000  2.000000
#                             Software      10000        1  10000.000000  1.000000
#               John Smith    CPU           35000        1  35000.000000  1.000000
#                             Maintenance    5000        2   5000.000000  2.000000
# Fred Anderson Cedric Moss   CPU           95000        3  47500.000000  1.500000
#                             Maintenance    5000        1   5000.000000  1.000000
#                             Software      10000        1  10000.000000  1.000000
#               Wendy Yule    CPU          165000        7  82500.000000  3.500000
#                             Maintenance    7000        3   7000.000000  3.000000
#                             Monitor        5000        2   5000.000000  2.000000
# All                                      522000       30  30705.882353  1.764706


# print(pivot_table.round(2))
#                                             sum               mean         
#                                           Price Quantity     Price Quantity
# Manager       Rep           Product                                        
# Debra Henley  Craig Booker  CPU           65000        2  32500.00     1.00
#                             Maintenance    5000        2   5000.00     2.00
#                             Software      10000        1  10000.00     1.00
#               Daniel Hilton CPU          105000        4  52500.00     2.00
#                             Software      10000        1  10000.00     1.00
#               John Smith    CPU           35000        1  35000.00     1.00
#                             Maintenance    5000        2   5000.00     2.00
# Fred Anderson Cedric Moss   CPU           95000        3  47500.00     1.50
#                             Maintenance    5000        1   5000.00     1.00
#                             Software      10000        1  10000.00     1.00
#               Wendy Yule    CPU          165000        7  82500.00     3.50
#                             Maintenance    7000        3   7000.00     3.00
#                             Monitor        5000        2   5000.00     2.00
# All                                      522000       30  30705.88     1.76

pivot_table.columns = ['sum_price', 'sum_quantity','mean_price', 'mean_quantity'] # 튜플 멀티컬럼에서 평탄화.
#                                          sum_price  sum_quantity    mean_price  mean_quantity
# Manager       Rep           Product                                                          
# Debra Henley  Craig Booker  CPU              65000             2  32500.000000       1.000000
#                             Maintenance       5000             2   5000.000000       2.000000
#                             Software         10000             1  10000.000000       1.000000
#               Daniel Hilton CPU             105000             4  52500.000000       2.000000
#                             Software         10000             1  10000.000000       1.000000
#               John Smith    CPU              35000             1  35000.000000       1.000000
#                             Maintenance       5000             2   5000.000000       2.000000
# Fred Anderson Cedric Moss   CPU              95000             3  47500.000000       1.500000
#                             Maintenance       5000             1   5000.000000       1.000000
#                             Software         10000             1  10000.000000       1.000000
#               Wendy Yule    CPU             165000             7  82500.000000       3.500000
#                             Maintenance       7000             3   7000.000000       3.000000
#                             Monitor           5000             2   5000.000000       2.000000
# All                                         522000            30  30705.882353       1.764706

# print(pivot_table)