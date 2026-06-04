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

tipDf = sns.load_dataset('tips')
# print(tipDf.head(5))
#    total_bill   tip   sex   smoker day    time   size
# 0    16.990   1.010  Female   No    Sun  Dinner    2 
# 1    10.340   1.660    Male   No    Sun  Dinner    3 
# 2    21.010   3.500    Male   No    Sun  Dinner    3 
# 3    23.680   3.310    Male   No    Sun  Dinner    2 
# 4    24.590   3.610  Female   No    Sun  Dinner    4 

# tipDf.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   total_bill  244 non-null    float64 
#  1   tip         244 non-null    float64 
#  2   sex         244 non-null    category
#  3   smoker      244 non-null    category
#  4   day         244 non-null    category
#  5   time        244 non-null    category
#  6   size        244 non-null    int64   
# dtypes: category(4), float64(2), int64(1)
# memory usage: 7.4 KB
# PS C:\Users\25\Documents\gi
##
flightDf = sns.load_dataset('flights')
# flightDf.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 144 entries, 0 to 143
# Data columns (total 3 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   year        144 non-null    int64   
#  1   month       144 non-null    category
#  2   passengers  144 non-null    int64   
# dtypes: category(1), int64(2)
# memory usage: 2.9 KB

# print(flightDf.head(5))
#    year month  passengers
# 0  1949   Jan      112   
# 1  1949   Feb      118   
# 2  1949   Mar      132   
# 3  1949   Apr      129   
# 4  1949   May      121   

##
grpflightDf = pd.pivot_table(
	data=flightDf,
	index=['year'],
	values=['passengers'],
	aggfunc='sum'
)

# print(grpflightDf)
#       passengers
# year            
# 1949   126.667  
# 1950   139.667  
# 1951   170.167  
# 1952   197.000  
# 1953   225.000  
# 1954   238.917  
# 1955   284.000  
# 1956   328.250  
# 1957   368.417  
# 1958   381.000  
# 1959   428.333  
# 1960   476.167 

# sns.barplot(
# 	data=grpflightDf,
# 	x='year',
# 	y='passengers',
# 	palette='Set3'
# )

# plt.show()

## 
titnicDf = sns.load_dataset('titanic')

# print(titnicDf.head(5))
#    survived  pclass   sex     age   sibsp  parch  fare  embarked class   who    adult_male deck embark_town  alive  alone
# 0      0        3      male 22.000    1      0    7.250     S     Third    man      True    NaN  Southampton    no  False
# 1      1        1    female 38.000    1      0   71.283     C     First  woman     False      C    Cherbourg   yes  False
# 2      1        3    female 26.000    0      0    7.925     S     Third  woman     False    NaN  Southampton   yes   True
# 3      1        1    female 35.000    1      0   53.100     S     First  woman     False      C  Southampton   yes  False
# 4      0        3      male 35.000    0      0    8.050     S     Third    man      True    NaN  Southampton    no   True
# PS C:\Users\25\Documents\github\python_project> 

# titnicDf.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 15 columns):
#  #   Column       Non-Null Count  Dtype   
# ---  ------       --------------  -----   
#  0   survived     891 non-null    int64   
#  1   pclass       891 non-null    int64   
#  2   sex          891 non-null    object  
#  3   age          714 non-null    float64 
#  4   sibsp        891 non-null    int64   
#  5   parch        891 non-null    int64   
#  6   fare         891 non-null    float64 
#  7   embarked     889 non-null    object  
#  8   class        891 non-null    category
#  9   who          891 non-null    object  
#  10  adult_male   891 non-null    bool    
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    object  
#  13  alive        891 non-null    object  
#  14  alone        891 non-null    bool    
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)
# memory usage: 80.7+ KB

## age 행 별 기준으로 결측치 행을 제거
titnicDf.dropna(
	axis=0,
	how='any',
	subset=['age'],
	inplace=True
)

# titnicDf.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 714 entries, 0 to 890
# Data columns (total 15 columns):
#  #   Column       Non-Null Count  Dtype   
# ---  ------       --------------  -----   
#  0   survived     714 non-null    int64   
#  1   pclass       714 non-null    int64   
#  2   sex          714 non-null    object  
#  3   age          714 non-null    float64 
#  4   sibsp        714 non-null    int64   
#  5   parch        714 non-null    int64   
#  6   fare         714 non-null    float64 
#  7   embarked     712 non-null    object  
#  8   class        714 non-null    category
#  9   who          714 non-null    object  
#  10  adult_male   714 non-null    bool    
#  11  deck         184 non-null    category
#  12  embark_town  712 non-null    object  
#  13  alive        714 non-null    object  
#  14  alone        714 non-null    bool    
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)

## 'sex' 컬럼명을 'gender'로변경
titnicDf.rename(columns={'sex' : 'gender'},inplace=True)

# print(titnicDf.head(5))
#    survived  pclass  gender   age   sibsp  parch  fare  embarked class   who    adult_male deck embark_town  alive  alone
# 0      0        3      male 22.000    1      0    7.250     S     Third    man      True    NaN  Southampton    no  False
# 1      1        1    female 38.000    1      0   71.283     C     First  woman     False      C    Cherbourg   yes  False
# 2      1        3    female 26.000    0      0    7.925     S     Third  woman     False    NaN  Southampton   yes   True
# 3      1        1    female 35.000    1      0   53.100     S     First  woman     False      C  Southampton   yes  False
# 4      0        3      male 35.000    0      0    8.050     S     Third    man      True    NaN  Southampton    no   True

## pclass 별 fare_female, fare_male 각 평균 구하고 시각화

titnicPvDf = titnicDf.pivot_table(
	index='pclass',
	columns=['gender'],
	values='fare',
	aggfunc='mean'
)

titnicPvDf.columns = ['fare_female','fare_male']

# print(titnicPvDf)
#         fare_female  fare_male
# pclass                        
# 1        107.946      71.143  
# 2         21.951      21.113  
# 3         15.875      12.163  

# titnicPvDf.plot.bar()

# plt.show()

##
flightpvDf = flightDf.pivot(
	index='month',
	columns='year',
	values='passengers'
)

# print(flightpvDf)
# year   1949  1950  1951  1952  1953  1954  1955  1956  1957  1958  1959  1960
# month                                                                        
# Jan     112   115   145   171   196   204   242   284   315   340   360   417
# Feb     118   126   150   180   196   188   233   277   301   318   342   391
# Mar     132   141   178   193   236   235   267   317   356   362   406   419
# Apr     129   135   163   181   235   227   269   313   348   348   396   461
# May     121   125   172   183   229   234   270   318   355   363   420   472
# Jun     135   149   178   218   243   264   315   374   422   435   472   535
# Jul     148   170   199   230   264   302   364   413   465   491   548   622
# Aug     148   170   199   242   272   293   347   405   467   505   559   606
# Sep     136   158   184   209   237   259   312   355   404   404   463   508
# Oct     119   133   162   191   211   229   274   306   347   359   407   461
# Nov     104   114   146   172   180   203   237   271   305   310   362   390
# Dec     118   140   166   194   201   229   278   306   336   337   405   432

plt.figure(figsize=(10,9))

# sns.heatmap(
# 	data=flightpvDf,
# 	annot=True,
# 	fmt='d',
# 	linewidths=3,
# 	cmap='YlGnBu',
# 	cbar=False
# )
# plt.show()

##

# print(tipDf.describe()) # 수치 데이터만 선별하여 기본통계 제공
#        total_bill    tip    size 
# count   244.000   244.000 244.000
# mean     19.786     2.998   2.570
# std       8.902     1.384   0.951
# min       3.070     1.000   1.000
# 25%      13.348     2.000   2.000
# 50%      17.795     2.900   2.000
# 75%      24.127     3.562   3.000
# max      50.810    10.000   6.000


sns.set_style('whitegrid')
sns.boxplot(
	data=tipDf,
	x='day',
	y='total_bill',
	hue='smoker',
	palette='Set3'
)

plt.show()