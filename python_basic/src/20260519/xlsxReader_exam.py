# C:\Users\25\python_project\python_basic\20260519\dictionary_exam2.py 산출물 열기

import pandas as pd

mydf = pd.read_excel(r'C:\Users\25\Documents\github\python_project\dataset\mydf.xlsx', index_col=0) # 엑셀 파일의 내용을 읽어서 데이터프레임 객체로 변환, index_col = 0 -> 인덱스를 컬럼으로 읽는 걸 방지.

print(mydf)

