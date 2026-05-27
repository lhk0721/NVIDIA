
# 시퀀스 객체는 데이터의 순서가 있는 문자열, 리스트, 튜플
# 객체지향언어(oop) 특정 클래스를 바탕으로 객체를 생성해서 프로그램이 동작한다.

#객체생성문법: 클래스명()
str("python"); # 동적 타이핑. 이 경우에는 문자열로 "python" 하는 순간 타입이 결정된다.
data1 = "python" #객체의 아이디를 담는 변수.

#메서드: 객체 정보에 접근,조작할 수 있는 멤버함수.
# data1.join()
# data1.replace()
# data1.format()
# data1.split()
# data1.strip()
# data1.upper()
# data1.lower()

# data1 = 800 #이제는 800 int 객체를 바라본다. 더이상 "python" 객체에는 접근할 수 없다. 참조할 수 있는 id를 잃어버리고, 가비지컬렉터가 메모리 free함.
data2 = 800

# 시퀀스 객체는 순서가 있다.
data1[0] # 색인연산: [index] index는 항상 0부터 출발한다.

# 순서가 있기 때문에 범위로 잘라버릴 수 있다.
data1[1:3] # 슬라이싱 문법: [start : stop-1]

# 곱셈연산, 덧셈연산
# data1 + data2 # 피연산자들의 타입이 달라 오류가 발생한다.
data3 = "800"
data1 + data3 # 두 문자열을 합쳐줌
data1 * 5 # 횟수만큼 반복해서 생성

# 타입변환
print(list(data1)) # 각 인덱스값을 리스트 원소로 꺼내는 타입변환

# 반복
for item in data1:
    print(item, end=' ');

