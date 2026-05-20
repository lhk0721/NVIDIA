# for와 range를 활용해서 1부터 100까지 정수의 합을 계산해서 출력
sum = 0
for x in range(1,101):
    sum += x
# print(sum)

# "Python Programming, Ai Agent Programming" 'g' 문자의 갯수를 for 반복문 활용해서 합산 출력.

myString = "Python Programming, Ai Agent Programming"
quantity = 0
for x in myString:
    if(x == 'g'):
        quantity +=1
# print(quantity)

# 표현할 구구단의 단수를 입력받고, 해당 구구단의 내용을 출력(for구문 활용)

# step = int(input('출력할 구구단 단수 입력: '))
# for x in range(step + 1):
#     print(f'{step} * {x} = {(x * step)}')
    

# key 와 value를 서로 바꿔보기
myDict = {'a':1,'b':2,'c':3,'d':4}
newDict = {}

data = myDict.items()
# print(type(data)) # <class 'dict_items'> 튜플이다.

# for key in myDict:
#     # newDict[value] = key
#     newDict[myDict[key]] = key

for key, value in myDict.items():
    newDict[value] = key 

# print(newDict)

wordList = ['car', 'apple', 'cattle', 'bar', 'book', 'air', 'cat']

wordDict = {}
Msl = set()

# for 반복문 활용해서 구현
for item in wordList:
    if item[0] not in Msl:
        Msl.add(item[0])
        wordDict[item[0]] = [item]
    else:
        wordDict[item[0]].append(item)
        # print(type(wordDict[item[0]])) # class <class 'list'>

print(wordDict)


