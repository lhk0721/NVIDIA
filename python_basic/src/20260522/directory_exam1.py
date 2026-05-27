import os # 조작에 주의. path가 날아갈 수 있음
# import sy # 이게 더 위험하다.
import shutil

# print(os.getcwd()) # 나중에 변수처리할 수 있음
root_dir = os.getcwd() + '\\' # 매번 파일명 앞에 쓰기 귀찮으면 여기 붙여놓자.
# print(root_dir)

##directory 만들기
# if os.path.exists(root_dir + 'pythonDataset'): # 있는데 또 만드려고 하면 에러 나옴. 에러처리 필요.
#     # pass
#     shutil.move(root_dir + 'pythonDataset', root_dir + 'dataset')
# else:
#     os.mkdir(root_dir + 'pythonDataset') # \ 넣어줘야 함!! 조건문 처리 해주는 게 좋음.
# print(os.listdir()) # == $ dir

# os.rmdir(root_dir + '\dataset') #. 단점...디렉토리 내부에 파일이 하나라도 존재하면 오류난다.
shutil.rmtree(root_dir + 'dataset') # 싹 날아감.

