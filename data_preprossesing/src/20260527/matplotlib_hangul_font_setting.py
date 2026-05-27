import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

# plt.title('한글 제목')
# plt.plot([10,20,30,40],[1,4,9,16])
# plt.xlabel('엑스축 라벨')
# plt.ylabel('와이축 라벨')
plt.title('plot')
plt.plot([10,20,30,40],[1,4,9,16])
plt.show()