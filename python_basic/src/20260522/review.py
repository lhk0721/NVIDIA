import os

#텍스트 파일(.txt)은 파일 입출력 코드로 접근하는게 편함
#파일 개방 함수 ==> open() 접근할 파일의 경로 -> 파일명, 접근모드를 설정
#접근모드 ==> 'r' (읽기) 'w' (새로 파일 생성, 쓰기모드, 기존파일 리셋) 'r+' (읽기 쓰기 가능) 'a' (추가모드)
#파일 해제 함수 ==> close()

#with open(파일명, 모드) as (약어) 구문->벗어나면 자동으로 close 됨
#\ 는 인식안되어서 /로 바꿔줘야함.
with open("C:/sua/python_basic/20260521/pythondata.txt","r+") as f: #open 디폴트파라미터는 'r' 모드임.
    #f.write('하이') #디폴트 파라미터가 'r'이라 오류뜸, 그래서 접근모드는 항상 써주는게 좋음.
    str = f.read()
    f.seek(0,0)
    str2 = f.readlines()

print(str)

# 하이on
# study
# Ai
# programming
# happy
# test
# test
#첫줄 python 앞 4개 사라지고 하이가 써짐-> 커서의 위치가 중요함 write는 삽입되는 것
# with open(mode="r+",file="C:/sua/python_basic/20260521/pythondata.txt") as f: #이렇게 key로 명시하면 순서 바꿔도 됨
print(str2) #['하이on\n', 'study\n', 'Ai\n', 'programming\n', 'happy\n', 'test\n', 'test']
listdata=[x.strip() for  x in str2]
print(listdata) #['하이on', 'study', 'Ai', 'programming', 'happy', 'test', 'test']


import pandas as pd
mydf=pd.DataFrame(listdata)
print(mydf)
#              0
# 0         하이on
# 1        study
# 2           Ai
# 3  programming
# 4        happy
# 5         test
# 6         test
mydf.to_excel(r"C:\Users\25\Documents\github\python_project\dataset\pythondata.xlsx", index=False ) #1열 idx 없어짐



import os
print(os.getcwd()) #파일 경로를 알려줌
#C:\sua\python_basic\20260522
print(os.listdir('C:/sua/python_basic')) #['.idea', '20260518', '20260519', '20260520', '20260521', '20260522', 'Include', 'Lib', 'pyvenv.cfg', 'Scripts']
#경로에 있는 파일 이름을 다 알려줌