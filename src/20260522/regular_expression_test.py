import re

strData = '파이썬, library 활용한 Text Preprocessing!!'

str_filter = re.findall(r'[a-zA-Z]+',strData)
print(', '.join(str_filter))
# str_split = re.split(r'[,\s]', strData)
# print(str_split)

# print(result) # library, Text, Preprocessing 인 한 문자열로 출력