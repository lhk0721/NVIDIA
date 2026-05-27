import numpy as np
import pandas as pd

# 판다스 ==> 넘파이 상위 라이브러리, 데이터분석에 특화된 라이브러리
# ==> 판다스는 두 가지 객체를 지원 ==> 1차원 배열 형태(Series), 2차원 배열 형태(DataFrame)

# 접근할 때 수치와 라벨(문자열) 인덱스도 지원을 해줌.
# 넘파이 2차원 배열을 접근할 때는 항상 수치 인덱스만 접근이 가능

# DataFrame 객체 생성 ==> 2차원 배열 형태
## 딕셔너리를 활용해 객체 생성
# 1. 사전 객체 전달
mydf = pd.DataFrame({"kor":[50, 60, 70], "eng": [80, 90, 77]}, index = list('abc'))
# print(mydf)
# print(mydf.columns) # 현 데이터프레임 객체의 column index를 반환
# dtype='object' => 문자열을 의미함.
# 데이터프레임 객체 생성시 인덱스를 부여하지 않으면 자동 인덱싱이 동작함.
# 자동인덱스는 정수(수치) 범위 인덱스가 동작.
# print(mydf.index) # 행 인덱스를 반환함.
# print(mydf.values, type(mydf.values)) # 데이터프레임 객체의 내용물을 반환 -> 넘파이 배열
# print(mydf, type(mydf))

# print("=" * 80)
# print(mydf['kor'], type(mydf['kor'])) # Series: 1차원
# Series에 접근 -> DataFrame 객체의 한 컬럼열을 선택하면 해당 객체는 1차원 형태의 Series 객체가 됨.
# print(mydf['kor'][0])
# print("=" * 80)

# 컬럼 인덱스 수정
mydf.columns = ["국어", "영어"] # 인덱싱을 통해 하나씩 바꿀 수 X -> 컬럼 인덱스를 수정하는 문법
# print(mydf)

# 인덱스
# 명시적 인덱스: 눈에 보이는 인덱스(라벨 인덱스)
# 암묵적 인덱스: 수치 인덱스

## 리스트를 활용해서 DataFrame 객체를 생성

myDf = pd.DataFrame([ [60, 80, 70], [90, 50, 85], [66, 77, 88]], columns=['국어', '영어', '수학'], index= ['a','b','c'])
# index('abc') 이렇게 줘도 된다.
# print(myDf)

# 컬럼은 국어, 영어, 수학
# 행은 a,b,c로 추하가자.

# myDf.columns('국어', '영어', '수학')
# print(myDf)

## numpy 배열을 활용한 DataFrame 객체 생성
myDf = pd.DataFrame(
    np.arange(10,25)
    .reshape((5,3)),
    columns=['one', 'two', 'three'],
    index=list('abcde')
    )

print(myDf)