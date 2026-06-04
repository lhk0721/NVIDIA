import numpy as np
import pandas as pd

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

##
df = pd.read_csv(r'C:\Users\25\Documents\github\python_project\dataset\tips.csv')
print(df.head(5))
print('='*80)

## 
# 그루핑할 기준키는 smoker
# 집계할 칼럼은 'total_bill' , 'tip'
# 집계 함수는 mean
# 흡연자, 비흡연자의 'total_bill' , 'tip' 평균을 계산!

gbmean = df.groupby(['smoker', 'gender'])[['total_bill', 'tip']].mean()

# print(gbmean)

#                total_bill       tip
# smoker gender                      
# No     Female   18.105185  2.773519
#        Male     19.791237  3.113402
# Yes    Female   17.977879  2.931515
#        Male     22.284500  3.051167

## 요일별 흡연자, 비흡연자 팁의 평균을 계산해서 평균

gbmean2 = df.groupby(['day','smoker'])[['tip']].mean()

# print(gbmean2)

#                   tip
# day  smoker          
# Fri  No      2.812500
#      Yes     2.714000
# Sat  No      3.102889
#      Yes     2.875476
# Sun  No      3.167895
#      Yes     3.516842
# Thur No      2.673778
#      Yes     3.030000


# print(gbmean2.index) # 멀티인덱스
# MultiIndex([( 'Fri',  'No'),
#             ( 'Fri', 'Yes'),
#             ( 'Sat',  'No'),
#             ( 'Sat', 'Yes'),
#             ( 'Sun',  'No'),
#             ( 'Sun', 'Yes'),
#             ('Thur',  'No'),
#             ('Thur', 'Yes')],
#            names=['day', 'smoker'])

# print(gbmean2.loc[( 'Sat', 'Yes'),'tip'])
# print(gbmean2.loc['Sat',:].loc['Yes',:])
# tip    2.875476
##
unstackgbmean2 = gbmean2.unstack()
print(unstackgbmean2)
#              tip          
# smoker        No       Yes
# day                       
# Fri     2.812500  2.714000
# Sat     3.102889  2.875476
# Sun     3.167895  3.516842
# Thur    2.673778  3.030000

# print(unstackgbmean2.keys()) # series(index)냐 dataframe(columns)이냐에 따라 반환값이 달라진다.
print(unstackgbmean2.columns) # 메서드가 아닌 attribute
# MultiIndex([('tip',  'No'),
#             ('tip', 'Yes')],
#            names=[None, 'smoker'])

# print(unstackgbmean2.loc['Sun',('tip', 'Yes')])
# 3.5168421052631573
