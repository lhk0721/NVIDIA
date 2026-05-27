# 파이썬은 객체지향 언어
# 파이썬은 기본적으로 다양한 클래스를 제공 (int, float, str)
# 클래스를 바탕으로 객체를 생성하고 생성된 객체를 변수로 참조해서 동작하는 언어
# ==> 파이썬 프로그램 기본 동작

# class Myclass():
#     def __init__(self):

# 메모리에 저장된 값을 참조할 수 있게 하는 게 바라보는 것이 변수
# 파이썬에서는 변수가 포인터
# data 변수는 50이라는 정수 객체를 참조하는 역할
# 메모리의 id(주소) 를 참조한다.
data = int(50) # 클래스를 바탕으로 객체를 생성하는 문법: 클래스명()
# 동적 typing 언어 => 타이핑 하는 순간 자료형 결정
# 원칙상 클래스 문법을 써야 하는데 알아서 내부적으로 자료형이 결정된다.

print(data, type(data), id(data))
# int 는 integer의 약자.
# str 는 string

# data = str("python")
data = "python"
print(data, type(data), id(data))
# 첫번째와 두번째의 data가 참조하는 id가 다르다.
# 첫번째는 참조 연결이 끊기므로, 메모리에서 garbagecollecting 된다.
# 50 정수 클래스는 더 이상 참조가 불가능하다. 따라서 변수명을 겹치게 하면 안된다.

data1 = 50
data2 = "python"
print(data1, type(data1), id(data1))
print(data2, type(data2), id(data2))
# 파이썬의 변수는 어떤 객체의 ID든 저장이 가능하고 참조가 가능하다!
# 특정 객체의 ID를 저장해서 특정 객체를 참조하는 역할이 파이썬 변수의 역할이다.

data3 = 5.8 # 실수
print(data3, type(data3), id(data3)) # float

# Bool 타입 true / false
# 편집기의 자동완성 기능을 최대한 이용핧 것.
data4 = True
print(data4, type(data4), id(data4))

# 변수 선언 시 타입을 정의하지 않는게 가능한 이유는
# 변수에 타입과 내용, 크기를 담는 게 아닌, id를 담기 때문이다.

# class Mycls() :
#     pass

# 객체를 생성
# myData = Mycls() # 객체 생성 문법
# print(myData, type(myData), id(myData)) # <__main__.Mycls object at 0x000001CA63B23B20> 이 위치의 myCls를 이용해 만들어졌습니다.


class Mycls() :
    def __init__(self, arg):
        self.mdata = arg

myData = Mycls(5)
print(myData.mdata, type(myData), id(myData))

