import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt # 차트 시각화 라이브러리

## pandas로 편하게 읽기
my_df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\서울특별시_지하철 승하차 승객수.csv', encoding='CP949')
# print(my_df.head())
print(my_df['호선_명칭'].unique())

## 3,7,9,수인선만 추출

# subset1 = my_df.loc[(my_df['호선_명칭'] == '3호선'), :].copy()
# subset2 = my_df.loc[(my_df['호선_명칭'] == '7호선'), :].copy()
# subset3 = my_df.loc[(my_df['호선_명칭'] == '9호선'), :].copy()
# subset4 = my_df.loc[(my_df['호선_명칭'] == '수인선'), :].copy()
# subset_concat = pd.concat([subset1,subset2,subset3,subset4])
# subset_concat.reset_index()

# print(type(subset_concat))
# print(my_df['호선_명칭'].isin(['3호선','7호선','9호선', '9호선(연장)'])) # 있으면 True, 없으면 False -> boolean 배열
subset = my_df.loc[my_df['호선_명칭'].isin(['3호선','7호선','9호선', '9호선(연장)']), : ]
subset.set_index(['기준_날짜'],inplace=True,drop=True)
print(subset)