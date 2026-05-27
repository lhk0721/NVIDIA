import numpy as np
import pandas as pd

# 사전을 활용해서 dataFrame 객체를 만들어볼 것이다.
dictData = {'Hong':[90, 80, 70, 50], 'Kim':[85, 95, 65, 55], 'Park': [88, 93, 75, 72], 'Lee':[55, 66, 77, 92]}
df = pd.DataFrame(dictData, index=['kor', 'eng', 'math', 'music'])

## 집계
# df['subjectTotal'] = [df.loc[x].sum() for x in df.index]
# df.loc['mean'] = [df[x].mean() for x in df.columns]

## 선택접근

# df.loc[ 행인덱스, 열인덱스 ] -> 한 위치 데이터만 접근
# df.loc[ 행슬라이싱, 열슬라이싱 ] -> 범위데이터 접근
# label(문자열 인덱스)는 마지막 stop을 포함
# int index는 stop-1까지 포함.

# loc 사용
# subsetDf = df.loc['eng':'math','Kim':'Park'].copy() #numpy의 view를 상속. copy하면 완벽한 복제 생성.

# iloc
# subsetDf = df.iloc[1:3,1:3]


# print(subsetDf)

## subset 수정

# subsetDf.loc['eng','Park'] = 99
# print(subsetDf) 
# print(df)

## 
subsetDf = df.iloc[1:3,1:3]
print(subsetDf)

subsetDf.iloc[0:1] = 99
print(subsetDf)
print(df) # 역시 view 관계 성립. 잘라내어 사본만 가공할 땐 .copy() 매서드로 사본 객체를 만들어주자.


