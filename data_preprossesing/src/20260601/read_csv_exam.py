import numpy as np
import pandas as pd

# df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\scoreData.csv', header=None) # 상위 데이터를 자동으로 컬럼으로 인식한다. 첫 행을 데이터로 넣고 싶으면 header = None 넣어주기.

df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\scoreData.csv', names=['kor','eng','math','total']) # names-> 컬럼 넣어주기.
print(df)

