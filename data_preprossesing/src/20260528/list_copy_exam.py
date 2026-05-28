import copy

listData1 = [30,50,[80,90],'python']

## shallowcopy
# # listData2 = listData1 
# # 사본이 복제된 게 아님. 복사된 주소임. 같은 원본 객체를 두 변수가 바라보는 중.

# listData2 = copy.copy(listData1)
# listData1[0] = 88

# print('listData1: ', listData1, id(listData1))
# print('listData2: ', listData2, id(listData2)) # 반영안됨!
# print('Are they same?: ', id(listData1) == id(listData2))

## deepcopy 
# 리스트 내부에 리스트를 포함하고 있을 경우에는 사본객체를 형성할 때 꼭 deepcopy를 사용해라.

listData2 = copy.copy(listData1)
listData1[2][0] = 100
print('listData1: ', listData1, id(listData1))
print('listData2: ', listData2, id(listData2)) # 반영됨!

