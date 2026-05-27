import numpy as np
import pandas as pd

dictData = {'Hong':[90, 80, 70, 50, 75], 'Kim':[85, 95, 65, 55, 75], 'Park': [88, 93, 75, 72, 75], 'Lee':[55, 66, 77, 92, 75]}
df = pd.DataFrame(dictData, index=['kor', 'eng', 'math', 'music', 'science'])

## kim의 70점 이상인 것만 추출

# print(df)
# print(df['Kim'] >= 70)

# 불린 배열을 색인 인덱스로 사용해서 추출 -> 불린색인은 loc만 지원!!
# 불린 배열의 True 항목만 자동 추출

subset = df.loc[df['Kim'] >= 70,'Kim':'Park'].copy()
print(subset)

print('='*80)

print(df)

## 특정 column 데이터만 선택

subset2 = df[['Hong','Park']] # 여러 개는 항상 list 사용! 여러 column 선택 문법
print(subset2)