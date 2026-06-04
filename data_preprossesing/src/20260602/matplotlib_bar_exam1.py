import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
pd.set_option('display.colheader_justify','center')  # 컬럼 중앙 출력
pd.set_option('display.float_format', '{:.3f}'.format) #  float 형식 소숫점 3자리 표현

# 엑셀파일을 전처리해서 시각화
# index_col = 0 : 0번째 컬럼을 인덱스로 설정해서 읽어들임
df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\tips.csv')
# df.info()
print(df.head())

#    total_bill   tip  gender smoker day    time   size
# 0    16.990   1.010  Female   No    Sun  Dinner    2 
# 1    10.340   1.660    Male   No    Sun  Dinner    3 
# 2    21.010   3.500    Male   No    Sun  Dinner    3 
# 3    23.680   3.310    Male   No    Sun  Dinner    2 
# 4    24.590   3.610  Female   No    Sun  Dinner    4 

##
pvdf = df.pivot_table(
	index='day',
	values=['total_bill','tip'],
	aggfunc='sum'
)

# print(pvdf)
#         tip   total_bill
# day                     
# Fri   51.960    325.880 
# Sat  260.400   1778.400 
# Sun  247.390   1627.160 
# Thur 171.830   1096.330 

##
# pandas Rendering <-> matplotlib Rendering
# pvdf.plot.bar()
# pvdf.plot.bar(stacked=True)
# pvdf.plot.barh(stacked=True)
fig,ax = plt.subplots(2,1,figsize=(10,6))
pvdf.plot.bar(ax=ax[0], stacked=True, rot=0)
pvdf.plot.barh(ax=ax[1], stacked=True)
plt.show()
# matplotlib은 나란한 차트를 쓰려면 위치를 나눠줘야 한다.

##
# plt.barh(
# 	pvdf['day'],
# 	pvdf['tip']
# )

# plt.show()
