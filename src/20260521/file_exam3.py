
## 파일 입출력 => with as
with open('pythonData.txt','r+',) as f:
    # 이 indent를 벗어나면 자동 close() 된다.
    # 이 block에서는 파일 접근 코드만 동작하면 된다.
    str = f.readlines() # 전체 문자열 읽기

# print(str) # 문자열 객체는 메모리에 남아있게 된다. 파일 객체와 구분하여 생각하는 것이 중요하다.
# f.readlines() # 오류! ValueError: I/O operation on closed file. 접근할 수 없다.


strList = [x.strip() for x in str] #문자열 '\n'로 붙어있어도 개행으로 인식하고 잘라낸다. '\\'도 잘라낸다.

print(strList)
##
