
listdata = [2,5,8,1,6,7]
# 오름차순으로 정렬
# 정렬 동작의 메서드(함수) 지원
# sort: return 없는 void
# print(listdata.sort()) # None! 출력할 값이 없다. 원 리스트 데이터를 기본적으로 오름차순 정렬할 뿐. 내부적으로 정렬된 사본 객체를 생성하지 않는다.
#원본 데이터에 직접 반영한다.
# 파이썬은 특정 함수의 return 값이 없을 경우 내부적으로 None 객체를 반환한다.

# 잘못된 코드.
# listdata2 = listdata.sort()
# print(listdata2)

# 내림차순 정렬
# listdata.sort(reverse=True)
# print(listdata)

# 정렬 기능의 내부 함수
# print(listdata)
sortedList = sorted(listdata) # 이터러블을 주고, 정렬된 사본을 return한다.
print(sortedList)

reverseSortedList = sorted(listdata,reverse=True) # 내림차순
print(reverseSortedList)

print(listdata) #원본도 사후 접근 가능!! 허나 메모리 비효율성의 tradeoff 존재. sort()와 sorted()는 상황에따라 다르게 선택하는 것이다.
