# 문자열 객체 는 기본적으로 시퀀스 타입 객체이다.
# 시퀀스 타입은 데이터의 순서가 있는 타입이다.
# 문자열 객체는 기본적으로 str() 이렇게 사용해야 한다.
# 허나 동적 타이핑 언어이므로 그냥 따옴표를 이용해서 생성해도 된다. (변수가 있어야 참조할 수 있음 주의!)
str1 = "python test"

# 시퀀스 타입은 인덱싱을 지원한다.
# 특정 위치를 인덱스로 접근할 수 있다.
# 인덱스는 항상 0부터 출발한다.
print(str1[0]) # p 출력
print(str1[5])

print(str1[-1]) # 뒤에서 부터 출발. -1 이 마지막이다. 뒤에서부터 셀 때는 -1 부터 시작한다.
print(str1[-2])

# 슬라이스 문법
# 슬라이스 문법은 잘라내기.
str2 = "python tset programming"
print(str2[7:11]) # [start : stop -1] 까지 잘라내라!
# print(str2[0:6])
print(str2[:6]) # 파이썬은 종단 인덱스는 비워두는 걸 더 선호한다.
print(str2[12:])

# 문자열 객체에 지원되는 연산
# (+, *)
str3 = "stydy"
print( str1 + ' ' +str3) # 연산자의 기본 동작에 '잇기' 추가 - overloading

# 곱셈 연산
# print("===============================================================")
print("="*50) # 문자열을 숫자 만큼 반복해서 생성해준다.

strData = "AI programming"
for item in strData:
    # 세로
    # print(item)
    print(item + ' ', end='')

print() # 개행 역할을 한다.
print('\n') # 이렇게 하면 개행 두번 먹는다.

strData3 = "AI core"
print(strData3) # DI core가 나오길 원할 땐?

# strData3[0] = 'D' # 오류! 문자열 객체는 재할당 및 수정이 불가능하다. 문자열 객체는 상수 const
# print(strData3)

strData3 = strData3.replace("A","D") # 다만, 원래 strData3에 들어있던 객체는 참조가 불가능해지기에 새로운 변수에 할당하는 게 바람직하다.
print(strData3)

# inedntation error 주의! 파이썬은 {} 코드블럭 개념이 없다. 들여쓰기가 대체하니, indent에 주의할 것!

# in 연산.
print ('py' in "python") #python 문자열 객체에 py 문자열이 있냐?
print ('py' not in "python")

if 'py' in "python":
    print('있음')
else:
    print('없음')

if 'te' not in "python":
    print('없음')
else:
    print('있음')

