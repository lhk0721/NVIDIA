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

##
irisDf = sns.load_dataset('iris')

# irisDf.info()
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   sepal_length  150 non-null    float64
#  1   sepal_width   150 non-null    float64
#  2   petal_length  150 non-null    float64
#  3   petal_width   150 non-null    float64
#  4   species       150 non-null    object 
# dtypes: float64(4), object(1)

# print(irisDf['species'].unique())
# ['setosa' 'versicolor' 'virginica']

# print(irisDf.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0     5.100        3.500         1.400        0.200      setosa
# 1     4.900        3.000         1.400        0.200      setosa
# 2     4.700        3.200         1.300        0.200      setosa
# 3     4.600        3.100         1.500        0.200      setosa
# 4     5.000        3.600         1.400        0.200      setosa

## irisDf를 sns lmplot으로 산점도 시각화. 3종류를 하나의 plot 창에 동시 시각화, fig_reg = False.
# 이 때 x축은 sepal length, y축은 petal width
# irisgrpDf = irisDf.pivot_table(
# 	index='species',
# 	columns=['sepal_length','petal_width'],
# 	values=
	
# )

sns.lmplot(
	data=irisDf,
	x='sepal_length',
	y='petal_width',
	fit_reg=False,
	hue='species'
)
plt.show()


##
titanicDf = sns.load_dataset('titanic')

##
tipDf = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\tips.csv')

# tipDf.info()
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   total_bill  244 non-null    float64
#  1   tip         244 non-null    float64
#  2   gender      244 non-null    object 
#  3   smoker      244 non-null    object 
#  4   day         244 non-null    object 
#  5   time        244 non-null    object 
#  6   size        244 non-null    int64  
# dtypes: float64(2), int64(1), object(4)

# print(tipDf.head())
#    total_bill   tip  gender smoker day    time   size
# 0    16.990   1.010  Female   No    Sun  Dinner    2 
# 1    10.340   1.660    Male   No    Sun  Dinner    3 
# 2    21.010   3.500    Male   No    Sun  Dinner    3 
# 3    23.680   3.310    Male   No    Sun  Dinner    2 
# 4    24.590   3.610  Female   No    Sun  Dinner    4 

##
tipDf['tip_pct'] = (tipDf['tip']/tipDf['total_bill'])
# print(tipDf.head())

#    total_bill   tip  gender smoker day    time   size  tip_pct
# 0    16.990   1.010  Female   No    Sun  Dinner    2    5.945 
# 1    10.340   1.660    Male   No    Sun  Dinner    3   16.054 
# 2    21.010   3.500    Male   No    Sun  Dinner    3   16.659 
# 3    23.680   3.310    Male   No    Sun  Dinner    2   13.978 
# 4    24.590   3.610  Female   No    Sun  Dinner    4   14.681 

##
# sns.set_style("darkgrid")

# fig, axis = plt.subplots(1,2,figsize=(10,6)) #subplots로 하면 axis가 알아서 받는다.


# sns.regplot(
# 	x=tipDf['total_bill'],
# 	y=tipDf['tip'],
# 	ax=axis[0],
# 	fit_reg=True,
# 	color='orange'
# )
# sns.regplot(
# 	x=tipDf['total_bill'],
# 	y=tipDf['tip'],
# 	ax=axis[1],
# 	fit_reg=False,
# 	color='blue'
# )

# plt.show()

##
