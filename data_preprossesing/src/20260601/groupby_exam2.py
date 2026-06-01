import numpy as np
import pandas as pd
import re
from prettytable import PrettyTable  # 3.3.0 version 설치
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import seaborn as sns

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


df = pd.read_excel(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\국소마취제_groupby.xlsx')

# df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 300 entries, 0 to 299
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   약효분류명   300 non-null    object
#  1   상병명     300 non-null    object
#  2   수량      300 non-null    int64 
#  3   금액      300 non-null    int64 
# dtypes: int64(2), object(2)
# memory usage: 9.5+ KB

# print(df.head(5))
#    약효분류명              상병명       수량         금액
# 0  국소마취제       치은염 및 치주질환  1627509  604712401
# 1  국소마취제  치수 및 근단주위조직의 질환   582096  215930479
# 2  국소마취제             치아우식   462333  171292240
# 3  국소마취제            무릎관절증   104374  168745741
# 4  국소마취제             어깨병변   110238  131824561

## '상병명' 기준으로 금액이 가장 큰 상위 top 5개 추출
group_sum = df.pivot_table(
	index=['상병명'],
	# columns=['약효분류명'],
	values=['금액'],
	aggfunc=['sum']
).copy()

# print(group_sum)

# print(group_sum.columns)
# MultiIndex([('sum', '금액')],
#            )

group_sum.columns = ['금액_sum']
# print(group_sum.columns)
# Index(['금액_sum'], dtype='object')

group_sum_sorted = group_sum.sort_values(by='금액_sum', ascending=False).head(5).copy()
prinf_df(group_sum_sorted)
# +-----------------------------+------------+
# |                             |  금액_sum  |
# +-----------------------------+------------+
# |      치은염 및 치주질환        | 1713360349 |
# | 치수 및 근단주위조직의 질환     | 614849172  |
# |           치아우식           | 474307211  |
# |          무릎관절증          | 459556927  |
# |           어깨병변           | 349889897  |
# +-----------------------------+------------+

## seaborn 라이브러리를 이용한 시각화
sns.barplot(data=group_sum_sorted,
			x=group_sum_sorted.index,
            y='금액_sum',
			palette='Set3')
# 또는 reset_index(drop=False) 라고 x에 원하는 칼럼명 넣기.
plt.show()
