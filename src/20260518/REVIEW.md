# 2026-05-18 파이썬 기초 복습 자료

> 수업 필기(`first_python.py`, `print_exam.py`, `dataType_exam.py`, `string_exam1.py`, `string_method_exam.py`, `input_exam.py`)를 주제별로 재구성하고 설명을 덧붙였습니다.

---

## 1. 파이썬 첫걸음

### 1-1. 가장 단순한 실행 — `print()`

```python
print("python test!!")
```

- `print()`는 **표준 출력(모니터)** 으로 값을 내보내는 내장 함수.
- 괄호 안에 출력할 값을 넣고, 문자열은 따옴표로 감싼다.
- 함수는 "이름 + 괄호" 형태로 호출한다는 점에서 다른 언어와 같다.

### 1-2. 주석(Comment)

```python
# 한 줄 주석입니다.
# print("이 줄은 실행되지 않습니다")
```

- `#` 뒤의 모든 텍스트는 **인터프리터가 무시**한다.
- 사용 목적
  1. 코드 설명(다른 사람, 미래의 나에게 메모).
  2. 임시로 코드 실행을 막을 때(주석 처리).
- 단축키: PyCharm / VS Code에서 `Ctrl + /` 로 토글.

### 1-3. 변수 선언

```python
semantic_var = 50
```

- 파이썬에서는 **타입을 적지 않고** `이름 = 값` 형태로 선언과 동시에 대입한다.
- 변수명 규칙
  - 영문/숫자/언더스코어(`_`) 가능, 숫자로 시작 불가.
  - 예약어(`if`, `class`, `for` …) 사용 불가.
  - 관례: 변수·함수는 **snake_case**, 클래스는 **PascalCase**.
- 끝의 세미콜론 `;` 은 허용되지만 **권장하지 않음**(파이썬은 줄바꿈으로 문장을 구분).

---

## 2. `print()` 함수 깊게 보기

### 2-1. 문자열 표기 — 작은따옴표 vs 큰따옴표

```python
print("python")
print('python')
print("문자열 안의 '작은따옴표'")
```

- 파이썬에서는 `'...'` 와 `"..."` 둘 다 같은 문자열.
- **혼합 사용의 이점**: 문자열 내부에 다른 종류의 따옴표가 들어가야 할 때 escape(`\`) 없이 쓸 수 있다.
  - `"He said 'hi'"`, `'그는 "안녕"이라 말했다'`

### 2-2. 이스케이프(특수)문자

| 표기 | 의미 |
|---|---|
| `\n` | 개행(줄바꿈) |
| `\t` | 탭 |
| `\\` | 역슬래시 자체 |
| `\'`, `\"` | 따옴표 자체 |

```python
print("줄바꿈 역할의 \n 특수문자")
```

### 2-3. 함수의 파라미터(인자)와 기본값

```python
print("줄바꿈 역할의 \n 특수문자", end="")
print("AI programming")
```

- `print()` 의 시그니처(요약): `print(*values, sep=' ', end='\n')`
- 즉, 호출할 때 인자를 주지 않으면 **기본값(default)** 이 자동 적용된다.
  - `sep=' '` : 여러 값을 출력할 때 사이에 들어가는 문자(기본 공백).
  - `end='\n'`: 출력 마지막에 붙는 문자(기본 줄바꿈).
- `end=""` 로 바꾸면 줄바꿈 없이 다음 출력이 같은 줄에 이어진다.
- 팁: 함수명에 마우스를 올리거나 `Ctrl + 클릭` 하면 **선언 위치/시그니처**를 확인 가능.

### 2-4. 자주 쓰는 예

```python
print("a", "b", "c")            # a b c
print("a", "b", "c", sep="-")   # a-b-c
print("진행 중", end="...")
print("완료")                    # 진행 중...완료
```

---

## 3. 파이썬의 객체지향과 변수의 본질

### 3-1. 모든 것은 객체(Object)

- 파이썬은 **객체지향 언어**.
- 정수, 실수, 문자열, 함수, 심지어 클래스 자체도 전부 **객체**.
- 객체를 찍어내는 틀이 **클래스(class)**.
  - `int`, `float`, `str`, `bool` 은 **파이썬이 기본 제공하는 클래스**.

### 3-2. 객체 생성 — "클래스명()" 문법

```python
data = int(50)      # int 클래스로 50 객체 생성
data = str("python")
```

- 원칙적으로는 클래스명을 호출해 객체를 만들어야 한다.
- 그러나 파이썬은 **동적 타이핑(dynamic typing)** 언어라, 리터럴(`50`, `"python"`)을 적으면 **자동으로 해당 클래스 객체를 생성**해준다.

```python
data = 50           # 위의 int(50) 와 동일한 결과
data = "python"
```

### 3-3. 변수 = "참조(reference)"

> **핵심**: 파이썬 변수는 값을 직접 담는 상자가 아니라, 메모리 어딘가에 있는 **객체의 주소(id)** 를 가리키는 **포인터** 다.

```python
data = 50
print(data, type(data), id(data))
# 50 <class 'int'> 140711...
```

- `type(x)` : x가 가리키는 객체의 **클래스(자료형)** 반환.
- `id(x)` : x가 가리키는 객체의 **메모리 주소(고유 번호)** 반환.

### 3-4. 재할당과 가비지 컬렉션

```python
data = 50          # data → [50] 객체
data = "python"    # data → ["python"] 객체로 화살표 이동
```

- 두 번째 줄 이후 `[50]` 객체를 가리키는 변수가 사라진다.
- 참조가 0이 된 객체는 **가비지 컬렉터(GC)** 가 자동으로 메모리에서 제거.
- 따라서 한 변수에 다른 자료형을 덮어쓰는 것은 가능하지만, 의도치 않게 **이전 객체를 잃어버리므로** 의미 있는 이름을 따로 두는 편이 안전하다.

### 3-5. 기본 자료형 한눈에

| 클래스 | 의미 | 예시 |
|---|---|---|
| `int` | 정수 | `50`, `-3`, `0` |
| `float` | 실수 | `5.8`, `3.14`, `-0.1` |
| `str` | 문자열 | `"python"`, `'a'` |
| `bool` | 불리언 | `True`, `False` (대문자 시작!) |

```python
a = 50          # int
b = 5.8         # float
c = "python"    # str
d = True        # bool
```

### 3-6. 변수에 타입을 안 적어도 되는 이유 — 정리

> 변수는 타입/내용/크기를 담는 게 아니라, **객체의 id 만** 담는다.
> 그래서 어떤 객체든 가리킬 수 있고, 다른 자료형으로의 재할당도 자유롭다.

### 3-7. 사용자 정의 클래스 맛보기

```python
class Mycls:
    def __init__(self, arg):
        self.mdata = arg

myData = Mycls(5)
print(myData.mdata, type(myData), id(myData))
```

- `class 이름:` 으로 새 클래스 정의.
- `__init__` : 객체가 만들어질 때 자동 호출되는 **생성자**.
- `self` : 만들어지는 **객체 자신**을 가리키는 참조(첫 번째 매개변수, 약속).
- `self.mdata = arg` : 객체 내부에 `mdata` 속성을 만들어 인자를 저장.
- `Mycls(5)` 호출 시 `arg=5` 가 들어가 `myData.mdata == 5`.

---

## 4. 문자열(`str`) 심화

### 4-1. 문자열은 "시퀀스(sequence) 타입"

- 시퀀스 = **요소들이 순서를 가진** 컬렉션.
- 시퀀스의 공통 기능
  1. 인덱싱(indexing): 위치로 한 개 꺼내기.
  2. 슬라이싱(slicing): 범위로 잘라내기.
  3. `len(x)` 로 길이 구하기.
  4. `in` 으로 포함 여부 확인.
- 같은 부류의 자료형: `list`, `tuple`, `range` …

### 4-2. 인덱싱

```python
str1 = "python test"
#       0123456789 10
print(str1[0])   # 'p'
print(str1[5])   # 'n'
print(str1[-1])  # 't'   (마지막 문자)
print(str1[-2])  # 's'
```

- 인덱스는 **0부터 시작**.
- 음수 인덱스는 **뒤에서부터** 세며 `-1` 이 마지막.
- 범위를 벗어나면 `IndexError`.

### 4-3. 슬라이싱 `[start : stop : step]`

```python
str2 = "python tset programming"
print(str2[7:11])  # 'tset'   인덱스 7~10
print(str2[:6])    # 'python' 처음부터 인덱스 5까지
print(str2[12:])   # 'programming' 인덱스 12부터 끝까지
```

- **`stop` 은 포함되지 않는다** (반-개구간 `[start, stop)`).
- 생략 규칙
  - `start` 생략 → 처음부터.
  - `stop` 생략 → 끝까지.
  - 파이썬 관례상 **끝까지 갈 땐 `stop` 을 비워두는 게 더 깔끔**하다.
- 응용
  ```python
  s = "abcdef"
  s[::2]   # 'ace'   2칸씩 건너뛰며
  s[::-1]  # 'fedcba' 역순(뒤집기)
  ```

### 4-4. 문자열 연산 — `+` 와 `*`

```python
str1 = "python test"
str3 = "stydy"
print(str1 + ' ' + str3)   # 'python test stydy'  연결(concatenation)
print("=" * 50)            # '=' 가 50번 반복
```

- 이를 **연산자 오버로딩(operator overloading)** 이라 한다.
  - 같은 `+` 라도 숫자에는 더하기, 문자열에는 이어붙이기로 동작.
- `*` 도 마찬가지로 문자열에서는 **반복**.

### 4-5. 반복문으로 문자열 순회

```python
strData = "AI programming"
for item in strData:
    print(item + ' ', end='')   # A I   p r o g r a m m i n g
print()        # 줄바꿈 한 번
print('\n')   # 줄바꿈 두 번(print 자체의 end='\n' + '\n')
```

- 문자열은 **이터러블(iterable)** → `for` 로 한 글자씩 꺼낼 수 있다.
- `print(item + ' ', end='')` : 글자 사이에 공백을 두면서, 줄바꿈 없이 가로로 출력.

### 4-6. 문자열은 **불변(immutable)** 객체

```python
strData3 = "AI core"
# strData3[0] = 'D'   # TypeError! 문자열 요소 변경 불가
```

- 한 번 만들어진 문자열 객체는 **내용을 바꿀 수 없다(상수처럼 동작)**.
- "변경"이 필요하면 **새 문자열을 만들어** 재할당한다.

```python
strData3 = strData3.replace("A", "D")
print(strData3)   # 'DI core'
```

- `replace(old, new)` 는 원본을 건드리지 않고 **새 문자열을 반환**.
- 그래서 결과를 받을 변수(같은 이름이든 새 이름이든)가 필요하다.

### 4-7. 자주 쓰는 문자열 메서드 (확장 학습)

| 메서드 | 설명 |
|---|---|
| `s.upper()` / `s.lower()` | 대/소문자 변환 |
| `s.strip()` | 양쪽 공백 제거 |
| `s.split(sep)` | 구분자로 나눠 리스트로 |
| `s.replace(a, b)` | a를 b로 치환 |
| `s.find(x)` | x의 위치(없으면 -1) |
| `s.startswith(x)` / `s.endswith(x)` | 시작/끝 검사 |
| `len(s)` | 길이 |

---

## 5. 문자열 포매팅과 자주 쓰는 메서드

### 5-1. 문자열 안에 변수 끼워 넣기 — `format()` vs f-string

```python
name = "홍길동"
age = 50

# (구) format 메서드 방식
print("나의 정보 ==> 이름 : {}, 나이: {}".format(name, age))

# (신) f-string 방식 — Python 3.6+
print(f"나의 정보 ==> 이름 : {name}, 나이: {age}")
```

- C/Java의 `%d`, `%s` 같은 **포맷 지정자는 파이썬에서 거의 쓰지 않는다**.
- `"...{}...{}".format(a, b)` : 중괄호 `{}` 자리에 인자가 순서대로 들어간다.
- **f-string**: 문자열 앞에 `f`를 붙이고 `{변수명}` 또는 `{식}`을 적으면 그대로 평가되어 들어간다.
  - 짧고, 식을 직접 적을 수 있어 가독성이 좋다.
  - 예: `f"내년 나이: {age + 1}"`, `f"이름 길이: {len(name)}"`.

### 5-2. 메서드 호출 — 점(`.`) 연산자

```python
strData = "python Programming"
print(strData.capitalize())   # 'Python programming'
```

- `객체.메서드()` 형태로 호출 → "그 객체에게 일을 시킨다" 는 의미.
- 점(`.`)은 C 구조체의 멤버 접근에서 유래한 **멤버 접근 연산자**.
- IDE에서 `객체.` 까지 입력하면 사용 가능한 메서드 목록이 뜬다.
- **문자열은 불변 객체** 이므로 모든 변형 메서드는 **새 문자열을 반환**, 원본은 그대로다.

### 5-3. 여러 줄 문자열 — 삼중 따옴표

```python
strData3 = """
python Programming
test python prog
python good
"""
```

- `"""..."""` 또는 `'''...'''` 안에는 줄바꿈을 그대로 적을 수 있다.
- 긴 안내문, 프롬프트 템플릿, 도큐먼트 작성 등에 유용.

### 5-4. 검색·치환·분할·결합

```python
strData3.count("python")              # 문자열 안에 'python' 이 몇 번 등장하는지

"test programming".replace("test", "python")   # 'python programming'

"test,programming,happy".replace(",", " ")     # ',' 를 공백으로

"python#test ai programming,study".split(",")  # 구분자로 잘라 리스트로 반환

"/".join(['kbs', 'mbc', 'jtbc', 'sbs'])        # 'kbs/mbc/jtbc/sbs'
```

- `count(x)` : `x` 가 몇 번 나오는지 정수로 반환.
- `replace(a, b)` : `a` 를 `b` 로 치환한 **새 문자열** 반환.
  - 한계: 한 번에 **여러 패턴을 동시에** 치환할 수 없다 → 여러 번 호출하거나 정규식을 써야 한다.
- `split(sep)` : `sep` 을 기준으로 잘라 **리스트** 반환. 인자를 생략하면 공백 기준.
- `"구분자".join(리스트)` : 리스트의 문자열들을 **구분자로 이어붙여** 하나의 문자열로.

### 5-5. 메서드 체이닝(method chaining)

```python
listData3 = "python#test ai programming,study"
result = (
    listData3
        .replace("#", ",")   # # 을 , 로
        .replace(" ", ",")   # 공백도 , 로
        .split(",")          # , 기준으로 분할
)
print(result)
# ['python', 'test', 'ai', 'programming', 'study']
```

- 각 메서드가 **새 문자열을 반환** 하므로 그 결과에 다시 메서드를 부를 수 있다.
- 괄호 `( ... )` 로 감싸면 줄을 바꿔 가며 읽기 좋게 작성할 수 있다.

### 5-6. 정규 표현식 맛보기 (참고)

```python
import re
result = re.sub(r'[#,]', ' ', "python#test,study")
# 'python test study'  ('#' 또는 ',' 를 모두 공백으로)
```

- `re.sub(패턴, 치환, 문자열)` : 패턴에 맞는 모든 부분을 한 번에 치환.
- 여러 구분자를 동시에 처리할 때 `replace` 의 한계를 보완한다. (자세한 문법은 추후 학습)

### 5-7. 자주 쓰는 문자열 메서드 정리

| 메서드 | 설명 |
|---|---|
| `s.upper()` / `s.lower()` | 대/소문자 변환 |
| `s.capitalize()` | 첫 글자만 대문자, 나머지는 소문자 |
| `s.strip()` | 양쪽 공백(또는 지정 문자) 제거 |
| `s.count(x)` | `x` 등장 횟수 |
| `s.find(x)` | `x` 의 위치(없으면 `-1`) |
| `s.replace(a, b)` | `a` → `b` 치환한 새 문자열 |
| `s.split(sep)` | 구분자로 나눠 **리스트** 반환 |
| `sep.join(리스트)` | 리스트를 구분자로 연결한 **문자열** |
| `s.startswith(x)` / `s.endswith(x)` | 시작/끝 검사 |
| `len(s)` | 길이 |

### 5-8. 컬렉션 객체 생성 문법 미리보기

```python
list_exam  = []        # 파이토닉
list_exam  = list()    # 클래스 호출 방식 — 동일한 빈 리스트

data = {}              # 빈 dict
data = dict()

data2 = ()             # 빈 tuple
data2 = tuple()

num      = int("352")  # 문자열 → 정수
list_num = list("abcdef")   # 'a','b','c','d','e','f' 6개 원소 리스트
```

- 모든 자료형은 결국 **클래스**이므로 `클래스()` 형태로도 객체를 만들 수 있다.
- 짧고 익숙한 **리터럴 표기**(`[]`, `{}`, `()`) 가 파이토닉(권장).
- `list(문자열)` 처럼 다른 시퀀스를 인자로 주면 **각 원소를 풀어** 리스트로 만들어 준다.
- 문자열은 불변이지만 **리스트는 항목을 자유롭게 수정**할 수 있다 → 다음 수업의 핵심 주제.

---

## 6. 입력(input) 과 형 변환(casting)

### 6-1. `input()` — 키보드 입력 받기

```python
data = input("데이터 입력: ")
```

- `input(prompt)` 는 다른 언어의 "출력 + 입력 대기"(C의 `printf` + `scanf`) 가 **하나로 합쳐진** 함수.
- 사용자가 Enter를 누르기 전까지 프로그램이 멈춰 기다린다.
- **중요**: `input()` 은 **무엇을 입력해도 항상 문자열(`str`)** 로 반환한다.

```python
a = input("1 입력: ")   # "10"  (사용자가 10 을 입력)
b = input("2 입력: ")   # "20"
print(a + b)            # '1020'  ← 숫자가 아니라 문자열 이어붙이기!
```

### 6-2. 형 변환(Casting) — `int()`, `float()`, `str()`

```python
a = int(input("데이터 1 입력: "))
b = int(input("데이터 2 입력: "))
print(a + b)            # 정상적인 정수 덧셈
```

- C/Java의 `(int)` 캐스팅과 달리, 파이썬은 **클래스 호출 형식 `int(x)`** 로 형 변환한다.
- 객체지향 관점에서 보면 "`int` 클래스로 새 객체를 만든다" 와 동일하다.
- 연산 시 **피연산자의 타입이 모두 같아야** 한다는 점이 핵심.

```python
int("1024")     # 1024     ← OK
int("1,024")    # ValueError! ',' 는 미리 제거해야 함
int("3.14")     # ValueError! 실수 문자열은 float() 로
float("3.14")   # 3.14
str(50)         # '50'
```

- 변환 실패 시 `ValueError` 가 발생하므로, 콤마·공백 등은 **전처리(replace/strip)** 후에 변환한다.

---

## 7. 제어 흐름 — 조건문과 반복문

### 7-1. `if / elif / else`

```python
saved_pw = 'python'
input_str = input("Password 입력(종료 : quit) ==> ")

if input_str == saved_pw:
    print("pw success!")
elif input_str == 'quit':
    print("종료합니다.")
else:
    print("pw fail!!")
```

- 조건이 참이면 그 블록 실행, 아니면 다음 `elif` / `else` 로 넘어간다.
- 콜론(`:`) 뒤에 줄을 바꾸고 **들여쓰기로 블록**을 만든다(파이썬의 핵심 문법).
- 비교 연산자: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- 동등 비교는 `==`(두 글자), 대입은 `=`(한 글자) — 구분 주의.

### 7-2. `while` 반복문

```python
while True:
    print("True")
    break   # 반드시 탈출 조건이 있어야 한다!
```

- `while 조건:` 은 조건이 참인 동안 블록을 반복.
- `while True:` 는 **항상 참** 이므로 그 자체로는 무한 루프.
- 안에서 `break` 또는 조건 변경이 없으면 프로그램이 멈추지 않는다.

### 7-3. 무한 루프 + `break` 패턴 (자주 쓰는 입력 검증)

```python
saved_pw = 'python'

while True:
    input_str = input("Password 입력(종료 : quit) ==> ")
    if input_str == saved_pw:
        print("pw success!")
        break             # 비밀번호 맞으면 반복 종료
    elif input_str == 'quit':
        break             # 사용자가 quit 입력해도 종료
    else:
        print("pw fail!!")  # 다시 입력 받기
```

- **무한 루프 + 내부 `break`** 는 "조건이 만족될 때까지 반복" 하는 매우 일반적인 구조.
- 흐름
  1. `while True:` 로 일단 들어간다.
  2. `input()` 으로 사용자에게 받는다.
  3. `if` 로 분기 → 만족하면 `break`, 아니면 다시 처음으로.
- 핵심 키워드
  - `break` : 현재 반복문을 **즉시 탈출**.
  - `continue` : 이번 회차만 건너뛰고 **다음 회차로**.

### 7-4. 들여쓰기 = 블록 (다시 강조)

- 파이썬은 중괄호 `{ }` 가 없으므로, **들여쓰기 칸 수가 곧 블록의 경계** 다.
- `if`, `elif`, `else`, `while`, `for`, `def`, `class` 모두 동일.
- 같은 블록 안에서는 들여쓰기를 **반드시 동일하게** 맞춘다(공백 4칸 권장).

---

## 8. 들여쓰기(Indentation) — 파이썬의 문법

```python
for item in strData:
    print(item)        # 4칸 들여쓰기 → for의 블록
print("loop end")      # 들여쓰기 없음 → for 바깥
```

- 파이썬은 다른 언어의 `{ ... }` 대신 **들여쓰기로 코드 블록을 표현**한다.
- 같은 블록 안에서는 **들여쓰기 칸 수가 동일**해야 한다.
  - 보통 **공백 4칸**이 표준(PEP 8).
  - 탭과 공백을 섞으면 `IndentationError`.
- 조건문, 반복문, 함수, 클래스 모두 마찬가지.

---

## 9. 한 줄 요약 체크리스트

- [ ] `print()` 는 `sep`, `end` 같은 **기본값(default) 파라미터** 를 갖는다.
- [ ] 파이썬 변수는 값이 아니라 **객체의 id(주소)** 를 저장한다 → 동적 타이핑.
- [ ] `type(x)` 는 클래스, `id(x)` 는 메모리 주소를 반환.
- [ ] 기본 클래스: `int`, `float`, `str`, `bool`.
- [ ] 문자열은 **시퀀스이자 불변(immutable)** 객체.
- [ ] 인덱싱은 **0부터**, 음수는 **뒤에서부터**(`-1`이 마지막).
- [ ] 슬라이싱 `[a:b]` 는 **`b` 미포함**.
- [ ] `+` 는 연결, `*` 는 반복(연산자 오버로딩).
- [ ] 문자열 수정은 **새 객체 생성**으로(예: `replace`).
- [ ] **f-string** `f"{var}"` 가 `.format()` 보다 간결한 최신 문법이다.
- [ ] `split()` 은 **리스트로**, `join()` 은 **문자열로** 변환한다.
- [ ] `replace` 는 동시에 여러 패턴을 못 바꾼다 → 체이닝 또는 정규식.
- [ ] `input()` 의 반환값은 **항상 `str`** → 숫자 연산하려면 `int()` / `float()` 캐스팅.
- [ ] `while True:` 무한 루프는 반드시 **`break` 탈출 조건**과 함께.
- [ ] 들여쓰기가 곧 블록 — **칸 수 일관성** 필수.

---

## 10. 셀프 체크 문제 (정답은 생각만)

1. `print("hi", "there", sep="_", end="!!")` 의 출력은?
2. 아래 코드의 출력 결과를 예상해 보세요.
   ```python
   data = 10
   id1 = id(data)
   data = data + 1
   id2 = id(data)
   print(id1 == id2)
   ```
3. `s = "ABCDEFG"` 에서 `"CDE"` 를 얻는 슬라이싱 식을 모두 적어 보세요.
4. `"-" * 5 + "GO" + "-" * 5` 의 결과는?
5. 다음 코드의 오류 원인은?
   ```python
   s = "hello"
   s[0] = "H"
   ```
6. 다음 코드가 의도대로 두 수의 합을 출력하려면 어디를 고쳐야 할까요?
   ```python
   a = input("a: ")
   b = input("b: ")
   print(a + b)
   ```
7. `"kbs , mbc , jtbc , sbs"` 를 양옆 공백 없는 `['kbs','mbc','jtbc','sbs']` 로 만들려면?
   (힌트: `replace` → `split`, 또는 `split` → 각 항목 `strip`)
8. f-string으로 `"이름: 홍길동 / 내년 나이: 51"` 을 출력하는 코드를 적어 보세요. (변수 `name`, `age=50` 가정)
9. 비밀번호 `"python"` 이 맞을 때까지 반복해서 입력받는 코드를 `while` 과 `break` 만 사용해 작성해 보세요.
10. `"a-b-c-d".split("-")` 와 `"-".join(["a","b","c","d"])` 의 결과는 각각 무엇인가요?

> 풀이 힌트는 위 본문에 모두 들어 있습니다. 막히면 해당 절을 다시 읽어보세요!
