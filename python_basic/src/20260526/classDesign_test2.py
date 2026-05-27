
class PersonInfo():
    def __init__(self, *args):
        self.name, self.age, self.region = args

    def DisplayInfo(self):
        print(
            '이름: ', self.name,
            '나이: ', self.age,
            '지역: ', self.region
            )

per1 = PersonInfo('Hong', 30, 'Seoul')
per2 = PersonInfo('Kim', 50, 'Daejeon')
per3 = PersonInfo('Park', 40, 'Busan')

perList = [per1, per2, per3]
for per in perList:
    per.DisplayInfo() #'이름: ~, 나이: ~, 지역: ~'
    print('='*80)
    print