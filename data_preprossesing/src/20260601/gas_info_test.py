import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable  # 3.3.0 version 설치

def prinf_df(df):
    table = PrettyTable(['']+ list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    print(str(table))
    print()



## 
df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\seoul_keumchun_gas_info.csv',encoding='CP949',index_col=0)

# df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 13 entries, 0 to 12
# Data columns (total 6 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   Unnamed: 0  13 non-null     int64 
#  1   주유소명        13 non-null     object
#  2   대표자         13 non-null     object
#  3   주소          13 non-null     object
#  4   전화번호        13 non-null     object
#  5   데이터기준일자     13 non-null     object
# dtypes: int64(1), object(5)
# memory usage: 752.0+ bytes

##
df['데이터기준일자'] = pd.to_datetime(df['데이터기준일자'])

print(df['데이터기준일자'])

# df.info()
#  5   데이터기준일자     13 non-null     datetime64[ns]

##

df.set_index('데이터기준일자', drop=True,inplace=True)
prinf_df(df.loc[:,:'대표자'])

# +---------------------+----------------------------------+----------------+
# |                     |             주유소명             |     대표자     |
# +---------------------+----------------------------------+----------------+
# | 2019-09-16 00:00:00 |           태영유업(주)           |     강계영     |
# | 2019-09-16 00:00:00 | KH에너지(주)직영 시흥대로 주유소 |     송진수     |
# | 2019-09-16 00:00:00 |      SK에너지(주)박미주유소      |     조경목     |
# | 2019-09-16 00:00:00 |    지에스칼텍스(주)일신주유소    | 허세홍, 김형국 |
# | 2019-09-16 00:00:00 |   SK네트웍스㈜ 순환도로주유소    | 최신원, 박상규 |
# | 2019-09-16 00:00:00 |     ㈜진우에너지 백운주유소      |     이미선     |
# | 2019-09-16 00:00:00 |            백산주유소            |     문성호     |
# | 2019-09-16 00:00:00 |       주식회사 명보에너지        |     나미선     |
# | 2019-09-16 00:00:00 |      SK에너지㈜ 이가주유소       |     조경목     |
# | 2019-09-16 00:00:00 |      구광석유(주)구광주유소      |     서영철     |
# | 2019-09-16 00:00:00 |         경복에너지주유소         |     표종명     |
# | 2019-09-16 00:00:00 |    대득에너지(금천셀프주유소)    |     정용석     |
# | 2019-09-16 00:00:00 |        남서울(경복에너지)        |     안경복     |
# +---------------------+----------------------------------+----------------+

