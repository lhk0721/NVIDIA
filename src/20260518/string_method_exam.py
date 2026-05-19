from unittest import result

#format 문법
name = "홍길동"
age = 50

# old 문법
print("나의 정보 ==> 이름 : {}, 나이: {}".format(name, age)) # 파이썬은 %d, 이런 게 의미 없다. format method 쓰면 됨.

# 최신 문법
print(f"나의 정보 ==> 이름 : {name}, 나이: {age}") # format 메서드 호출과 같다. 짧게 쓰려는 python의 노력.

strData = "python Programming"
# strData. 점 찍어보기! c의 구조체 멤버에서 유래됨. 멤버 직접 접근 연산자. 메서드는 멤버함수 연산자.

print(strData.capitalize()) # p -> P로 바뀐 새로운 문자열 객체가 생성됨. 문자열은 constant 객체 이므로

# 여러 줄 문자열 작성 추후 프롬프트 입력에 유리하다.
strData3 = """
python Programming
test python prog
python good
"""

# count
print(strData3.count("python"))

#replace
strData4 = "test programming"
print(strData4.replace("test","python"))

#replace
strData5 = "test,programming,happy"
print(strData5.replace(","," "))
newString = strData5.replace(","," ")
print(newString)

#특정 문자 기준으로 분할
newString2 = newString.split(" ")
print(newString2) # 결과물을 리스트로 반환.
print(newString2[1])
print(newString2[:2])

string_exam = "kbs , mbc , jtbc , sbs"
# result = string_exam.replace(" ", "").split(",")
newString = string_exam.split(",")

# strip
# listData = []
# for item in newString:
#     listData.append(item.strip())
# print(listData)

# listData = [item.strip() for item in newString]
# print(listData)

listData1 = ['kbs' , 'mbc' , 'jtbc' , 'sbs']
newData = "/".join(listData1)
print(newData)

listData3 = "python#test ai programming,study"
result = (
    listData3
      .replace("#",",") # replace는 동시에 2개 이상을 처리할 수 없는 한계를 가지고 있다.
      .replace(" ", ",")
      .split(",")
)

import re # 정규 표현식.. 뒤에 배울 내용임. 그냥 참고
result = re.sub(r'[#,]', ' ', listData3)

print(result)


# 매서드 확인
list_exam = [] # 대괄호로 심어놔서 인터프리터가 내부적으로 인식하는 클래스 생성 문법
list_exam = list() # 원칙 또는 내가 만든 클래스일 때. 객체생성문법'객체이름()'  내장 클래스 또는 라이브러리 일 때는 상관없음.
print(list_exam, type(list_exam))
#list_exam.

str_exam = "asdadsa"
# str_exam.
# 메서드 이름 같아도 전달해야 하는 인자 다르다.

str_exam.split()
#괄호 쳐보면 뭘 넣어줘야 하는 지 알려준다.

# 같은 이름을 가지는 매서드들이 다양한 곳에서 오버로딩되어 쓰이기 때문에, 이동 -> 호출위치 해서 확인해 보는 것도 도움이 된다.

data = dict() # dict 클래스를 이용한 dict 객체 생성
data = {} # 다른 방법

data2 = tuple() # 클래스 문법을 사용한 객체 생성
data2 = () # 파이토닉한 방법


num = int("352")
_str = "abcdef"
list_num = list(_str)
print(list_num)

# 문자열 연산은 항목 수정이 불가능하지만, 리스트는 r/w가 가능한 객체이다.
# 파이썬에서 가장 중요한 것이 리스트 문법이다.
