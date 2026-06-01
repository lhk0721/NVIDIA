import numpy as np
import pandas as pd

df = pd.DataFrame(
    [[80,90,70],[75,65,95]],
    index=pd.Index(['kor','math'], name='subject'),
    columns=pd.Index(['stu1','stu2','stu3'], name='student') # index name도 줄 수 있다.
)

# print(df)
# student  stu1  stu2  stu3
# subject                  
# kor        80    90    70
# math       75    65    95

## 재형성.
# 데이터프레임의 형태(모양)을 바꿀 때 사용

stdf = df.stack() # df객체 재형성

# print(stdf)
# subject  student
# kor      stu1       80
#          stu2       90
#          stu3       70
# math     stu1       75
#          stu2       65
#          stu3       95
# dtype: int64

# 그루핑, 기타 작업 시 이런 시리즈로 나올 때가 있다. 이때 unstack 해주면 된다.
unstdf = stdf.unstack()

# print(unstdf)
# student  stu1  stu2  stu3
# subject                  
# kor        80    90    70
# math       75    65    95

# unstack, stack은 종종 쓴다.


