
## OOP 
# Object Oriented Programming 객체지향 언어. 
# 클래스 기반으로 객체를 생성해서 프로그램이 동작.
# 구조체 -> 정보를 담는 역할의 멤버변수. 
    # 정보만 담을 수 있다. 필요한 코드만 복사해 딸랑 가져간다. 흩어져 있는 의존성 함수들은 또 만든다.
# 클래스 -> 정보를 담는 역할의 멤버변수, 멤버변수를 접근해서 관리하는 멤버함수(메서드).
    # 캡슐화. 멤버함수까지 캡슐화함. 하나의 큰 자료형(타입)을 설계함. 용도에 맞는 적절한 그릇.

# 객체(실체문, instance)를 생성할 때 특정 클래스를 바탕으로 생성.

# 상속. 바퀴부터 다시 만들 필요는 없다. 기본 클래스를 물려받아 시작 

# 파이썬 기본 제공 클래스. -> int, float, bool, str, list, dict, tuple, set, ...

# 사용자 정의 클래스. 

# 클래스 정의 키워드 -> class 
# class MyCls('상속받을 부모 클래스'): # 클래스 정의
#     pass 

# MyCls 클래스를 바탕으로 객체를 생성해야지만 프로그램이 동작. 클래스는 그릇일 뿐. 함수 문법과 유사하다.
# 객체생성문법 -> 클래스명(). 
# data = MyCls()

# 멤버변수 를 등록하고 초기화하는 특수한 역할의 메서드.
class MyCls(): 
    
    # 생성자 역할의 함수. 객체가 생성되는 시점에서 자동으로 호출되는 특수한 메서드
    # 모든 특수한 역할의 메서드는 __
    def __init__(self, arg): # 초기화. arg는 내부 변수. __init__이 끝나기 전에 멤버변수에 넣어줘야 한다.
        print('__init__ 호출 완료')
        # 명시 안하면 디폴트 코드가 동작함.

        # 지역 등록 변수
        # local_val = 50 # 해당 함수 내에서만 동작하는 지역 등록 변수. 객체가 살아 있더라도 함수 내부에서만 살아있음. 메서드 안에서 임시적으로 사용되는 변수.

        # 멤버 변수        
        # 정보를 저장할 수 있는 멤버 변수를 등록하고 초기화. 객체 내부에 등록된 변수. 객체가 사라지지 않는 한 메모리에 살아있을 것이다.
        self.m_val = arg #해당 객체의 멤버변수다. 멤버 변수를 등록하고 초기화.    

    # 퍼블릭 인터페이스 메서드
    def InfoDisplay(self):  # self: 메서드를 어떤 객체가 호출했는지, 객체의 정보를 자동으로 전달.  메서드는 공유하지만 정보는 다르다. 어떤 객체가 InfoDisplay를 호출했는가? 객체의 중요한 정보를 담고있다. 없으면 멤버변수가 아닌 일반 함수.
        print('self.m_val: ', self.m_val)

data = MyCls(60) 
print(data.m_val) # 외부접근. 파이선은 기본적으로 외부 접근을 허용한다. 정보 은닉 위배. 되도록이면 지양하자. 클래스 내부에서만 접근하자.
print(data.InfoDisplay()) # 함수 자체가 반환값이 없기에 None이 반환된다. 'self.m_val:  100'은 내부에서 출력할 분 print에는 나올 값이 없다.

temp_data = MyCls(70)
print(temp_data.InfoDisplay()) # 내부 'print('self.m_val: ', self.m_val)'실행 후 None 반환
temp_data.InfoDisplay() # 내부 'print('self.m_val: ', self.m_val)'실행

listData = [0,50]
listData.sort() # self로 '[0,50]' 객체가 넘어감.
print(listData.sort()) # 내재된 반환값 None을 반환, 출력. 매서드라고 해도 함수 기능은 동일하다.

listexam = MyCls(80) # 오류!. 60을 받는 매개변수가 없다. self는 어떤 객체가 메서드를 호출했는지. 매서드를 공유하기 때문에. self 말고 매개변수를 추가해줘야 한다.

temp_myData = MyCls('python programming') # 다른 언어에서는 문제가 되겠지만, 파이썬에서는 동적 타이핑으로 문제가 없음. 변수가 바라보는 id가 넘어오기 때문에. 
print(temp_myData.m_val)