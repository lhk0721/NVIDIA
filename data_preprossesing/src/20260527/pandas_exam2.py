import numpy as np
import pandas as pd

myDf = pd.DataFrame(
    np.arange(10,25)
    .reshape((5,3)),
    columns=['one', 'two', 'three'],
    # index=list('abcde')
    )

# print(myDf)

## 데이터프레임 객체 secelction. 접근 문법

# 명시적 인덱스 / 암묵적 인덱스
# 넘파이의 클래스와 다르다.
# print(myDf['b','two']) # 오류!
# print(myDf[ 행인덱스, 열인덱스 ]) values가 넘파이(무조건 수치), 바깥은 데이터프레임이다.
# 접근할 때 라벨로 접근할지 수치로접근할지 정하는 매서드가 필요하다.

# loc ( 라벨 location )라벨로 접근
# print(myDf.loc[ 'c', 'two' ])
# true,false boolean 배열이 접근 가능하다.

# iloc ( integer location ) 수치 인덱스로 접근
# print(myDf.iloc[2,1])
# 인덱스를 배열로 줘서 퐁당퐁당 cherrypickking도 가능하다. 펜스(?) 인덱싱

# 암묵적 index만 존재할 때 loc로 접근
# 명시적 인덱스 2를 라벨로 접근해서 loc가 가능하다.
# print(myDf.loc[2,'two']) # 수치지만, 명시적 인덱스로 접근한다. 가능은 하지만 통일해서 사용한다. 이러한 경우 iloc으로 접근.

## 새로운 'four' 컬럼 추가.
# 일단 컬럼만 추가하고, 데이터는 나중에 처리.
myDf['four'] = list(range(5)) # 딕셔너리다!
myDf['four'] = 0 # 리스트로, 동일한 값이면 브로드캐스트로
# 엑셀의 빈칸 표현 -> 결측치 NaN, Not a Number
myDf['four'] = np.nan

# myDf.to_excel('.\src\\20260527\Mydata.xlsx',index=False) # 엑셀로 저장

# 새로운 행 추가
myDf.loc[5] = np.nan # 명시적 인덱스로 해줘야 한다.
# iloc은 안되는 이유 라벨을 부여 안했기 때문에 수치로 보이지만, 판다스는 명시적 라벨로 본다. 거의 loc밖에 쓸 일이 없을 거다.

# 항상 인덱스, 컬럼, 타입 출력해보자.
print(myDf.index)