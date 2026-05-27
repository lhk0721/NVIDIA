
scoreList = [['Kor'],['Eng'],['Math']]
print(scoreList)

print('='*80)

# 문제
# input 함수를 이용해서 키보드로 각 과목의 점수를 입력받아 저장, 출력
Kor_score = input("국어 점수 입력: ")
Eng_score = input("영어 점수 입력: ")
Math_score = input("수학 점수 입력: ")

scoreList[0].append(Kor_score)
scoreList[1].append(Eng_score)
scoreList[2].append(Math_score)

print(scoreList) #[['Kor',90], ['Eng',80], ['Math',70]]

# 학생의 총점과 평균을 계산해서 출력
scoreSum = int(Kor_score) + int(Eng_score) + int(Math_score)
scoreAvg = scoreSum/3
print(f"총점: {scoreSum:.2f} ")
print(f"평균: {scoreAvg:.2f} ")