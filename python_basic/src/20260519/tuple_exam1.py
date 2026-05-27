# tuple 또한 시퀀스 테이터 타입의 일종이다.

# 클래스 생성 문법
# tuple() == ()
data1 = ()
print(data1, type(data1))

data2 = (50)
print(data2, type(data2)) # int
# 튜플은 하나의 데이터면, 괄호 연산자로 처리되어 버린다. 따라서 뒤에 ','를 붙여줘야 한다.
# 괄호 연산자 - 연산자가 하나 이상일 경우 꼭 () 연산자를 통해 연산자 간 우선순위를 체크해야 한다.

data3 = (50,)
print(data3, type(data3)) # tuple

# 튜플 또한 시퀀스 객체이며, 어떤 객체이든지 항목으로 올 수 있음!!
data4 = (50, 30, 'asdasd', [10,2,3])
print(data4, type(data4))
data4[3][1] = 100 # 인덱스로 항목에 접근 가능
print(data4, type(data4))
# data4[1] = 100 # 문자열처럼 수정 불가능함!!!
# print(data4, type(data4))

# 50, 60, 70, 80 -> 원래대로라면 객체 메모리 공간이 4개가 필요함
data5 = 50, 60, 70, 80 # 튜플의 pack 기능! 여러 객체를 하나로 묶어버림.
print(data2)

a,b,c = (5,3,2) # 튜플의 unpack 기능! 
print(a,b,c, type(a)) # 튜플이 풀어져버린다. 여러 전달 인자를 하나의 튜플로 받아버릴 수 있다.