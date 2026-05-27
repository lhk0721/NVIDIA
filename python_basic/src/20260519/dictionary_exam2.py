#판다스는 다음 주차에 따로 배움. dict 자료형의 중요성 알기 위한 시간.

import pandas as pd
# col, row. 길이는 맞아야 한다.
scoredict = {'kor': [80,90,70], 'eng': [77,88,55], 'math': [33,55,66]}

print(scoredict) # 허나 여전히 dict로 보인다.

mydf = pd.DataFrame(scoredict) #메모리에 떠있는 데이터
print(mydf)

mydf.to_excel('mydf.xlsx') # 데이터프레임 객체를 엑셀 데이터로 저장
