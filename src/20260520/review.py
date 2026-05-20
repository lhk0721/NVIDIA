import numpy as np
# 시퀀스타입은 문자열, 리스트, 튜플

# 가장 많이 쓰는 것은 리스트
# list() # 객체지향 언어이기 때문에 클래스 문법 써야 한다.
# [] # 위 명령과 동일
# 위 두 명령은 메모리에 리스트 객체를 생성함. 
# listData = [] 그 주소를 담을 변수가 필요하다.
# listdata = [[5,6], "python", 3.14] # 리스트에 담는 항목은 제한이 없다. 리스트는 항목들의 Id를 담기 때문이다.
# print(listdata[1]) # 색인연산
# listdata[1] = "ai" # 읽기, 쓰기가 둘 다 가능하다. 

# 튜플
# tupleData = () # == tuple()
# tupleData = (5,) # 하나의 객체만 담으면 연산자 우선순위로 처리하기 때문에 콤마 써라.

# import numpy as np # 원래는 최상단에 올려 import들 묶어야 한다.
# arr1 = np.array([[[3,4,5,6,7],[4,3,3,2,5]]]) # np를 이용해 리스트 객체를 만들어라. 
# print(arr1)
# print(arr1.ndim) # 몇 차원인가?
# print(arr1.shape) # 형태 (5,) 튜플 형태로 shape를 반환한다.

# 접근은 행과 열의 슬라이싱 연산으로 한다.

# 범위데이터
# range() # 파이썬 기본 제공
# print(np.arange(1,11)) # 콤마가 없으면 넘파이.
# arr1 = np.arange(1,10).reshape(3,3) # 2행 5열로 만들어줘. 단, reshape하려는 형식과 원본 데이터의 갯수가 맞아야 한다.
# 원래 shape를 전달할 때는 튜플로 전달해야 하나, 튜플의 unpack 기능으로 풀어지는 것이다.
# unpack
# data1, data2 = (3,5)
# print(data1, data2)
# print(arr1)
# print(arr1.shape)

a = 5
b = 7
a,b = b,a # tmp 변수가 필요가 없다. 내부적으로 튜플 처리가 된 것이다. pack이 일어나 복사되었다가 다시 unpack이 일어난다. 가장 파이썬스러운 코드이다.

print(a,b)

# 튜플은 리스트와 같이 항목에 제한이 없고, 인덱스가 있다. 하지만 리스트와 달리 불변한다. 바라보는 변수가 달라지지 않게 하는 상수 개념이다. 인덱스에 해당하는 메모리 주소를 고정하는 것이다. 튜플은 read 전용이다.

# 딕셔너리
dictData = {} # == dict(), 매핑 타입. key와 value로 이루어져 있다. 시퀀스타입이 아니다.
dictData["key"] = 'value' # []대괄호에 key가 온다. 시퀀스타입이 아니기 때문에, 인덱스로 접근하면 안된다.
dictData["key"] = 'value2' # 없는 key면 생성하고, 있는 key면 value를 수정한다.
print(dictData['key'])

for key in dictData: # 반복문에 dict가 오면 key가 반환되어 전달된다.
    print(key, dictData['key'])

