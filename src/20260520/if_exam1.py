# 파이썬 조건문 
# 조건문은 프로그램의 흐름을 제어하는 역할을 한다. 분기문이라고도 한다.
# 어디로 흘러갈거냐 를 결정.

# 표현식. 조건. 참이냐 거짓이냐를 반환하는 문법을 사용한다.
# 비교(관계) 연산자가 그 역할을 한다. a>b, a<=b, a>=b, a==b, a!=b
# 비트 연산자 ~,&,|,^ 거의 안쓴다.
# 논리 연산자 ||(or) -> OR(두 항이 하나의 항이라도 TRUE이면 전체가 TRUE), AND(둘다 참이어야),
print((5==3) and (3>1))
# 사칙 연산자. +,-,*,%(나머지), /(나눗셈), //(몫만)
print(5%7)

print( 5 > 3 )

# 1. 단독 if 문
# truthy. 컴퓨터에서는 0 이외의 모든 숫자는 참이다.
if(50):
    print('참')

data = 5
if(data == 5):
    print('data == 5')

# 2. if-else 문
if(data == 5):
    print('data == 5') # 조건이 참일 때 수행하는 구문
else:
    print('data != 5') # 조건이 거짓일 때 수행하는 구

# 3. if-elif-else 문. 조건의 경우의 수가 많을 경우 사용

print('메뉴 : 1. 사이다. 2. 콜라. 3. 생수. 4. 쥬스. 5. 프로그램 종료')
while True:
    selMenu = int(input('메뉴를 선택하세요.')) # input은 항상 입력값을 문자열 객체처리한다. 처리 방향에 따라 타입변환을 해야 한다.
    if selMenu == 1:
        print('사이다를 선택하셨습니다.')
    elif selMenu == 2:
        print('콜라를 선택하셨습니다.')
    elif selMenu == 3:
        print('생수를 선택하셨습니다.')
    elif selMenu == 4:
        print('쥬스를 선택하셨습니다.')
    elif selMenu == 5:
        print('프로그램을 종료합니다.')
        break
    else: # 위 조건을 하나도 만족하지 않을 경우 수행. 조건은 if, elif 뒤에만 올 수 있다. 
        print('1~4 중 메뉴 하나를 선택하셔야 합니다.')
    




