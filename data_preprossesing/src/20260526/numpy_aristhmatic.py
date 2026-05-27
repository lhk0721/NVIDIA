import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([5,6,7])
arr2 = np.array([3,4,5])
# print(arr1 + arr2) # 리스트 객체는 이어붙이지만, numpy는 행렬연산한다.

arr1 = np.array([5,6,7])
arr2 = np.array([3,4,5,2])
# print(arr1 + arr2) # !오류! shape이 맞아야 한다.

arr1 = np.array([[5,6], [3,7]])
arr2 = np.array([[3,4], [5,2]])
# print (arr1)
# print (arr2)
# print(arr1 + arr2) # 역시 행렬연산. position별.

# shape이 안맞아도 연산이 되는 경우
arr3 = np.array([3,4,5])
# print(arr3 + 3) # 3 하나의 schala -> 내부적으로 [3,3,3]. 앞에 있는 shape에 일치. broadcast 전파 라고 한다.

## matplotlib 사용 예시
arr4 = np.linspace(1,10,5) # 3번째 인자 생략하면 기본값 50구간.
print(arr4)
# plt.plot(arr4) # 메모리에 랜더링
# plt.show()

arr5 = np.array([1,3,6,10,15])
# plt.plot(arr5)
# plt.show()

# y = 1/ np.exp(-x) + 1
# plt.plot(y)
# plt.show()



