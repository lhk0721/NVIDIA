
# 파이썬 기본 제공 -> 범위 데이터 생성하는 클래스
print(range(10)) # 반복문 돌리거나 타입변환 해야 내가 원하는 게 나온다.
print(list(range(10)))
# print(list(range(10,101)))
# print(list(range(30,41)))

# listdata = [] # not pythonic
# for x in range(30,41):
#     # print('print: ',x)
#     listdata.append(x)
#     print(listdata)

print('='*80)

listdata = [ x for x in range(0,10)] # 리스트 반복문 내포 문법. compilation. 반복문이 먼저 실행된다.

# 리스트 내포 문법에 여과 조건 추가
listdata = [ x for x in range(0,11) if x%2 == 0] # %: 나머지 연산
listdata = [ str(x+5) for x in range(0,11) if x%2 == 0]

print(listdata)
print(''.join(listdata)) # 579111315 여전히 문자열이다.

print('='*80)

mystr = "kbs, mbc, sbs"
# print(mystr.split(','))
# mystr = ['kbs', 'sbs', 'mbc']

# mylist = []
# for item in mystr.split(','):
#     mylist.append(item.strip())
    # print(item.strip())

mylist = [x.strip() for x in mystr.split(',')] #pythonic
print(mylist)


#문제. 리스트 내포 문법을 사용해서 아래 결과를 도출하세요
mystr1 = "Python, STudy, GooD"
mystr1  = [x.lower().strip() for x in mystr1.split(',')]

print(mystr1) 

mylistdata = ['python', 'frog', 'good']

for index, item in enumerate(mylistdata): # 인덱스와 항목을 동시에 변환. 각 항목에 인덱스 부여
    print(index, ":", item)
