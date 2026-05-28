import numpy as np
import pandas as pd
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from prettytable import PrettyTable  # 3.3.0 version 설치
import re
# import seaborn as sns


def prinf_df(df):
    table = PrettyTable(['']+ list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    print(str(table))
    print()


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
df = pd.read_excel('src\\20260528\youtube_rank_1000.xlsx')#0index_col=0) #
# df['Video'].astype('int64') 특정 컬럼 데이터를 일괄 타입변환
##
def Shorter(arg):
    shortName = arg.split(' ')
    # print(shortName[0])
    return shortName[0]

df['ChannelName'] = df['ChannelName'].map(lambda x: x.split()[0]).copy()


##
# print(df['Video'])

# def ToInt(arg):
# 	_str = (
# 		arg
# 		.strip('개')
# 		.replace(',','')
#     )
# 	return(int(_str))
	
# df['Video'] = df['Video'].apply(ToInt)

# df['Video'] = df['Video'].map(lambda x: int(x.strip('개').replace(',','')))

df['Video'] = df['Video'].map(lambda x: int(re.sub(r'[,개]','',x)))

# print(df)

df.sort_values(by=['Video'], ascending=False, inplace=True) # by값 리스트로 주면 여러 컬럼 정렬 가능
# prinf_df(df[['Video']].head(10))

# df[['Video']].plot.pie()
# plt.show()

## channel name col을 
# df2 = df['Video'].head(10).copy()
# print(df2)

# df2.plot.bar(color=[
# 	'lightskyblue',
# 	'lightsalmon',
# 	'lightpink',
# 	'lightblue',
# 	'lightseagreen',
	
#     'lightcoral',
# 	'indianred',
# 	'lightslategray',
# 	'lightcyan',
# 	'lemonchiffon'	
#     ])
# plt.savefig('src\\20260528.jpeg')
# plt.show()

## seaborn을 이용한 시각화
# df2 = df.head(10).copy()

color = [
	'lightskyblue',
	'lightsalmon',
	'lightpink',
	'lightblue',
	'lightseagreen'
	
    # 'lightcoral',
	# 'indianred',
	# 'lightslategray',
	# 'lightcyan',
	# 'lemonchiffon'	
    ]

# print(df2)

# sns.barplot(
# 	data=df2,
# 	x='ChannelName',
# 	y='Video',
# 	palette=color,
#     hue='ChannelName')

# plt.show()

##

data = df['Category'].value_counts() ## 시리즈를 반환

dataDf = pd.DataFrame(data=data)
# print(dataDf.index.name) # 엑셀에 넣을 때 index.name이 행 하나로 잡혀버린다.
dataDf.index.name ='' # index name 지워주기

# dataDf.columns.name = 통째로 변겅
dataDf.rename(columns={'count':'CategoryFreq'}, inplace=True)
dataDf_top5 = dataDf.head(5).copy()
print(dataDf_top5)

dataDf_top5.plot.pie(
                    x = dataDf_top5.index, 
                    y='CategoryFreq',
                    colors=color,
                    legend=False,
                    startangle=90,
                    wedgeprops={
                        'width':0.5,
                        'edgecolor':'black',
                        'linewidth':3
                    },
                    autopct='%.2f%%',
                    explode=[0.1]*len(dataDf_top5.index)
                    )
plt.show()