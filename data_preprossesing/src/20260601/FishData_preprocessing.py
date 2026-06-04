import numpy as np
import pandas as pd
import re
from prettytable import PrettyTable  # 3.3.0 version 설치
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

def prinf_df(df):
    table = PrettyTable(['']+ list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    print(str(table))
    print()

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)
np.set_printoptions(precision=3)

##

df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\Fish.csv')

# df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 159 entries, 0 to 158
# Data columns (total 7 columns):
#  #   Column   Non-Null Count  Dtype  
# ---  ------   --------------  -----  
#  0   Species  159 non-null    object 
#  1   Weight   159 non-null    float64
#  2   Length1  159 non-null    float64
#  3   Length2  159 non-null    float64
#  4   Length3  159 non-null    float64
#  5   Height   159 non-null    float64
#  6   Width    159 non-null    float64

## 몇종류의 물고기가 있는가?
# print(len(df['Species'].unique()))
# 7 species
# ['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']

##

# print(df.head(5))
#   Species  Weight  Length1  Length2  Length3   Height   Width
# 0   Bream   242.0     23.2     25.4     30.0  11.5200  4.0200
# 1   Bream   290.0     24.0     26.3     31.2  12.4800  4.3056
# 2   Bream   340.0     23.9     26.5     31.1  12.3778  4.6961
# 3   Bream   363.0     26.3     29.0     33.5  12.7300  4.4555
# 4   Bream   430.0     26.5     29.0     34.0  12.4440  5.1340

df2 = df.iloc[:,:3].copy()
# print(df2.head(5))
#   Species  Weight  Length1
# 0   Bream   242.0     23.2
# 1   Bream   290.0     24.0
# 2   Bream   340.0     23.9
# 3   Bream   363.0     26.3
# 4   Bream   430.0     26.5

# df2.columns = ['Species', 'Weight', 'Length']
df2.rename(columns={'Length1':'Length'}, inplace=True)

# print(df2.head(5))
#   Species  Weight  Length
# 0   Bream   242.0    23.2
# 1   Bream   290.0    24.0
# 2   Bream   340.0    23.9
# 3   Bream   363.0    26.3
# 4   Bream   430.0    26.5

## plt.scatter() 산점도
# x축을 length
# y축을 weight
# plt.scatter(
# 	x=df2['Length'],
# 	y=df2['Weight']
# 	)

# g = sns.lmplot(
#     data=df2,
#     x="Length", 
# 	y="Weight", 
# 	hue="Species", # grooping
#     height=5,
# 	fit_reg=False
# )

# Use more informative axis labels than are provided by default
# g.set_axis_labels("Fish Length", "Fish Weight")

# plt.show()

##
# print(df.head())
#   Species  Weight  Length1  Length2  Length3   Height   Width
# 0   Bream   242.0     23.2     25.4     30.0  11.5200  4.0200
# 1   Bream   290.0     24.0     26.3     31.2  12.4800  4.3056
# 2   Bream   340.0     23.9     26.5     31.1  12.3778  4.6961
# 3   Bream   363.0     26.3     29.0     33.5  12.7300  4.4555
# 4   Bream   430.0     26.5     29.0     34.0  12.4440  5.1340
df3 = df.drop(columns=['Length2','Length3']).copy()

# print(df3.head(5))

#   Species  Weight  Length1   Height   Width
# 0   Bream   242.0     23.2  11.5200  4.0200
# 1   Bream   290.0     24.0  12.4800  4.3056
# 2   Bream   340.0     23.9  12.3778  4.6961
# 3   Bream   363.0     26.3  12.7300  4.4555
# 4   Bream   430.0     26.5  12.4440  5.1340

df3.rename(columns={'Length1':'Length'},inplace=True)
# print(df3.head(5))
#   Species  Weight  Length   Height   Width
# 0   Bream   242.0    23.2  11.5200  4.0200
# 1   Bream   290.0    24.0  12.4800  4.3056
# 2   Bream   340.0    23.9  12.3778  4.6961
# 3   Bream   363.0    26.3  12.7300  4.4555
# 4   Bream   430.0    26.5  12.4440  5.1340

## Height, Width의 평균을 계산해서 출력

df3_pivotTable = pd.pivot_table(
	data=df3,
	index=['Species'],
	values=['Height','Width'],
	aggfunc='mean'
)

# print(df3_pivotTable)
#               Height     Width
# Species                       
# Bream      15.183211  5.427614
# Parkki      8.962427  3.220736
# Perch       7.861870  4.745723
# Pike        7.713771  5.086382
# Roach       6.694795  3.657850
# Smelt       2.209371  1.340093
# Whitefish  10.027167  5.473050

## Height, Width 각 5씩 가산.

df3_pivotTable[['Height', 'Width']] = (
	df3_pivotTable[['Height', 'Width']].map(lambda x: x+5)
)

# print(df3_pivotTable)
#               Height      Width
# Species                        
# Bream      20.183211  10.427614
# Parkki     13.962427   8.220736
# Perch      12.861870   9.745723
# Pike       12.713771  10.086382
# Roach      11.694795   8.657850
# Smelt       7.209371   6.340093
# Whitefish  15.027167  10.473050