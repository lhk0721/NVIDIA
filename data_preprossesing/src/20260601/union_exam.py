import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'customId':[1234,5678,1111,3333], # 공유 키가 있을 때 키 기준으로 합칠 수 있다.
    'name':['Lee','Han','Hong','Park']
    })

# print(df1)

df2 = pd.DataFrame({
    'customId':[1234,5678,1111,3333,7777], 
    'consume':[5000,7000,4000,10000,1000] 
    })
# print(df2)

# mergeDf = pd.merge(df1,df2) # 특정 키 기준으로 두 데이터프레임이 병합된다.
# mergeDf = pd.merge(df2,df1) # 좌우 바꿀 수도 있다.
# print(mergeDf) # key가 달라졌을 때는? 안된다. inner join(교집합)
# 기본 기능은, 두 데이터프레임의 병합할 키 데이터 중 둘 다 있는 교집합에 대해서만 병합을 수행한다.

mergeDf_inner = pd.merge(df1,df2,how='inner') # 교집합 병합 (default)
mergeDf_outer = pd.merge(df1,df2,how='outer') # 합집합 병합

# print(mergeDf_inner)
# print(mergeDf_outer)

## 동일 키(컬럼명)가 없는 경우 좌,우 키 지정하여 병합
# 그냥 하면 오류가 난다. 기본적으로 key 기준 inner join이기 때문

df3 = pd.DataFrame({
    'customId':[1234,5678,1111,3333], # 공유 키가 있을 때 키 기준으로 합칠 수 있다.
    'name':['Lee','Han','Hong','Park']
    })


df4 = pd.DataFrame({
    'customTf':[1234,5678,1111,3333,7777],
    'consume':[5000,7000,4000,10000,1000]
    })

# print(df3)
# print(df4)
mergeDf2 = pd.merge(df3,df4,left_on='customId',right_on='customTf') 
# print(mergeDf2)

# 특정 데이터프레임을 병합할 때에는 merge, concat만 기억하면 된다. 
## concat
# numpy concatenate와 동일
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[5,6,7],[13,15,16]])

print(arr1)
print(arr2)

arr_con = np.concatenate([arr1,arr2], axis=0) # 행으로 취급해 밑으로 붙여버림 (default)
# arr_con = np.concatenate([arr1,arr2], axis=1) # 열으로 취급해 옆으로 붙여버림
# default param에 의존하지 말고, 의도를 명시할 것.
print(arr_con)
