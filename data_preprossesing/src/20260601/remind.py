import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\tips.csv') # csv 파일을 읽어서 데이터프레임 객체로 만들어준다.

# print(df)
# print(df.info)
# print(df['gender'].unique()) # 특정 컬럼데이터 속성이 뭐가 있고 몇개가 있는지 체크

df['gender'] = df['gender'].map({'Female':1, 'Male':0}) # 업데이트해줘야 한다.
# print(df)

# 특정 컬럼데이터 기준 정렬
df.sort_values(by=['gender'],ascending=True,inplace=True) # param by는 정렬할 기준 컬럼. 리스트로 올 수도 있다.

# print(df.head(50))
df_top5 = df.head(5).copy()
# print(df_top5)
df_top5_index = df_top5.reset_index(drop=True).copy()
# print(df_top5_index)

## 특정 컬럼 데이터의 데이터 항목의 갯수를 파악.
daycnt = df['day'].value_counts()
# print(daycnt)
daycntdf = pd.DataFrame(daycnt)
# print(daycntdf)

## 특정 컬럼의 특정 데이터만 추출 -> isin. boolean 배열을 형성.
# print(df['time'].isin(['Lunch']))
# df['isLunch'] = df['time'].isin(['Lunch']) # 한 컬럼 데이터여도 리스트 형태로 전달해야 한다.
# print(df)
# print(df.loc[df['time'].isin(['Lunch']), 'tip':'time'])

subset = df.loc[df['time'].isin(['Lunch']), 'tip':'time']
print(subset)
