# ord() 문자의 원래 값을 반환

srcString = 'PYTHON PROGRAMING'

listData = [ chr(ord(x)+32) 
            if ((ord(x)>=65) and (ord(x)<=90)) 
            else x  
            for x in srcString]

result = ''.join(listData)

print(result) # 'python programing' 매서드 활용 금지, 리스트 내포와 조건 표현식 활용.


wordList = ['book','car', 'apple', 'python', 'ai']
#wordList의 문자열 항목 중 문자열의 길이가 4 이상인 문자열만 새 리스트에 저장 출력

newWordList = [word for word in wordList if (len(word) >= 4)]
print(newWordList)