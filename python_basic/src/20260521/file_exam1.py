# 파일을 객체화하여 접근해서 일고 쓰기 동작을 수행하는 것이 파이썬의 파일 입출력이다.
# .txt 텍스트 파일은 파일 입출력 방식이 최고이다. xlsx, csv 같은 복잡한 파일은(csv도 텍스트이지만) pandas를 활용해 읽는 것이 좋다.

# open: 파일 개방함수(라이브러리가 지원함.)
#open(파일명,모드)
# open('mytext.txt','r') # r == 읽기모드. 없으면 오류남
# a == 추가모드
# r+ == 읽고 쓰기가 가능한 모드
f = open('C:/Users/25/Documents/github/python_project/src/20260521/myText','w') # w = 쓰기모드. 없으면 만든다. 
# f.write('hello world')
f.write('no way!!') # 있으면 덮어씀 주의!
f.close() #닫아줘야 실행된다!

# close: 파일객체 해제함수

# 어플리케이션에서 OS에게 명령을 전달하고 OS가 펌웨어, 하드드라이브에 접근한다.
# 따라서 라이브러리를 사용해야 한다.