import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt # 차트 시각화 라이브러리

## pandas로 편하게 읽기
popdf = pd.read_excel(r'C:\Users\25\Documents\github\python_project\dataset\population_in_seoul.xls') # 엑셀파일 읽어서 df 객체로 생성
# popdf.dropna(inplace=True)
# print(popdf)

## 데이터프레임 객체의 정보를 확인
# info() 항상 info를 통해 확인해봐야 한다.
# print(popdf.info()) # ! 아님!

# popdf.info()

# print(popdf.head(10)) # 앞부터 n(기본값 5)행 출력

# print(popdf.tail()) # 뒤부터 n(기본값 5)행 출력

# print(popdf.sample(5)) # random으로 n(기본값 1)행 출력

# 사본 추출
# subset = popdf.head().copy() # view 관계 끊기
# print(subset)

## 전처리

# 행으로는 '합계'가 있는 행 삭제
popdf.drop([0],axis=0,inplace=True)
# print(popdf)

# 열로는 '고령자'칼럼 열 삭제
popdf.drop(['고령자'],axis=1,inplace=True)
# print(popdf)

# print(popdf)
# print('='*80)

# 결측치 행 제거
# print(popdf.isna())
# print(popdf['남자'].isnull()) # nan이면 True. boolean 배열을 형성
# print(popdf.loc[popdf['남자'].isnull(),:])
# print(popdf.loc[popdf['여자'].isnull(),:])

# for col in popdf.columns :
#     print('column: ',col)
#     print(popdf.loc[popdf[col].isnull(),:]) # 결측치 검사용 코드
#     print('='*80)

popdf.dropna(axis=0, how='any', inplace=True)
# how = 'any' 행에 결측치가 하나라도 있으면 삭제
# how = 'all' 행의 모든 데이터가 NaN일 때 삭제

# reset_index() 결측치를 삭제하고 난 뒤에는 항상 인덱스를 초기화해주는 게 좋다.
# popdf.reset_index(inplace=True) # 기본 기능. 기존 인덱스를 column에 올리고 인덱스를 초기화함.

# 컬럼별로 올리지 말고, 기존 인덱스 제거
popdf.reset_index(inplace=True,drop=True)

# set_index() 특정 컬럼 데이터를 인덱스로 설정해서 사용 
popdf.set_index('자치구',inplace=True)

## 문제.
# 남자 colum 기준으로 인구수가 20만 이상인 데이터만 추출, 막대그래프로 시각화하기.

print(popdf)
# popdf['남자'].copy().sort_values(inplace=True)

# print(popdf.iloc[12:])
# df = popdf.iloc[11:].copy()
# print(df)

# df.plot.bar()
# plt.show()

popdf['isBig'] = False

for rows in popdf.index:
	print(rows)
# print(popdf)


