import numpy as np
import pandas as pd
import re
##

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)


##
# df = pd.read_csv('.\src\\20260528\서울특별시_지하철 승하차 승객수.csv', encoding='CP949')

# print('='*80)
# df.info()
# print('='*80)
# print(df.head(10))
# print('='*80)

## 호선_명칭 컬럼 데이터 중 숫자문자가 있는 호선_명칭 데이터만 추출하여 출력

# def Find(arg):
#     bool = len(re.findall(r'[0-9]+',arg))

#     if (bool > 0):
#         return True
#     else:
#         return False


# print(df.loc[df['호선_명칭'].apply(Find), :])


##
df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\tips.csv', encoding='CP949')

df['gender'] = df['gender'].map({'Male':0, 'Female':1})

# def Gender_Binary(arg):
#     if(arg == 'Male'):
#         return 0
#     else:
#         return 1
    
# df['gender'] = df['gender'].map(Gender_Binary)

# print(df.head())

## 몇개의 요일이 있는지 체크

print(len(df['day'].unique()))

## 'Sat' 요일과 'Thur' 요일만 추출
# print(df)

dayList = ['Sat', 'Thur']

subset = df.loc[df['day'].isin(dayList),:].copy()

print(subset)

## 토요일과 목요일 인원수의 평균은?
print(subset['size'].mean())