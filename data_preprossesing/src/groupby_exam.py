import numpy as np
import pandas as pd

# 그룹핑 -> groupby, pivot_table

# groupby -> 1. split. 2. apply. 3. combine (내부적으로 동작)

df = pd.DataFrame(
    {
        'subject': ['kor', 'eng','kor', 'eng', 'math','kor', 'math'],
        'score':   [   70,    80,   90,    85,     96,   54,     80]
    }
)

# print(df)
#   subject  score
# 0     kor     70
# 1     eng     80
# 2     kor     90
# 3     eng     85
# 4    math     96
# 5     kor     54
# 6    math     80
# 1. kor, eng, math 각 그룹으로 분할
# 2. 각 그룹에 대해 집계
# 3. 시리즈 하나로 합치기

## groupby(기준키)[집계통계함수를 적용할 컬럼].집계통계함수()
# gbsum = df.groupby('subject')['score'].sum()
# print(gbsum)
# subject
# eng     165
# kor     214
# math    176
# Name: score, dtype: int64
# -> 시리즈로 반환

# gbsumdf = pd.DataFrame(gbsum) 또는
gbsum = df.groupby('subject')[['score']].sum()
print(gbsum) 
#          score
# subject       
# eng        165
# kor        214
# math       176
# -> 바로 DataFrame로 반환

