
## 문제 1
class MyCalList():
    def __init__(self, *arg):
        self.list1, self.list2 = arg

    def SumOfList(self):
        # sumList = [
        #     self.list1[i] + self.list2[i] 
        #     for i,_ in enumerate(self.list1)
        # ]
        sumList = [a+b for a,b in zip(self.list1, self.list2)]
        print(sumList)
        
data = MyCalList([5,6,7],[8,9,10])
# data.SumOfList() # [13, 15, 17]

## 문제 2

class MyCalList2():
    def __init__(self, *arg):
        self.list1, self.list2 = arg
        # sumList = [
        #     self.list1[i] + self.list2[i] 
        #     for i,_ in enumerate(self.list1)
        # ]

        sumList = [a+b for a,b in zip(self.list1,self.list2)]

        # print(sumList)

    def SubOfList(self):
        # subList = [
        #     self.list1[i] 
        #     for i,_ in enumerate(self.list1) 
        #     if (self.list1[i] not in self.list2)
        # ]

        # subList = [a for a in self.list1 if a not in self.list2]

        subList = list(set(self.list1) - set(self.list2))
        print(subList)


data2 = MyCalList2([5,6,7,9],[8,9,5,10]) #[13, 15, 12, 19]
# data2.SubOfList() # [6,7] OR [7,6]

## 문제 3

class studentScore():
    def __init__(self, name, *arg):
        self.name = name
        self.scoreList = arg

    def sum(self):
        return sum(self.scoreList)
    
    def avg(self):
        return self.sum()/len(self.scoreList)
    
    def ScoreDisplay(self):
        print(f'\t{self.name}', self.sum(), self.avg(),sep='\t|\t')

StudentList = [
    studentScore('Hong', 80, 60, 70, 90),
    studentScore('Kim', 90, 70, 80, 90),
    studentScore('Park', 80, 60, 70, 90),
    studentScore('Lee', 80, 60, 70, 90)
]

print('\tname', 'sum', 'avg',sep='\t|\t')

for i in StudentList:
    i.ScoreDisplay()

# (i.ScoreDisplay() for i in StudentList)
# {i.ScoreDisplay() for i in StudentList}