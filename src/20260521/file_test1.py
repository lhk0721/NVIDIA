
## read as 활용 예제
# file_test.txt

# with open('file_test.txt','r') as f:
#     str = f.readline()

# # print(str) # python, test,programming, study, good
# strList = [ x.strip() for x in str.split(',') ]

# # print(strList) #['python', 'test', 'programming', 'study', 'good']

## 'R' 의 갯수를 파악하기

with open('setup.log','r') as log:
    str = log.read()

def FindCharFunc(str, char):
    num = 0
    for s in str:
        if(s == 'R'):
            num += 1
    return num

result = FindCharFunc(str,'R')
# print(result)


# print(str)
# strList = [x.strip() for x in str.split('\n')]
# print(strList)

## Csv 파일은 , 로 구분되는 텍스트파일이라고 보면 된다.
import pandas as pd

data = pd.read_csv('Health_info.csv')
# print(data) # 2차원 배열 형태의 dataFrame 데이터로 반환해준다.
# print(data.info())

# print(data['Weight'])
# print(data['Weight'].mean())


# with open('Health_info.csv', 'r') as hi:

## 
import random
listdata = ['감자','양파','대파','당근','피망']

print(random.choice(listdata))

## exe파일 만들기

# pip install pyInstaller #venv에서
# cd c:\Users\25\Documents\github\python_project\src\20260519
# python -m PyInstaller -w -F GUI_exam.py # 각 단어가 무슨 뜻인가?