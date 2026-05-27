# 파일 입출력 -> open, close
# open(): 파이썬에서 접근할 수 있도록 파일 객체와 연결
# close(): 파일 객체 해제
# 

# f = open('./pythonData.txt', 'r')

## read
# strData = f.read() # 텍스트파일에 작성된 모든텍스트를 읽어들여 문자열 객체 생성
# print(strData)

## readline
# strData = f.readline() # 텍스트파일의 첫번째 줄만 읽는다.
# print(strData)

## readlines
# strData = f.readlines() # 각 라인의 텍스트를 읽고 리스트의 항목으로 넣어 리스트를 반환한다.
# print(strData)

## 오류
# print('읽기 전,', f.tell())
# strData = f.read() # 여기서 다 읽어버려서 파일 포인터가 끝으로 이동해버린다.
# print('read(),', f.tell())
# strData = f.readlines() # 더이상 읽을 게 없다.
# print('readlines(),', f.tell())
# print(strData) # [].
# f.seek(0,0) # 파일 포인터를 맨 위로 초기화
# print('seek(0,0),', f.tell())
# print('readlines(),', f.tell())
# strData = f.readlines()
# print(strData) 

## r+모드
# f = open('./pythonData.txt', 'r+',-1,'utf-8') # 읽고 쓸 수 있는 모드
# strData = f.read()
# print('strData: ',strData)
# f.write('\n가나다라')
# f.seek(0.0)
# strData = f.readlines()
# print('strData: ',strData)
# f.close() # 파일 객체 메모리 해제. 파일 종료되면 자동으로 해제되긴 하는데, 프로그램이 살아있을 경우 메모리 누수가 발생할 수 있다.

