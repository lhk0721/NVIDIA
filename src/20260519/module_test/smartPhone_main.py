# 파이썬에서는 파일명이 모듈명으로 사용된다!
import camera_operation as cam
import phone_call as ph

# 사진 기능
# cam.picture_function() # 두번 동작해버린다..
    # 사진 동작 완료!
    # __name__:  camera_operation
    # 사진 동작 완료!

# 호출을 주석처리하고 실행해도 동작해버린다. 하위 모듈에서 if(__name__ == '__main__'): 처리가 필요하다.

cam.picture_function()

# 전화 기능
ph.phone_call()

# display 기능