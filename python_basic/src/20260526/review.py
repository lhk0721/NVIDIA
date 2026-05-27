import re

## 파일 다루기
# with open('파일명을 포함한 경로','접근모드') as f: # 접근모드 -> r, w, a, r+
#     f.read() # 모든 텍스트 내용을 읽어서 하나의 문자열 객체로 생성
#     f.readlines() # 텍스트 파일 각 라인별 내용을 리스트에 항목으로 변환
#     f.write() # 텍스트파일에 현재 메모리 내용을 쓰는 함수.

## 정규식 표현
# 문자열 객체의 내용을 특정 패턴을 활용해서 찾고(검색), 치환(수정), 분할 시키는 역할의 문법
# 패턴 -> r'찾고자 하는 패턴' 
# r'[a-z]+, r'A-Z'+, r[0-9]+, r[가-힣]+

strData = "AI 프로그래밍 1998 python Processing!!"
print(re.findall(r'[가-힣]+',strData))
print(re.findall(r'[0-9]+',strData))
print(re.findall(r'[a-zA-Z]'))