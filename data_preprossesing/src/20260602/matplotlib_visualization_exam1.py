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

# df = pd.read_excel(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260602\youtube_data.xlsx', index_col=0)
# df.info()
##
# fig = plt.figure(figsize=(10,6))

# ax1 = fig.add_subplot(1,2,1)
# ax2 = fig.add_subplot(1,2,2)

# ax1.bar([10,20,30,40,50],[20,60,80,90,120]) # 차트 렌더링. default: linear
# ax2.plot([10,20,30,40,50],[20,60,80,90,120]) 
# plt.show() # 화면에 출력
# plt.savefig(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260602\linechart.jpeg') # 이미지 파일로 저장

##
fig, axis = plt.subplots(1,2,figsize=(12,6))
axis[0].bar([10,20,30,40,50],[20,60,80,90,120]) # 차트 렌더링. default: linear
axis[1].plot([10,20,30,40,50],[20,60,80,90,120]) 

plt.show()