# print()는 문자열 출력.

# input() => 키보드로부터 문자열을 입력받는 함수
# python은 scanf와 print가 input 하나로 합쳐져있다.
# input("데이터 입력: ") # 문자열을 화면에 출력하고 입력 대기

# input은 무조건 문자열로 처리된다.
# inputData1 = input("1 변수로 저장할 숫자 입력: ")
# inputData2 = input("2 변수로 저장할 숫자 입력: ")
# print(inputData1 + inputData2) # 문자열로 처리된다!

#정수 처리 하고 싶을 땐 타입 변환이 필요하다.(casting)
# 다른 언어는 (int) 이런 식이지만, 객체 지향 언어로 넘어오면서, int() 이렇게 된다.
# 연산처리 하려면, 피연산자들의 타입이 모두 같아야 한다.
# int("1024") -> 1024로 처리된다.
# int("1,024") -> 오류! ','는 전처리 단계에서 지워줘야 한다.
# inputData1 = int(input("데이터 1 입력: "))
# inputData2 = int(input("데이터 2 입력: "))
# print(inputData1 + inputData2)

saved_pw = 'python'

# 들여쓰기 단위도 생각해보자. 파이썬은 중괄호 구문 단위가 없다.
# while True: # while 조건문... thile true: 항상 참.
#     input_str = input("Password 입력(종료 : quit) ==>")
#     if input_str == saved_pw:
#         print("pw success!")
#         break # 반복문 탈출
#     elif input_str == 'quit':
#         break
#     else:
#         print("pw fail!!")


while True:
    print("True")
    break # 탈출해주지 않으면 무한 반복된다.
