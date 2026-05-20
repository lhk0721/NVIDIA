
max = 0
# max 변수에는 두 변수의 큰 값을 체크해서 저장

data1 = 50
data2 = 90

# if data1>data2:
#     max = data1
# else:
#     max = data2

# print(max)

# 간단한 if-else 구문을 한 라인으로 표현한 것이 조건표현식이다.
# python에는 switch case가 없다.
max = data1 if (data1 > data2) else data2

# 조건표현식과 리스트 내포 구문을 하나로 표현해서 사용.
listData = [ '짝' if (x%2==0) else '홀' for x in range(1,9)]
print(listData)


# 리스트 항목 여과기. 조건에 맞는 것만 넘김. 리스트 내포 조건표현식과 달리 뒤에 위치

wordList = ['book','car', 'apple', 'python', 'ai']
#wordList의 문자열 항목 중 문자열의 길이가 4 이상인 문자열만 새 리스트에 저장 출력

newWordList = [word for word in wordList if (len(word) >= 4)] # 필터링 구문
print(newWordList)
