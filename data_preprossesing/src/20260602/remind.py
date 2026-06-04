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
df = pd.read_excel(r'C:\Users\25\Documents\github\python_project\dataset\youtube_data.xlsx', index_col=0)
df.info()
#  #   Column       Non-Null Count  Dtype 
# ---  ------       --------------  ----- 
#  0   ChannelName  1000 non-null   object
#  1   Category     1000 non-null   object
#  2   Subscriber   1000 non-null   object
#  3   View         1000 non-null   object
#  4   Video        1000 non-null   object

# 1. 결측치가 있는가? 2. 데이터 타입?

##

df['Subscriber'] = df['Subscriber'].map(lambda x: int(re.sub(r'만','0000',x)))
# df['Subscriber'] = df['Subscriber'].apply(lambda x: int(x.replace('만','0000')))
# df['Subscriber'] = df['Subscriber'].str.apply(lambda x: int(x.replace('만','0000')))

df.info()

##

pvdf = df.pivot_table(
    index = 'Category',
    values = 'Subscriber',
    aggfunc = 'mean'
)

grpdf = df.groupby('Category')[['Subscriber']].mean().copy()

# print(grpdf)

grpdf.sort_values(by='Subscriber',ascending=False,inplace=True)
grpdf_top7 = grpdf.head(7).copy()

# print(grpdf_top7)
grpdf_top7.plot.bar(rot=0)
plt.show()


