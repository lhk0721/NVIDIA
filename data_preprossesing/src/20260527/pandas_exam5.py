import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt # 차트 시각화 라이브러리

import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

## font

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

dictData = {'Hong':[90, 80, 70, 50, 55], 'Kim':[85, 95, 65, 55, 95], 'Park': [88, 93, 75, 72, 45], 'Lee':[55, 66, 77, 92, 65]}
df = pd.DataFrame(dictData, index=['kor', 'eng', 'math', 'music', 'science'])

## 삭제 문법

# 특정 열 하나 삭제 -> del 키워드. 여러개 하려면 반복문 써야 한다.
# del df['Park']
# print(df)

# 특정 column이나 여러개의 column 동시 삭제하는 방법.
# numpy 2차원 단위의 행,열 축 -> axis = 0/1. 어느 축으로 움직일 것이냐?
# drop() 메서드

# df.drop(['Hong','Park'], axis=1, inplace = True) # default axis = 0. 사본 객체를 생성하기 때문에, 변수에 담아주거나, return 값 None 해줘야 한다.
# print(df) # inplace = True 이면 직접 반영 return None 한다. 원본을 따로 출력해야 한다., False이면 사본 객체 생성
# dataFrame은 메모리를 많이 잡아먹는다. inplace가 필수인 시점이 온다..

## 행 삭제

# df.drop(['eng','music'], axis=0, inplace = True)
# print(df)

## 인덱스를 한글로 바꿔보자
print(df)
print('='*80)
df.index = ['국어', '영어', '수학', '음악', '과학']
print(df)

# plt.plot 기능을 pandas에 포함시켜 버렸다.
df.plot.bar()
plt.show()