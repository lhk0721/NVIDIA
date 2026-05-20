# 정의와 실행이 번갈아가며 작성하는 것은 학습용이고, 선언부와 호출부가 분리되어야 한다. 한 파일에서 분리되던지, 호출부 외부에서 선언 후 호출부에서 import 하던지.

# 함수 코드의 유지보수성과 코드의 재활용성을 향상시키는 기능이다.
# 특정 기능을 분할해서 완성된 코드를 구현하는 목적에서 함수를 사용한다.
# y = f(x)

# input이 없을 수도 있고, output도 없을 수 있다.
# 전달받는 것이 매개변수, 내뱉는 것이 리턴값이다.

# 파이썬에서는 함수 정의와 호출만 있으면 된다.
# 함수 정의는 특정 기능의 명령어의 집합이다.
# 함수 호출은 특정 함수 정의 부분으로 jump시키는 것이다. 
# 함수 호출은 내부적으로 stack으로 다룬다. 함수 호출 depth가 높을 수록 복잡도가 높아진다.
# C에서는 stack 메모리를 많이 잡아먹지만, 

# 정의는 def로 시작한다. 호출은 함수명으로 시작한다.

#def 함수명():
# def ComNameDisplay():
#     pass # 일단 뼈대만 완성. 최소한 이건 있어야 오류가 발생하지 않는다.

    # 함수는 하나의 box 개념이다. 
# def ComNameDisplay(): # 여기의 괄호는 매개변수가 들어갈 위치를 명시한다. 비어있으면, 입력을 안받는 것이다.
#     print('Ai core')

# 함수 호출. 오타 막기 위해 복붙할 것.
# 함수이름 + ()
# print('프로그램 시작')
# ComNameDisplay()
# print('프로그램 종료')

# 전달인자
# def ComNameDisplay(arg): #'lee' 라는 객체의 id가 매개변수로 복사된다. 전달인자와 매배변수 사이에는 보이지 않는 = 대입 연산자가 숨어있다. id를 복사해 주는 것이다.
#     print(f'{arg} Ai core')

# print('프로그램 시작')
# ComNameDisplay('Lee') # 함수명( 전달인자 ) 함수 정의부로 jump! 
# print('프로그램 종료')

# 전달인자의 다중화
# def ComNameDisplay(arg1, arg2): # 다중 인자, 매개변수
#     # print(f'{arg1} {arg2} Ai core')
#     return (f'{arg1} {arg2} Ai core') # 반환구 추가. 파이썬에서는 반환값이 없을 경우 오류 발생이 아닌 None 객체를 반환한다. sort 할 때 경험했을 것이다.
#     # return -> 함수의 종료 기능 과 값의 반환 기능을 한다.

# print('프로그램 시작')
# result = ComNameDisplay('Lee', 80) # 실행결과를 변수에 담을 수 있다.
# print (result)
# print('프로그램 종료')

# 매개변수가 없는 경우
def InputData(): 
    numData = int(input('정수 하나 입력하세요'))
    return(numData) 

# garbagecollect되지 않도록 리턴값을 바라보는 변수 하나를 준다.
data1 = InputData()
print("data1: ",data1)
# 함수 안에 있는 변수와 함수 밖에 있는 변수의 역할이 다르다. 함수 내부에서 선언된 변수는 함수 내부에서만 유효하다. 
# 따라서 함수 외부에서 변수를 따로 선언해 id를 넘겨받아야 한다.