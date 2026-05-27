
# 객체가 생성될때 '객체생성완료! 를 출력되게 해보자.'
class MyDataControl(): # 클래스 정의. 객체 생성되기 전엔 뭐 안한다.
    def __init__(self,*args): # 등록, 초기화 역할에 국한하자.
        print('객체 생성 완료!')
        # self.data = [x for x in args]
        # self.data = list(args)
        self.data = args

    def SumOfData(self):
        sum = 0
        for x in self.data:
            sum += x

        print('total: ', self.sum) # 합을 출력하게 해보자.

# 객체생성
myData = MyDataControl(50,60,70,80,90) # 객체생성문. 객체를 메모리에 생성했으면 변수로 참조해야 한다. 생성자가 객체를 생성한다. 소멸자는 가비지컬렉터가 있어 필요 없다.
myData.SumOfData()

