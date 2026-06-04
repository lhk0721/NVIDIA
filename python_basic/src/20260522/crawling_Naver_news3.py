import pandas as pd
import re

newsDf = pd.read_excel(r"C:\Users\25\Documents\github\python_project\dataset\naverNews.xlsx")

print(newsDf)

# print(newsDf)
# print(newsDf['뉴스제목'][0])

# for item in newsDf['뉴스제목']:
#     eng = re.sub(r'[^가-힣\s]','',item)
#     print(eng)
#     print('-'*80)

# print('='*80)

# for item in newsDf['뉴스제목']:
#     kor = re.findall(r'[가-힣]+',item)
#     _kor = ''.join(kor)
#     print(_kor)
#     print('-'*80)

##

def NewsTitleFiltering(title):
    # print('title: ',title)
    # print(re.sub(r'[^가-힣\s]','',title))
    return re.sub(r'[^가-힣\s]','',title) # 반영시키기

newsDf['뉴스제목'] = newsDf['뉴스제목'].apply(NewsTitleFiltering) # 함수 명만 온다.

print('='*80)

print(newsDf)

newsDf.to_excel(r"C:\Users\25\Documents\github\python_project\dataset\naverNews_filtering.xlsx",index=False)