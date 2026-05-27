import re
import os

strData = '파이썬,Ai PYThON3#Programming97@성장 2026 ALL In ONe !! 빅테크'

# findall() 패턴을 이용해서 특정 문자를 검색 
# split() 패턴을 이용해서 특정 문자열을 분할

## re를 안쓰고 split
# strData.split(',') # 리스트로 반환. split을 연이어 쓸 수 없다.
# 문자열 매서드로 여러 개의 구분자를 활용해 분할하기에는 문제점을 가지고 있다.
# 이를 해결하기 위해 패턴을 이용하여 문자를 분할하여 사용.

## 정규표현식을 사용할 경우
# \n: 개행
# \s: 스페이싱
# result = re.split(r'[,\s#@]',strData)

## re 안쓰고 replace()
# result = strData.replace('seperator','') # replace(k,'')삭제 replace(k,'')공백으로 둠
# print(result)

## sub() replace처럼 치환시키는 역할
# sub 문자열 replace 값과 유사.
result = re.sub(r'[,#@\s]',', ',strData) # 정규표현식 패턴을 사용 sub(패턴,치환값,문자열)
# print(result)
root = os.getcwd()
cwd = root + '\\src\\20260522'
dest = cwd + '\\readData.txt'
with open(dest,'w',encoding='UTF-8') as f:
    f.write(result)
