# set 타입 (집합 타입) 수학의 집합연산 (합, 교, 차, 여) 지원.
# 시퀀스 타입이 아니다.

# 객체 생성 문법
# set() # == {} 다만, 이렇게만 하면 dict타입이 된다.
data1 = {50,90,60,40}
print(data1, type(data1))

# 데이터 중복을 없애기 위한 set 으로의 형 변환
listData = [5,4,32,4,6,2,1,2,4,4,5,6,67,1,6,5]
print(set(listData))
# set 타입의 특징. 중복 데이터를 허용하지 않는다. unique한 것만 반환해준다.

data2 = {90, 60, 80, 30}

# 차집합 연산 수행
print(data1 - data2)

# 합집합 연산 수행
print(data1 | data2)

# 교집합 연산 수행
print(data1 & data2)

# 여집합 연산 수행
print(data1 ^ data2)

import random # 파이썬 기본 제공

# 임의의 정수(난수) 추출
result = random.randint(1000000,2000000) # a~b 사이의 임의의 정수 하나를 반환
print(result) # 한계... 하나의 정수밖에 추출해주지 않는다.

import numpy as np # 넘파이 사용하면 크기 지정 가능

result2 = np.random.randint(1,46,(6,))
print(set(result2))
print(list(set(result2))) 

result3 = np.random.randint(1,46,(5,6))
print(result3)