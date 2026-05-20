dictData = {'kor': 90, 'eng': 70, 'math': 80}

print("py" in "python") # 문자열 객체의 in 연산

print('kor' in dictData) # dict의 in 연산은 해당 dict에 key가 있냐 없냐를 체크한다.

if 'music' in dictData:
    print(dictData['kor'])
else:
    print("key 없음!")

# get
# print(dictData['music']) # 프로그램이 뻗어버린다.
print(dictData.get('kor',None)) # 중요! get은 예외처리를 지원한다. 두번째 인자로 예외값을 지정할 수 있다. default 는 None. 하지만 명시하는 습관을 들이자. get 메서드는 기억해두자.
print(dictData.get('music',None))

while True:
    inputData = input('과목을 입력: ')
    if(dictData.get(inputData,None)): # key가 있으면 해당 key에 대한 vlaue를 반환한다. 없으면 뒤에 명시한 값을 반환한다.
        print(dictData[inputData])
    else:
        print('해당 과목은 없음!')