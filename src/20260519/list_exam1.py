
# 리스트도 마찬가지로 시퀀스 타입 객체이다. (색인연산, 슬라이싱연산, +,*)
# 객체지향언어이기 때문에 항상 클래스 이름으로 만들어야 한다.
list() # 리스트 타입의 객체 생성 문법

# 왜 타입이 다 쪼개져있을까? 데이터의 특성 때문이다.
# 항상 메모리에서 꺼내올 수 있는 id를 담을 변수가 필요하다.
# 대입 연산: '=' 왼쪽의 내용을 오른쪽으로 복사 대입.
data1 = list()
# 비교 연산 '==, >, <, <=, >=, !=' 비교 연산의 결과물은 항상 boolean 값이다. true | false

data2 = [] # list()와 같다. 빈 리스트 타입의 객체 타입 선언
print(data2, type(data2))

# 리스트는 문자열과 달리 읽고 쓸 수 있는 타입이다.
# data2[0] = 50 # 오류! index out of range 빈 객체. 빈 리스트는 메모리 공간이 할당되어있지 않고, 아직 인덱스가 안잡혀있음.
data2.append(50)
print(data2, type(data2))
data2.append(80) # write
print(data2[0], data2[0:0]) # read

#빈 리스트 객체에 내용물을 추가하는 방법 (메모리가 안 잡혀있는데, 추가 시 추가 메로리 확보)
data3 =[]
# 리스트에 내용물을 추가하는 메서드(함수)
# list.append() # 뒤에다 붙이기.
# object -> 하나의 객체를 전달.
data3.append(60)
print(data3)
# 문자열은 문자열끼리만 join할 수 있지만, 리스트는 항목으로 오는 객체의 타입에 제한이 없다. 즉, 어떤 객체든지 항목으로 올 수 있다.
data3.append('python')
print(data3)
data3.append(5.9)
print(data3)
# data3.append(list(programming)) 오류!
data3.append(["programming",[90,"nvi"]])
print(data3[3][1][1][1]) #색인연산 사용 방법
print('='*80)

# list.extend() #여러 객체를 동시에 추가할 때 사용. 이터러블의 항목이 풀어져서 들어간다.
# iterable -> 시퀀스객체를 의미한다.
# data3.extend(50) # 오류! 시퀀스 객체가 아님. 이터러블이 와야 함.
data3.extend([50,60,70])
print(data3)
print('='*80)

# list.insert() # 특정 위치에 객체 항목을 넣고, 원래 있던 건 뒤로 밀어냄.
# 첫번째 자리: 들어갈 항목이 위치했으면 하는 값. 두번째 인자는 object로 들어감.
data3.insert(2,30)
print(data3)
print('='*80)

# 길이 계산
print(len(data3))
print('='*80)

#항목 삭제 push,pop같은 다양한 메서드가 있지만 del 키워드를 활용한다.
del data3[4]
print(data3)



