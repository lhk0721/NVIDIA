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


df = pd.read_excel(r'C:\Users\25\Documents\github\python_project\dataset\반도체_제어_이력.xlsx')

# print(df.head(5))
# print(df.info())
# print(df.columns)
# Index(['이력 ID', '공정 단계', '장비명', '파라미터', '목표값', '실제값', '단위', '변경 일자', '담당 엔지니어', '비고'], dtype='object')
## 다섯 개 컬럼만 선택추출

semidf = df[['공정 단계', '장비명', '파라미터', '목표값', '실제값']]
# print(df.loc[:,['공정 단계', '장비명', '파라미터', '목표값', '실제값']])
# print(semidf)

## 1. 장비명에 숫자문자가 있는 장비명 행만 추출(선택)

subset1 = df.loc[df['장비명'].str.contains(r'[0-9]+'),:]

# def NameFilter(arg):
#     return len(re.findall(r'[0-9]+', arg))>0
# subset1 = df.loc[df['장비명'].apply(NameFilter),:].copy()

# subset1 = df.loc[df['장비명'].apply(lambda x: len(re.findall(r'[0-9]+', str(x))) > 0), :]

# print(subset1)


#     이력 ID 공정 단계                장비명 파라미터      목표값      실제값     단위       변경 일자 담당 엔지니어         비고
# 0       1    식각  Lam Research 2300   압력  3048.24  3050.52  mTorr  2025-01-26     김철수   장비 점검 필요
# 3       4   CMP      Ebara FREX300   압력  1116.39  1112.68    psi  2025-02-14     박민수     재조정 예정
# 7       8   CMP      Ebara FREX300   압력  4988.70  4991.24    psi  2025-02-02     박민수  공정 최적화 필요
# 14     15   CMP      Ebara FREX300   압력  2851.81  2848.11    psi  2025-02-14     이영희     재조정 예정
# 15     16    식각  Lam Research 2300   압력  4491.82  4488.75  mTorr  2025-01-24     최지훈  공정 최적화 필요

# print(subset1)
## 2. 가장 많은 공정단계

# print(df['공정 단계'].value_counts())


# groupset = df.groupby('공정 단계')['장비명'].count().copy()


# print(groupset)
# 공정 단계
# CMP      18
# 검사       17
# 금속 배선    17
# 노광       16
# 식각       15
# 증착       17
# Name: 장비명, dtype: int64

## 공정 단계별 목표값, 실제값의 평균을 계산해서 출력
# print(semidf.head(5))

prinf_df(semidf.head(5))
# +---+-----------+-------------------+-----------+---------+---------+
# |   | 공정 단계 |       장비명      |  파라미터 |  목표값 |  실제값 |
# +---+-----------+-------------------+-----------+---------+---------+
# | 0 |    식각   | Lam Research 2300 |    압력   | 3048.24 | 3050.52 |
# | 1 |    검사   | KLA-Tencor Archer |  결함 수  | 3449.16 | 3450.56 |
# | 2 | 금속 배선 |  TEL Clean Track  | 회전 속도 | 3043.13 | 3042.47 |
# | 3 |    CMP    |   Ebara FREX300   |    압력   | 1116.39 | 1112.68 |
# | 4 | 금속 배선 |  TEL Clean Track  | 회전 속도 | 3774.33 | 3779.21 |
# +---+-----------+-------------------+-----------+---------+---------+

groupmean = semidf.groupby('공정 단계')[['목표값','실제값']].mean().copy()

# prinf_df(groupmean)
# +-----------+--------------------+--------------------+
# |           |       목표값       |       실제값       |
# +-----------+--------------------+--------------------+
# |    CMP    | 2299.077222222222  | 2298.6944444444443 |
# |    검사   | 2892.0941176470587 | 2892.9864705882355 |
# | 금속 배선 | 2929.725294117647  | 2929.998235294118  |
# |    노광   |     2320.01125     |    2320.763125     |
# |    식각   | 2609.3166666666666 | 2608.6213333333335 |
# |    증착   | 2142.954117647059  | 2142.7935294117647 |
# +-----------+--------------------+--------------------+

group = semidf.groupby('공정 단계').agg(
    {
        '목표값' : ['count','sum','mean'],
        '실제값': ['count','sum','mean']
    }
).round(2).copy()

# prinf_df(group)
# +-----------+---------------------+-------------------+--------------------+---------------------+-------------------+--------------------+
# |           | ('목표값', 'count') | ('목표값', 'sum') | ('목표값', 'mean') | ('실제값', 'count') | ('실제값', 'sum') | ('실제값', 'mean') |
# +-----------+---------------------+-------------------+--------------------+---------------------+-------------------+--------------------+
# |    CMP    |          18         |      41383.39     |      2299.08       |          18         |      41376.5      |      2298.69       |
# |    검사   |          17         |      49165.6      |      2892.09       |          17         |      49180.77     |      2892.99       |
# | 금속 배선 |          17         |      49805.33     |      2929.73       |          17         |      49809.97     |       2930.0       |
# |    노광   |          16         |      37120.18     |      2320.01       |          16         |      37132.21     |      2320.76       |
# |    식각   |          15         |      39139.75     |      2609.32       |          15         |      39129.32     |      2608.62       |
# |    증착   |          17         |      36430.22     |      2142.95       |          17         |      36427.49     |      2142.79       |
# +-----------+---------------------+-------------------+--------------------+---------------------+-------------------+--------------------+

# groupmean.plot.bar()
# group.plot.bar()
# plt.show()