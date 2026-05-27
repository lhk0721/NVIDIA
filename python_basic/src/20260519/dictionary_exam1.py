#시퀀스타입은 문자열, 리스트, 튜플이 해당된다.
#매핑 타입은 딕셔너리. dict 클래스

# 클래스 문법
# dict() == {}

dict1 = {} # 빈 딕셔너리 객체 생성

print(dict1, type(dict1))

dict2 = {50} #! 오류! set 타입으로 처리된다. key:value 로 짝지어야 함.

print(dict2, type(dict2))

dict3 = {'key1':50} # key 값은 const object가 와야 한다.

print(dict3, type(dict3))

# 사전에 항목을 추가.
dict4 = {} 
dict4["key1"] = 'value' #없는 key 값에 value 할당하면 key:value가 생성됨.

print(dict4, type(dict4))

dict4['def'] = 30
print(dict4, type(dict4))

# 사전의 value 읽기
print(dict4['def'])

# 사전의 valiue 수정
dict4["def"] = 50 # 기존 key에 값을 할당하면 업데이트된다.
print(dict4['def'])

# 항목 삭제.
del dict4['def'] # 여러 클래스에서 공통적으로 사용하는 del 키워드 사용. 다른 수단도 있긴 함.
print(dict4)

scoreDict = {'kor': 90, 'eng':70, 'math':30}

total = 0
for key in scoreDict: # 반복문에 사전이 올 경우 변수에 key가 전달된다.
    print(key,':', scoreDict[key],'|', end=' ')
    total += scoreDict[key] # 기타대입

print()
print('total: ',total)