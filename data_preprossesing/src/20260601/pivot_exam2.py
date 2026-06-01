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


df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\tips.csv')

# print(df.head(5))
#    total_bill   tip  gender smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4

# print(df.info())
# print(df.columns)

## 요일별 'total_bill','tip'의 총합을 계산 출력

grp = df.groupby('day')[['total_bill','tip']].sum()

# print(grp)
#       total_bill     tip
# day                     
# Fri       325.88   51.96
# Sat      1778.40  260.40
# Sun      1627.16  247.39
# Thur     1096.33  171.83

## 재형성에서 pivot_table() 명시적이라서 
# pd.pivot_table(data=df) # 가 아닌
pt = df.pivot_table(
	index='day',
	values=['total_bill','tip'],
	# columns=[], # 여기선 의미가 없다.
	aggfunc='sum',
	# sort=False
)

# print(pt)
#          tip  total_bill # 지가 알아서 컬럼명을 오름차순 정렬시켜버린다. sort=False 주면 안한다.
# day                     
# Fri    51.96      325.88
# Sat   260.40     1778.40
# Sun   247.39     1627.16
# Thur  171.83     1096.33

## 

# print(df.head(5))
#    total_bill   tip  gender smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4

pt2 = df.pivot_table(
	index=['day'],
	columns=['smoker'],
	values='tip',
	aggfunc='sum'
)

print(pt2)
# smoker      No     Yes
# day                   
# Fri      11.25   40.71
# Sat     139.63  120.77
# Sun     180.57   66.82
# Thur    120.32   51.51

##
pt2.plot.bar(
	stacked=True, # 누적 차트
	rot = 0 # 바로눕히기
)

plt.show()