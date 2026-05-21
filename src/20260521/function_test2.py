StringData = 'I love AI python programming'

EncBook = {
    'l' : '#',
    'p' : '@',
    'o' : '7',
    'g' : '$',
    'I' : '%',
    'a' : '8',
    't' : '*',
    'r' : '3',
    'n' : '6'
    }

DecBook = {v:k for k,v in EncBook.items()}

'''
```python
EncBook = {
    'l' : '#',
    'p' : '@',
    'o' : '7',
    'g' : '$',
    'I' : '%',
    'a' : '8',
    't' : '*',
    'r' : '3',
    'n' : '6'
    }

DecBook = {DecBook[v] = k} for k,v in EncBook
```

뭐가 잘못된거야?

문법 오류가 두 군데 있어. 하나씩 짚어볼게.

## 오류 1: 컴프리헨션 안에서 할당문 사용

```python
{DecBook[v] = k}
```

dict comprehension은 `{key표현식: value표현식 for ...}` 형태인데, 너는 그 자리에 **할당문**(`DecBook[v] = k`)을 넣었어. 컴프리헨션 자체가 새로운 dict를 만들어내는 표현식이라, 안에서 또 다른 dict에 값을 넣을 필요가 없어. 그냥 **`key: value`** 형태로 적으면 돼.

```python
{v: k for ...}    # ✅ value를 key로, key를 value로
```

## 오류 2: `.items()` 빠짐

```python
for k, v in EncBook
```

dict를 그냥 순회하면 **key만** 나와. `k, v`로 언패킹하려면 `(key, value)` 튜플을 내놔야 하니까 `.items()`가 필요해.

```python
for k, v in EncBook.items()   # ✅
```

추가로 컴프리헨션은 끝에 콜론(`:`)이 아니라 `for` 절이 끝나면 닫는 중괄호로 마무리해야 해.

## 올바른 코드

```python
DecBook = {v: k for k, v in EncBook.items()}
```

읽어보면 "`EncBook`의 각 `(k, v)` 쌍에 대해, `v`를 key로 하고 `k`를 value로 하는 새 dict를 만들어라"라는 뜻이야.

확인:

```python
print(DecBook)
# {'#': 'l', '@': 'p', '7': 'o', '$': 'g', '%': 'I', '8': 'a', '*': 't', '3': 'r', '6': 'n'}

print(DecBook['#'])  # 'l'
print(DecBook['$'])  # 'g'
```

## 참고: 컴프리헨션 없이 쓴다면

문법이 헷갈리면 일반 for 루프로도 똑같이 만들 수 있어. 이건 너가 처음 시도했던 방식(빈 dict에 하나씩 채워넣기)에 가까워:

```python
DecBook = {}
for k, v in EncBook.items():
    DecBook[v] = k
```

결과는 동일하지만, 컴프리헨션이 더 짧고 파이썬다운 표현이야.'''

print(DecBook)

# 암호화
def EncryptFunc(msg):

    global EncBook

    for s in msg:
        if s in EncBook:
            msg = msg.replace(s,EncBook[s])

    return msg

encmsg = EncryptFunc(StringData) # 전달된 문자열을 암호화 시켜서 반환하는 함수

# print(encmsg)

# encmsg 복호화

def decryptFunc(msg):

    global DecBook

    for s in msg:
        if s in DecBook:
            msg = msg.replace(s,DecBook[s])
    return msg
    
decmsg = decryptFunc(encmsg)
print(decmsg)