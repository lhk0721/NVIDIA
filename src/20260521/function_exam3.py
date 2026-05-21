
# =========================== 문제 1 ======================================

strData = '# AI % 3 pro&*graM'

def AlphaFindFunc(str):
    string = '' # 리스트로 관리, 추후에 ''.join 하는 방법도 있다.
    # print(str)
    for s in str:
        # if (ord(s) <= ord('Z')) and (ord(s) >= ord('A')) or (ord(s) <= ord('z')) and (ord(s) >= ord('a')):
        if ((s <= 'Z') and (s >= 'A')) or ((s <= 'z') and (s >= 'a')):
            string += s
    return string

result = AlphaFindFunc(strData)# 함수 호출
# print('result: ', result) # AiprograM 영문 대소문자만 추출 출력
# print('a'<'b') #도 가능하다. 궂이 ord 할 필요 없음.
# or 연산으로 하면 더

# =========================== 문제 2 ======================================
listData = ['python', 'ai', 'study', 'good', 'ai', 'python', 'ai']

## word counter
# def WordCountFunc(list):
#     print('scope=>WordCountFunc')
#     dataSet = set(list)
#     count = {}
#     print('\ttypecheck=>',type(count),count.items())

#     print('\tloop =>start')
#     loopCount = 0
#     for _,w in enumerate(list):
#         loopCount += 1
#         print(f'\t\tloop=>{loopCount}')
#         if w in dataSet:
#             print('\t\t\tlog=>',w,type(w))
#             if w not in count:
#                 count[w] = 1
#                 print('\t\t\tlog=>',count[w],type(count[w]))
#             else:
#                 count[w] += 1
#                 print('\t\t\tlog=>',count[w],type(count[w]))

#     print('\tloop =>end')

#     return count

# print('scope=>global')
# result = WordCountFunc(listData)
# print('scope=>global')
# print(result)


# =========================== 문제 3 ======================================
key_list = ['name','age','address']
value_list = ['hong',50,'seoul']

def InfoCombine(keys, values):
    # combDict = {}
    # for i,v in enumerate(keys):
    #     combDict[v] = values[i]
    combDict = { v:values[i] for i,v in enumerate(keys)}

    return combDict

result = InfoCombine(key_list,value_list)
print ('result: ', result)
