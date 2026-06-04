import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
t = [ x for x in range(7) ]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure( figsize = (10, 6))
plt.plot(
    t, y, 
    color = 'green', 
    linestyle = ':', 
    marker = '1')
# linestyle 지정
# marker 옵션으로 데이터 가 존재하는 곳에 마킹
#plt.plot(t,y, 'gD--') # 위 코드위 동일
# marker 색 및 size 지정
m = [2, 4, 8, 6, 5, 2, 5]
plt.plot(
    t, m, 
    color = 'red', 
    linestyle = ':', 
    marker = 'o', 
    markerfacecolor = 'm', 
    markersize = 8
    )
plt.show()