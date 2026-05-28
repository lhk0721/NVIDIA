import numpy as np
import pandas as pd

## np 내장함수
arr = np.arange(1,10).reshape(3,3)
# print(arr)

# print(arr.max(axis=0)) # 제공해주는 집계(통계): sum, min, max, mean

## pandas 내장함수
df = pd.DataFrame(arr, columns=['a', 'b', 'c'])
# print(df)

# print(df['a'].mean())
# print(df['a'].max())

## map
# 최신 버젼에서는 apply, map이 map으로 통합됨.

## lambda

def MyAddFunc(arg):
    return arg + 5

result = MyAddFunc(7)
# print(result) 함수를 만들기 귀찮다,,

# 'x' : 매개변수
# ':' : return
f = lambda x : x+5 # 익명함수. lambda함수
f = (lambda x : x+5)(7) # 바로 7을 넘김
f = lambda x=7 : x+5 # 기본값 7

# print(f(30))

print(5**3)
print(np.power(5,3))
print((lambda x: x**3)(5))

##

dictData = {'Hong':[90, 80, 70, 50, 75], 'Kim':[85, 95, 65, 55, 75], 'Park': [88, 93, 75, 72, 75], 'Lee':[55, 66, 77, 92, 75]}
df = pd.DataFrame(dictData, index=['kor', 'eng', 'math', 'music', 'science'])

# DataFrame 또는 Series의 각 요소에 특정 함수를 일괄 적용시켜서 동작하는 기능을 함수 적용이라고 한다.
# 1. map mapper
# 2. apply 특정 함수 적용 시 많이 사용된다.
# print(df)

# df2 = df[['Hong']].map(lambda x: x+3)
# print(df2)

## map 사용 사례

df['성별'] = ['male', 'female', 'male', 'female', 'male']
# print(df)
# df.info()

# def DataControl(arg):
    
#     # print('arg: ', arg)
    
#     if(arg == 'male'):
#         return 1
#     else:
#         return 0


# print(df['성별'].map(DataControl)) # series 넣었으니 series 반환

# df['성별'] = df['성별'].map(DataControl) # 갱신. 허나 이런 경우엔 apply를 더 많이 쓴다. 결국 함수를 만들어야 해서

# df['성별'] = df['성별'].map({'male':1, 'female':0})

# print(df)

## apply 사용 사례
print(df)

# def ScoreIncrease(arg):
#     return arg + 3
# df['Hong'] = df['Hong'].apply(ScoreIncrease)

df['Hong'] = df['Hong'].apply(lambda x: x+5) # 앞에를 그냥 df 하면, 변수 처리되어 새로운 시리즈가 생겨버린다. 

print(df)
