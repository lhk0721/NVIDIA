
# 시퀀스 객체에 지원하는 연산: *,+,
listdata1 = [40,30,10]
listdata2 = [50,39,123]

reslist = listdata1 + listdata2 # 빼기는 지원하지 않는다.
print (reslist)

# 곱셈 연산. 자료구조 알고리즘 설계 시 메모리 공간을 미리 확보할 때.
listtmp = [None] * 10 # 원형 큐,, 10개만 미리 만들어달라. 빈 걸로 하면 인덱스가 잡히지 않는다.
print(listtmp)
listtmp[9] = 40
print(listtmp)

print('='*80)

print(reslist[1:4])

print('='*80)

# 각 항목에 연산. 수치연산
# listdata3 = [5,6,7,8] + 3 # 오류!
listdata3 = [5,6,7,8] + [3]
print(listdata3) # 뒤에 붙어버린다. 각 항목에 더하고 싶다만 리스트의 덧셈 연산의 한계. 리스트 객체끼리만 가능하다.

listdata4 = []
# for 문 활용... 잘 쓰지 않는다.
# for item in listdata3:
#     listdata4.append(item + 3)

# 수치연산에 특화된 라이브러리 넘파이 활용. 외부 라이브러리!
# 파이참 가상 인터프리터 env lib에 설치해야 한다.
# 가상환경 내에서 'pip install numpy'
# 특정 버젼을 설치하고 싶다면 가상환경 내에서 'pip install numpy==~(공백없음!)'
# 확인: 'pip list'
print(listdata4, type(listdata4))

# 라이브러리(패키지) 추가 문법
# as: 별칭(alis) 부여
import numpy as np

print('='*80)

arr1 = np.array([99,22,33,35])
print(arr1,type(arr1))
print (arr1 + 3) # 넘파이는 이걸 지원하는 리스트의 상위 3 -> [3,3,3,3]으로 확장시킨다. 앞의 shape와 뒤의 shape를 일치시킨다.
