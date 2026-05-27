
class MyComInfo():
    def __init__(self, arg = 'Python Academy'):
        self.name = arg

    def DisplayName(self):
        print(self.name)

    def SetName(self, arg):
        self.name = arg

com1 = MyComInfo('AI Academy')
com1.DisplayName() # 'AI Academy'

com2 = MyComInfo()
com2.DisplayName() # 'Python Academy'

com2.SetName('Agent Academy')
com2.DisplayName() # 'Agent Academy'