
# data = 50
# value = 70

# def ReverseData():
#     global data, value # 두 변수를 전역공간에서 채용
#     data, value = value, data

# print('========== 호출 전 ==========')
# print("data: ",data, ' ', 'value: ',value) # 호출 전

# ReverseData() # 함수 호출

# print('========== 호출 후 ==========')
# print("data: ",data, ' ', 'value: ',value) # 호출 후


# # return을 활용해서 바꿔치기
# data = 50
# value = 70

# def ReverseData():
#     # data = 70
#     # value = 50
#     return 70, 50 # 여러개 반환하면 알아서 튜플로 묶어줄 것이다.

# print('========== 호출 전 ==========')
# print("data: ",data, ' ', 'value: ',value) # 호출 전


# data, value = ReverseData() # 함수 호출

# print('========== 호출 후 ==========')
# print("data: ",data, ' ', 'value: ',value) # 호출 후