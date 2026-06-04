import numpy as np
import pandas as pd
import platform
import matplotlib.pyplot as plt
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

##
df = pd.read_excel(r'C:\Users\25\Documents\github\python_project\dataset\youtube_rank_1000.xlsx',index_col=0)
# df.info()
# print(df.head(10))

## ChannelName 정리할 것임.

# def Shorter(arg):
#     shortName = arg.split(' ')
#     # print(shortName[0])
#     return shortName[0]

# df['ChannelName'] = df['ChannelName'].apply(Shorter)

# df['ChannelName'] = df['ChannelName'].map(lambda x: x.split()[0])
# print(df)

## 저장

# df.to_excel('src\\20260528\youtube_data.xlsx')

##

# print(df['Category'].unique())

categoryList = dict()

def CategoryFerq(arg):
    global categoryList
    category = arg.strip('[').strip(']')
        
    if category not in categoryList:
        categoryList[category] = 1
    else:
        categoryList[category] += 1

df['Category'].apply(CategoryFerq)

# print(categoryList)

myDf = pd.DataFrame.from_dict(categoryList,orient='index',columns=['Freq'])
myDf.sort_values('Freq', ascending=False, inplace=True)
# print(myDf)

df2 = myDf.iloc[:5,0].copy()
print(type(df2))

df2.plot.pie()
plt.show()
