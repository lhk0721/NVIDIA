import numpy as np # numpy를 np라는 alias로 사용하겠다.

# 1,2,3, 다차원 배열 형태의 데이터를 생성하고 연산할 필요성 존재.

# 넘파이 배열 객체를 생성
arr1 = np.array( [[5,6,7,8],[15,16,17,18]] ) # 리스트를 이용해서 넘파이 배열 객체를 생성
# print(arr1)
# print(arr1.ndim) # 배열의 차원수를 반환
# print(arr1.shape) # 배열의 형태를 반환 # 2행 4열

## 잠깐 미리보기.

arr2 = np.array([[5],[6],[7],[8]]) # (4,1)
# print(arr2,arr2.ndim,arr2.shape)

arr3 = np.array( [ [ [5], [6], [7], [8] ] ]) # (1,4,1) (4,1)을 1개 묶었다.
# print(arr3,arr3.ndim,arr3.shape)

arr4 = np.array( [ [ [5], [6], [7], [8] ], [ [9], [10], [11], [12] ] ]) # (2,4,1) (4,1)을 2개 묶었다.
# print(arr4,arr4.ndim,arr4.shape)
# print(arr4,arr4.ndim,arr4.shape[0]) # shape[0] -> channel 수

## 범위데이터를 이용해서 넘파이 배열을 생성
arr5 = np.arange(1,13) # 이렇게 하면 1차원 배열, 선형 수열 범위데이터가 생성됨. 
# print(arr5.shape) # (12,)

arr6 = np.arange(1,13).reshape((3,4)) # np 크기는 튜플로 준다.
# print(arr6,arr6.shape)

# 임의의 난수 numpy 배열 생성
# np.random.randn #진짜 난수
arr7 = np.random.randint(1,100,(4,5))
# print(arr7)


## selcection 문법
arr8 = np.arange(1,21).reshape((4,5))
# print(arr8)
# print( arr8[1][2] ) # 범위는 항상 (행,열)
# print(arr8[3][3])

# 슬라이싱
# print(arr8[1:2][1:2]) # 안됨... shape이 틀리다.

# subset = arr8[1:3,1:3] # [행 슬라이싱, 열 슬라이싱]
# subset = arr8[1:, 3:]
subset = arr8[:3, :3]
# print(subset)

## zeros, ones
# zeros 배열의 내용을 0으로 채워서 생성해준다.
arr_zero = np.zeros((13,13))
# print(arr_zero)

arr_ones = np.ones((13,13))
print(arr_ones)

