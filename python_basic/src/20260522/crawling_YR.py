import requests 
from bs4 import BeautifulSoup 
import re 
import pandas as pd

## 웹 페이지 요청
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)  
html = r.text

## 파싱

soup = BeautifulSoup(html, 'lxml')  

## 추출

#받아오기
data = soup.find_all('td', class_='subject') #bs의 경우 (태그, className)

datalist = [x.find_all('a')[0].text.strip() for x in data]

# print(datalist)

# stringData = '\n'.join(datalist)

# print(stringData)
## 취합

# 영문만 남겨보자.
# result = re.findall(r'[a-zA-Z\s]+',stringData)
# result = re.sub(r'[^a-zA-Z\s]+','',stringData)
# print(result)

##
# 리스트 내포와 정규표현식을 이용해서 한줄로 영문 대소문자만 남겨보자.
# result = [re.sub(r'[^a-zA-Z\s]+'.strip(),'',x) for x in datalist]

##
mydf = pd.DataFrame(datalist,columns=['제목'])
mydf.to_excel(r"C:\Users\25\Documents\github\python_project\dataset\youtubedata.xlsx",index=False)

# print(mydf)
