import re # regular expression, 정규표현식

## 정규표현식 regular
# 문자열에서 특정 패턴을 검색하거나 치환할 때 사용.
# match, search, findall
# 사이드 패키지가 아닌 내장

# strData = '파이썬 Ai PYThON3 Programming97, 성장 2026 ALL In ONe !! 빅테크'

# 문자열 매서드가 아닌, 특정 패턴을 활용하여 특정 문자열을 찾고(검색), 분할하고, 치환(삭제)할 수 있는 정규표현식 매서드를 지원한다.

# 검색. findall()만 기억하면 된다.
# re.findall() #패턴에 매칭된 모든 내용을 리스트 형태로 반환한다.

# 영문 대문자 패턴. A,B,C,...,Z 이런 경우 범위를 활용 A-Z f'{}' 쓰듯이 r''로 사용
# result = re.findall(r'A', strData)
# result = re.findall(r'A-Z',strData)
# print(result)

## 조건문과 연계
# 빈 문자열은 false로 인식한다.
# 리스트에 내용물이 있으면 true, 없으면 false. findall은 리스트로 반환한다.
# print(result)

# if result:
#     print('있어요')
# else:
#     print('없어요')

# # not 연산자

# if not result:
#     print('없어요')
# else:
#     print('있어요')

## 범위
# result = re.findall(r'[ABC]',strData) # A,B,C 따로 본다. 여러 개의 패턴을 하나로 묶어서 표현할 때.
# result = re.findall(r'[A-Z]',strData) # 범위는 '-'로 표현한다. 각각으로 표현.

# 단어 단위로 보고 싶을 땐? + 메타문자. 
# +앞에 있는 패턴이 하나 이상인 문자를 찾아서 반환해라.
# result = re.findall(r'[A-Z]+',strData) # +를 붙인다. 연속된 것은 모두 찾아준다.

## 영문 소문자 패턴

# result = re.findall(r'[A-Z]',strData) # 영문 대문자를 찾아서 모두 개별출력
# result = re.findall(r'[a-z]',strData) # 영문 소문자를 찾아서 모두 개별출력
# result = re.findall(r'[a-z]+',strData) # 하나 이상인 영문 소문자를 찾아서 모두 출력

## 조합
# result = re.findall(r'[A-Za-z]+',strData) # 영문 대소문자로 이루어진 단어를 찾아 출력.
# result = re.findall(r'[A-Z,a-z]+',strData) # ',' 넣으면 문자열에서 ',' 도 포함해서 찾아버릴 수 있다.

## 한글
# result = re.findall(r'[ㄱ-힣]+',strData) # 한글 하나 이상인거 모두 찾아서 출력
# 한글 완성형의 끝은 힣이다!! 
# 가-힣(완성형 범위) 또는 ㄱ-힣(조합형 범위)


## 숫자 문자
# result = re.findall(r'[0-9]+',strData) # 한글 하나 이상인거 모두 찾아서 출력

# result = re.search(r'[A-Z]+', strData) # 중간에 있어도 찾아주는 것.
# result = re.search(r'[TE]+', strData) # 가장 먼저 만난 걸 찾아주는 것.

strData = 'Ai반 Ai AiAi구축 Ai프로그램 Ai'

# 교안 참고 복습할 것
# \w 임의의 문자를 나타냄
# . : .위치에 한 문자 매치
# [^] : 아닌 것.
# ^[] : -로 시작하는 것
# * : * 메타문자 기준으로 앞에 패턴이 0개 이상인 것을 매칭
# result = re.findall(r'Ai\w*',strData) # ai가 포함된 모든 문자
# result = re.findall(r'Ai\w+',strData) # 임의의 문자가 한개 이상
# result = re.findall(r'Ai*',strData) # *: 있어도 되고 없어도 되고
# result = re.findall(r'Ai*',strData) #



print(result)
