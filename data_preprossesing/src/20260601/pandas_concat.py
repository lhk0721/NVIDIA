import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\tips.csv')

# print(df['day'].unique())
subset1 = df.loc[df['day'].isin(['Sat','Fri']),:]

subset2 = df.loc[df['day'] == 'Sat',:]
subset3 = df.loc[df['day'] == 'Fri',:]
# print(subset2)
# print(subset3)

df_con = pd.concat([subset2,subset3], axis=0 ) 
# axis=1은 잘 안쓴다. (키(인덱스)가 일치하지 않기에)? NaN이 상호 위치에 생긴다. 행축으로 합쳐라.
# series 간 concat도 잘 안쓴다.
# keys 로 상위 col 인덱스도 만들어줄 수 있다.
print(df_con)