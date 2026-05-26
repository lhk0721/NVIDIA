import requests # 특정 URL의 웹페이지 정보를 요청하는 키워드
from bs4 import BeautifulSoup # 웹페이지 정보를 파이썬 객체화해서 파싱할 수 있게 지원해주는 패키지
# 무거워지지 않도록 특정 패키지의 특정 클래스만 포함
import re # 정규 표현식

## 웹 페이지 요청
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4&ackey=yyfens5e'

r = requests.get(url)  # 웹페이지 요청
html = r.text  # r.content Or r.text(한글로 보고 싶을 때) : 웹페이지 형태
# print(html)

## 파싱
# 가장 바른 파서가 lxml
soup = BeautifulSoup(html, 'lxml')  # 파서 지정

# print(type(soup))

##
#위 방법과 다른 find_all(), find() 메서드 활용
newtitlesoup = soup.find_all(
    class_ = 'sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1'
    ) # 리스트로 반환. 파라미터는 'class_'
# print(newtitlesoup)

headLines = [x.text for x in newtitlesoup]
print(headLines)
