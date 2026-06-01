import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\teacher_list_pivot_exam.xlsx')

# print(df)
#     카테고리                       과정명  강의시수  강사명
# 0   prog             C Programming    32  홍길동
# 1   prog             C Programming    32  대조영
# 2   prog             C Programming    28  이순신
# 3    Emb    Embedded C Programming    32  홍길동
# 4    Emb    Embedded C Programming    64  대조영
# 5    Emb    Embedded C Programming    36  이순신
# 6    Emb          Embedded Porting    28  홍길동
# 7    Emb          Embedded Porting    32  대조영
# 8    Emb          Embedded Porting    28  이순신
# 9    Emb  Linux system Programming    50  홍길동
# 10   Emb  Linux system Programming    70  홍길동
# 11   Emb  Linux system Programming    25  대조영
# 12   Emb  Linux system Programming    30  이순신

## DataFrame.pivot_table()

# pvDf = df.pivot(index='과정명', columns='강사명', values='강의시수') #오류!
# 재형성 시점에서 중복데이터 발생 시 오류가 발생한다.

pvDf = df.pivot_table(index='과정명', columns='강사명', values='강의시수', aggfunc='sum')
# 중복데이터 발생 시 어떻게 처리할 지 aggfunc 인자를 줄 수 있다. 
# 재형성과 동시에 집계.통계를 적용한다.

# print(pvDf)
# 강사명                       대조영  이순신  홍길동
# 과정명                                    
# C Programming              32   28   32
# Embedded C Programming     64   36   32
# Embedded Porting           32   28   28
# Linux system Programming   25   30  120

##
df2 = pd.read_excel(r'C:\Users\25\Documents\github\python_project\data_preprossesing\src\20260601\teacher_list_pivot_exam_1.xlsx') # 중복데이터를 지우면 피봇도 된다.

# print(df2)
#     카테고리                       과정명  강의시수  강사명
# 0   prog             C Programming    32  홍길동
# 1   prog             C Programming    32  대조영
# 2   prog             C Programming    28  이순신
# 3    Emb    Embedded C Programming    32  홍길동
# 4    Emb    Embedded C Programming    64  대조영
# 5    Emb    Embedded C Programming    36  이순신
# 6    Emb          Embedded Porting    28  홍길동
# 7    Emb          Embedded Porting    32  대조영
# 8    Emb          Embedded Porting    28  이순신
# 9    Emb  Linux system Programming    70  홍길동
# 10   Emb  Linux system Programming    25  대조영
# 11   Emb  Linux system Programming    30  이순신

df2_pivotTable = df2.pivot_table(
    index='과정명',
    columns='강사명',
    values='강의시수',
    aggfunc='sum'
)

df2_pivotTable.index = ['C', 'EmbC', 'EmbP','Linux']

print(df2_pivotTable.index)


print(df2_pivotTable)
df2.plot.bar()
plt.show()



