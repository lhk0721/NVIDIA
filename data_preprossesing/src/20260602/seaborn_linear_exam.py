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
fig, axis = plt.subplots(2,1)

dateidx = np.arange(0,100,10)

data = np.random.randn(10,4).cumsum(axis=0)
print(data)
# [[ 1.054 -1.851 -0.21  -1.459]
#  [ 0.32  -2.18   0.245 -0.648]
#  [ 0.695  0.277 -0.957 -0.173]
#  [-1.553  0.657 -1.442 -0.762]
#  [-2.803  2.582 -1.014 -1.2  ]
#  [-4.046  2.322 -0.988 -1.577]
#  [-3.591  1.968 -0.948 -1.813]
#  [-3.359  1.364 -2.652 -1.594]
#  [-1.762  2.712 -1.431 -2.493]
#  [-2.748  3.73  -0.395 -0.996]]

df = pd.DataFrame(
	data, 
	index=dateidx, 
	columns=list('ABCD')
)

# print(df)
#            A         B         C         D
# 0  -1.274577 -1.510505 -2.052623  1.254524
# 10  0.298362 -0.961062 -2.540982  1.970934
# 20  0.201830 -1.154512 -2.304531  3.627930
# 30  0.208561 -1.529680 -1.157849  2.859569
# 40  1.512357 -1.883944 -0.394305  3.939591
# 50  3.095830 -1.752315 -0.149042  3.485977
# 60  3.013676 -1.107580  1.773060  4.102602
# 70  4.466783 -0.104049  2.799853  3.642594
# 80  4.499093 -1.398311  4.087138  5.276506
# 90  5.078002  0.135250  2.185375  5.971812

# sns.lineplot(ax=axis[0], data=df)
# sns.lineplot(ax=axis[1], data=df['C'])

sns.barplot(ax=axis[0], data=df)
sns.barplot(ax=axis[1], data=df['C'])

plt.show()

