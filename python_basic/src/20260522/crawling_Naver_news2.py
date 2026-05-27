import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import re 

## 웹 페이지 요청
url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EB%B0%98%EB%8F%84%EC%B2%B4'

r = requests.get(url) 
html = r.text
# print(html)

## 파싱

#sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1

soup = BeautifulSoup(html, 'lxml')  # 파서 지정

newsTitleList = soup.find_all(
    class_='sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1'
    )

# print(newsTitleList[0].text)

##취합

newsDataList = [item.text for item in newsTitleList]

# print(newsDataList)

myNewsDf = pd.DataFrame(newsDataList, columns=['뉴스제목'])
# print(myNewsDf)

myNewsDf.to_excel("naverNews.xlsx", index = False)