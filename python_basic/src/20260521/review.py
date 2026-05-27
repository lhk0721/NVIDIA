# function
# 코드의 양이 커지고 큰 프로젝트를 수행해야 할 경우, 기능 단위로 코드를 분할해서 프로젝트를 완성해야 할 경우 필수적으로 기능 단위를 함수화시켜서 사용해야 한다.
# 함수 단위를 함수화시켜서 사용해야 한다!

# 함수는 라이브러리 / 사용자 정의 함수로 나뉜다.
# 라이브러리: print, input 등등,,, 이미 만들어져있는 함수를 호출해서 사용
# 사용자 정의 함수 ( 직접 구현 ) 함수 정의까지 직접 만들어야 한다.
# 함수가 호출되면 함수 정의부로 점프한해서 함수 정의가 동작하고 함수 정의에 있는 명령이 모두 종료되면 호출부로 다시 되돌아온다.
# 인터럽팅과 폴링
# 함수 정의 후 def로 사용
def 함수명(매개변수):
    # 해당 함수가 동작하는 명령어들의 집합 함수의 기능을 서술
    pass # 미정의 오류 escape

# ex) 넘겨받은 전달인자 값에 5 더해서 출력하는 함수.
def addDataFunction(arg): # 함수 정의부분
    # print('result: ', arg + 5)
    # return arg + 5 # 값의 반환과 함수의 종료 기능
    sum = 0
    for i in arg:
        sum += i
    avg = sum/len(arg)
    # print('sum: ',sum)
    # print('avg: ',avg)
    return sum, avg

    
    

# 함수 호출 은 함수명부터 시작한다. 
# 함수명(매개변수) 매개변수: 함수 정의 부분으로 던져주는 값.
# 변수 먼저 적는 것은 함수 반환값 id를 담을 곳을 마련하는 것 뿐이다. 함수 이름이 먼저다.
# result = addDataFunction(5)

# res = addDataFunction([5,6,7,8,9])
# print('res: ',res, type(res)) # 특정 함수의 return이 없을 경우 None을, 있을 경우 그 return값

res_total, res_avg = addDataFunction([5,6,7,8,9])
print('res_total: ',res_total)
print('res_avg', res_avg)

