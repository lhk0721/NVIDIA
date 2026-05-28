import numpy as np
import pandas as pd

dictData = {'Hong':[90, 80, 70, 50, 75], 'Kim':[85, 95, 65, 55, 75], 'Park': [88, 93, 75, 72, 75], 'Lee':[55, 66, 77, 92, 75]}
df = pd.DataFrame(dictData, index=['kor', 'eng', 'math', 'music', 'science'])

print(df)

print('='*80)

# fancy 인덱싱. 추출하고자 하는 index의 배열을 전달
print(
    df.iloc[[1,3],:]
)
