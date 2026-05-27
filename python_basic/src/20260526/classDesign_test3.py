

# 멤버함수는 __init__ 말고도 다 self 인자로 시작해야 하는가?
class MyCalData():
    def __init__(self,arg):
        self.myData = arg

    def AvgDisplay(self):
        sum = 0
        count = 0
        for i in self.myData:
            # print(i, type(i))
            sum += i[1]
            count += 1
        print('Avg: ', f'{sum/count:.2f}')

data = MyCalData([
    ('kim', 100),
    ('Park', 90),
    ('Hong', 70)
])

data.AvgDisplay() # 숫자에 대한 평균을 출력