# 0~ 전달해주는 특정 정수까지의 총합을 계산하는 함수

# def SumOfIntData(arg=5, _=10): # parameter에 값을 주면, 함수 호출 시 인자를 주지 않았을 시 기본값으로 동작한다. (default parameter)
#     total = 0
#     for i in range(arg): # range: 범위 설정.
#         total += i
#     return total

# result = SumOfIntData(50) # function call. param은 인덱스 기반으로 들어간다. 호출부에서 앞선 매개변수에 기본값이 있다고 다음 매개변수에 들어가지 않는다.

# 전달 인자가 여러개인 경우 처리하는 함수 가변 매개변수
# def SumOfData(_arg,*arg,): # *를 param에 붙이면, 여러 개의 전달인자를 하나로 묶어서(pack) 받는다. tuple로 처리. param을 하나 더 넣어도 앞에 *가 다 흡수해버린다.

    # print(arg, type(arg)) # (3, 5, 6, 7, 8, 9) <class 'tuple'>
    
    # return

# result = SumOfData(3,5,6,7,8,9) # 원칙상 정의부에 param이 6개 있어야 한다.

# dict 형태 처리 함수
# def MyDictFunc(**arg): # *를 쓰면 tuple로 묶어버린다. dict로 받고 싶으면 **를 쓴다. 그럼 호출부 값의 
#     print(arg.keys(), arg.values(), type(arg))

# MyDictFunc(a = 100, b = 30, c = 90)

# 예제
def MyDataControll(arg):
    result = 0
    for i,v in arg:
        result += v
    return result

# enumerate는 튜플로 반환한다.

dataList = [(3,4), (5,6),(7,5)]
result = MyDataControll(dataList)
print(result)