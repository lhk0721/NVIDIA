
def listSumOfData(list):
    sum = 0
    for num in list:
        sum += num
    return sum

def addListData(arr1, arr2):
    result = []
    for i in range(len(arr1)): # enumerate도 가능하다.
        result.append(arr1[i] + arr2[i])
    return result

# total = listSumOfData([60,77,88,33]) # 함수 정의로 점프
# print('total: ', total )

result = addListData([5,6,7,8],[2,3,4,5])
# print(result)

def function(*arg): # 튜플로 받음
    # print(arg, type(arg)) # (1, 3, 4, 5, 6, 6) <class 'tuple'>
    return

function(1,3,4,5,6,6)


# 앞에 전달된 문자열 중 뒤에 전달된 문자의 개수를 파악해서 반환하세요
def CheckAlphaData(_str,alpha):
    count = 0
    # for i in range(len(_str)):
    for _, s in enumerate(_str): # 참조하지 않을 반환값이 있으면 '_' 로 준다.
        if(s == alpha):
            count += 1

    return (count)

cnt = CheckAlphaData('python programming','p')
print('cnt: ',cnt)