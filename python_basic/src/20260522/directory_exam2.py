import os
import shutil

## 프로젝트 루트 디렉토리 아래에 'reference' 디렉토리를 만들기

# root = os.getcwd() + '\\'

# if os.path.exists(root + 'reference'):
#     print("'\\reference' dir already exists.")
# else:
#     print("Create \\reference dir.")
#     os.mkdir(root + 'reference')

## 20260521 디렉토리 내부에 존재하는 Health_info.csv 파일을 복사시키기. reference 디렉토리 내부로

# 중간경로까지 한번에 만들고 싶으면, os.mkdirs()
# shutils.copy(src,dist)는 목적지 경로를 만들어주지만, 중간경로는 만들어주지 않는다.

# if os.path.exists(root + 'src\\20260521\\Health_info.csv'):
#     print('Moving data to destination...')
#     data = root + 'src\\20260521\\Health_info.csv'
#     dest = root + 'reference'
#     if not os.path.exists(dest + '\\Health_info.csv'):
#         shutil.copy(data, dest)
#         print(os.listdir())
#         print('Done')
#     else:   
#         print("'\\Health_info.csv' already exists in dest...")
# else:
#     print("Can't find '\\Health_info.csv'...")
#     pass

# shutil.copy2() # 파일의 속성정보까지 모두 메타데이터까지 복사. 깊은복사

## 시간
import time

print(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday)
