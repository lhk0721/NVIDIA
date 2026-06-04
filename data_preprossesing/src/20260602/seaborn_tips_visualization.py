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

df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\tips.csv')

## seaborn은 hue가 그루핑 역할을 대신해준다. 그루핑 하고 줄 필요가 없다.
# sns.lineplot(
# 	x='size',
# 	y='total_bill',
# 	data=df,
# 	hue='time'
# )

sns.barplot(
	x='size',
	y='total_bill',
	data=df,
	hue='time'
)

plt.show()