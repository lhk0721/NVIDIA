
def picture_function(): # 함수 정의부. 호출 전엔 동작하지 않는다.
    print('사진 기능 동작!')

# 정의된 함수가 동작하려면 호출되어야 한다.

# 현재 파일이 실행 모듈일 경우 내부 특수 변수 __name__은 __main__을 갖는다!
# picture_function()
# print("__name__: ", __name__) # __main__

# 해당 파일이 import되는 모듈일 경우 __name__은 모듈명(파일명)을 갖는다!
# __name__가 뭔지에 따라 동작을 달리해라.
# 외부 호출인 경우: 실행하지 마라
# 내부 호출인 경우: 실행해라
if(__name__ == '__main__'):
    picture_function()
    print("__name__: ", __name__)