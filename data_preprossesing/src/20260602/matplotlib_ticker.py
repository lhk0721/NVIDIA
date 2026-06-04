import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


idxdata = [ str(x) for x in range(20000501,20000531)]
print(idxdata) # 문자 인덱스
mydf = pd.DataFrame({'가격':np.random.randint(12000,13000,size=(30,))},index=idxdata)
print(mydf)
fig = plt.figure(figsize=(11,7)) 
ax1 = fig.add_subplot(1,1,1) 
ax1.plot(mydf.index, mydf)

ax1.xaxis.set_major_locator(MultipleLocator(3))
ax1.xaxis.set_minor_locator(MultipleLocator(1))

ax1.tick_params(
    axis='x',
    which='major',
    length=10,
    width=2,
    color='r',
    rotation=15
)

plt.show()