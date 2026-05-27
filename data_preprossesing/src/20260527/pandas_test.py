import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt # 차트 시각화 라이브러리

import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
##
import pandas as pd
import numpy as np

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)


## font

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

dictData = {'Hong':[90, 80, 70, 50, 55], 'Kim':[85, 95, 65, 55, 95], 'Park': [88, 93, 75, 72, 45], 'Lee':[55, 66, 77, 92, 65]}
df = pd.DataFrame(dictData, index=['kor', 'eng', 'math', 'music', 'science'])

## 7호선, 
# subset = df.loc[df['Kim'] >= 70,'Kim':'Park'].copy()

my_df = pd.read_csv('src\\20260527\서울특별시_지하철 승하차 승객수.csv', encoding='CP949')


my_df['기준_날짜'] = pd.to_datetime(my_df['기준_날짜']) # 문자열 항목을 시계열 데이터로 바꿔라.
# print(my_df['기준_날짜'])
# my_df.info()
# print(my_df.head())

my_df.set_index('기준_날짜',inplace=True, drop=True)

# print(my_df.head())
# print(my_df.loc['2024-8-18'])

index_data = pd.date_range('2025.12.25',periods=30,freq='D') # 시계열의 범위 데이터를 생성
# print(index_data)

index_df = pd.DataFrame(np.arange(30,60), columns=['데이터'], index=index_data)

print(index_df['2025'])
##

# target = ['7호선', '3호선']

# # print(my_df['호선_명칭'])
# # print((my_df['호선_명칭'] target))

# # print(my_df['호선_명칭'])
	

# subset = my_df.loc[(my_df['호선_명칭'] == '7호선'), :].copy()

# print(subset)


