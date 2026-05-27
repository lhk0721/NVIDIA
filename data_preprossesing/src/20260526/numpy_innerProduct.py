import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## 행렬연산
x = np.array( [[2,3],[1,2]] )
# print(x)

y = np.array( [[1,2],[2,3]] )
# print(y)

# print(np.dot(x,y)) # 행렬연산

## 비교연산
arr1 = np.random.randint(1,13,(3,4))
# print(arr1 > 6) # 비교연산.. boolean 배열을 형성해준다.

## 집계통계

arr2 = np.arange(1, 50, 2).reshape((5,5))
# print(len(arr2))
print(arr2)

# axis 중요!! 행, 열단위로 할 수 있음.
    # axis = 0 행축 (행 간 연산. 세로)
    # axis = 1 열축 (열 간 연산. 가로)
    # default -> 총합


# # print(arr2.sum()) # 625. 안주면 총합
# print(arr2.sum(axis = 0)) # [105 115 125 135 145] 행축 연산 (아래로 내려감.)
# print(arr2.sum(axis = 1)) # [ 25  75 125 175 225] 열축 연산 (옆으로감)

# # mean
# print( arr2.mean(axis=0))
# print( arr2.mean(axis=1))

# # sum
# print(np.sum(arr2)) # 인스턴스의 메서드로 쓰는 게 아니면 목적을 인자로 줘야 한다.

# print(np.max(arr2))
# print(arr2.max(axis=0))
# print(arr2.max(axis=1))

# print(np.min(arr2))
# print(arr2.min(axis=1))

## 빨리 파일로 저장하고 싶을 경우: 넘파이 배열로도 엑셀로 저장할 수 있다.

df = pd.DataFrame(arr2, columns=list('abcde')) # k,v가 아닌 넘파이 배열을 이용해서 데이터프레임 객체 생성. numpy는 오로지 수치로만. pandas는 수치 지원.
# 암묵적으로 index로 접근할 순 있다.
print(df)
# print(df['d'][1]) # pandas가 되었기 때문에... [1][2]가 아닌 
print(df.iloc[1,2])  