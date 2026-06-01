# 판다스(Pandas) DataFrame 메서드 정리

> 2026-05-27 ~ 2026-06-01 수업에서 사용된 pandas DataFrame 관련 메서드와 핵심 인자 총정리

---

## 0. 기본 개념

- **판다스**: 넘파이(numpy)의 상위 라이브러리, 데이터 분석에 특화
- 두 가지 핵심 객체
  - `Series`: 1차원 배열 형태 (DataFrame의 한 컬럼을 선택하면 Series가 됨)
  - `DataFrame`: 2차원 배열 형태
- 인덱스 종류
  - **명시적 인덱스(라벨 인덱스)**: 눈에 보이는 문자열/지정 인덱스 → `loc` 사용
  - **암묵적 인덱스(수치 인덱스)**: 자동 부여되는 정수 인덱스 → `iloc` 사용
- 넘파이 2차원 배열은 수치 인덱스만 가능하지만, 판다스는 수치 + 라벨 둘 다 지원

---

## 1. 객체 생성

### `pd.DataFrame()` — DataFrame 객체 생성
| 인자 | 설명 |
|------|------|
| `data` | 사전(dict), 리스트, numpy 배열 등 |
| `columns` | 열(컬럼) 인덱스 지정 |
| `index` | 행 인덱스 지정 (`list('abc')` 형태도 가능) |

```python
# 1) 사전(dict)으로 생성 — key가 컬럼이 됨
mydf = pd.DataFrame({"kor":[50,60,70], "eng":[80,90,77]}, index=list('abc'))

# 2) 리스트로 생성
myDf = pd.DataFrame([[60,80,70],[90,50,85]], columns=['국어','영어','수학'], index=['a','b'])

# 3) numpy 배열로 생성
myDf = pd.DataFrame(np.arange(10,25).reshape((5,3)), columns=['one','two','three'], index=list('abcde'))
```

### `pd.DataFrame.from_dict()` — 사전을 DataFrame으로
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `data` | — | 변환할 사전(dict) |
| `orient` | `'columns'` | `'columns'`=key를 컬럼으로 / `'index'`=key를 **행 인덱스**로 |
| `columns` | `None` | 컬럼명 지정 (`orient='index'`일 때 사용) |

```python
myDf = pd.DataFrame.from_dict(categoryList, orient='index', columns=['Freq'])
```

---

## 2. 속성 확인 (메서드 아님)

| 속성 | 반환 |
|------|------|
| `df.columns` | 컬럼 인덱스 반환 (수정도 가능: `df.columns = [...]`) |
| `df.index` | 행 인덱스 반환 (수정도 가능: `df.index = [...]`) |
| `df.values` | 내용물을 numpy 배열로 반환 |
| `df.index.name` | 인덱스 이름 (지우기: `df.index.name = ''`) |

```python
df.columns = ["국어", "영어"]          # 컬럼 인덱스 통째로 수정
df.index = ['국어','영어','수학','음악','과학']  # 행 인덱스 통째로 수정
```

---

## 3. 데이터 확인 / 정보

| 메서드 | 핵심 인자 | 설명 |
|--------|-----------|------|
| `df.info()` | `verbose`, `show_counts` | 데이터 정보 확인 (※ `print()` 없이 직접 호출. 반환값 아님) |
| `df.head(n)` | `n=5` | 앞에서 n행 출력 |
| `df.tail(n)` | `n=5` | 뒤에서 n행 출력 |
| `df.sample(n)` | `n`, `frac`, `random_state`, `replace` | 무작위 표본 추출 |
| `df['col'].unique()` | — | 컬럼의 고유값(중복 제거) 반환 (인자 없음) |
| `df['col'].value_counts()` | `normalize`, `sort`, `ascending`, `dropna` | 컬럼의 값별 빈도수 집계 (Series 반환) |

#### `sample()` 핵심 인자
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `n` | `1` | 추출할 행 개수 |
| `frac` | `None` | 비율로 추출 (예: `0.1`=전체의 10%). `n`과 동시 사용 불가 |
| `random_state` | `None` | 난수 시드 고정 → 같은 값이면 항상 같은 표본 (재현성) |
| `replace` | `False` | `True`면 중복 허용 추출(복원 추출) |

```python
popdf.info()
popdf.head(10)
my_df['호선_명칭'].unique()
df['day'].value_counts()
```

#### `value_counts()` 핵심 인자
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `normalize` | `False` | `True`면 개수 대신 **상대 비율(0~1)** 로 반환 |
| `sort` | `True` | 빈도수 기준 정렬 여부 |
| `ascending` | `False` | `False`=빈도 많은 순(내림차순), `True`=적은 순 |
| `dropna` | `True` | `True`면 NaN 제외, `False`면 NaN도 카운트 |
| `bins` | `None` | 수치형일 때 구간(bin) 개수로 묶어서 집계 |

```python
df['day'].value_counts()                    # 빈도 많은 순 (기본)
df['day'].value_counts(normalize=True)      # 비율로 반환
df['day'].value_counts(ascending=True)      # 적은 순 정렬
df['day'].value_counts(dropna=False)        # NaN도 포함해서 카운트
```

> 결과는 빈도가 값(value), 고유항목이 인덱스인 Series → `pd.DataFrame(...)`로 감싸면 표로 활용 가능.

---

## 4. 선택 / 접근 (Selection)

### 컬럼 선택
```python
df['kor']              # 단일 컬럼 → Series 반환
df[['Hong','Park']]    # 여러 컬럼 → 반드시 리스트로! DataFrame 반환
```

### `loc` — 라벨(명시적) 인덱스로 접근
```python
df.loc['c', 'two']             # 단일 위치
df.loc['eng':'math', 'Kim':'Park']   # 슬라이싱 (라벨은 stop 포함!)
df.loc[df['Kim'] >= 70, 'Kim':'Park']  # 불린 색인 (loc만 지원)
```
- **라벨 슬라이싱은 마지막(stop)을 포함**
- 불린 배열(boolean) 색인은 `loc`만 지원

### `iloc` — 정수(암묵적) 인덱스로 접근
```python
df.iloc[2, 1]          # 단일 위치
df.iloc[1:3, 1:3]      # 슬라이싱 (정수는 stop-1까지)
df.iloc[[1,3], :]      # 팬시 인덱싱 (추출할 인덱스 배열 전달)
```
- **정수 슬라이싱은 stop-1까지** (일반 파이썬과 동일)

---

## 5. 추가 / 수정

```python
# 새 컬럼 추가
myDf['four'] = list(range(5))   # 리스트로
myDf['four'] = 0                # 단일값 → 브로드캐스트
myDf['four'] = np.nan           # 결측치(NaN)로

# 새 행 추가 (라벨 인덱스로만 — loc 사용)
myDf.loc[5] = np.nan
```

> ⚠️ `iloc`/`loc`로 잘라낸 subset은 원본과 **view 관계**(numpy 상속) → subset 수정 시 원본도 바뀜.
> 독립 사본이 필요하면 반드시 `.copy()` 사용.

### `df.copy()` — 완전 복제 (view 관계 끊기)
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `deep` | `True` | `True`=데이터·인덱스까지 완전 복제(원본과 독립). `False`=얕은 복사(원본과 데이터 공유) |

```python
subset = df.loc['eng':'math', 'Kim':'Park'].copy()
```

---

## 6. 삭제

### `del` 키워드 — 단일 컬럼 삭제
```python
del df['Park']
```

### `df.drop()` — 행/열 삭제
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `labels` | — | 삭제할 라벨 (리스트로 여러 개 가능) |
| `axis` | `0` | `0`=행, `1`=열 (어느 축으로 삭제할지) |
| `index` | `None` | 삭제할 행 라벨 직접 지정 (`axis` 없이 사용) |
| `columns` | `None` | 삭제할 열 라벨 직접 지정 (`axis` 없이 사용) |
| `inplace` | `False` | `True`=원본 직접 반영(None 반환), `False`=사본 반환 |

```python
df.drop(['Hong','Park'], axis=1, inplace=True)   # 열 삭제
df.drop(['eng','music'], axis=0, inplace=True)   # 행 삭제
popdf.drop([0], axis=0, inplace=True)            # 인덱스 0번 행 삭제
df.drop(columns=['Hong','Park'], inplace=True)   # columns= 로 열 삭제 (axis 불필요)
```

> `inplace=True`면 원본 반영 후 `None` 반환 → 변수에 재할당하면 안 됨.
> DataFrame은 메모리를 많이 쓰므로 `inplace`가 필요한 시점이 옴.

---

## 7. 결측치(NaN) 처리

| 메서드 | 핵심 인자 | 설명 |
|--------|-----------|------|
| `df.isna()` / `df['col'].isnull()` | — | NaN이면 True인 불린 배열 반환 |
| `df.dropna()` | `axis`, `how`, `inplace` | 결측치 행/열 제거 |

#### `dropna()` 핵심 인자
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `axis` | `0` | `0`=결측치 있는 행 삭제 / `1`=열 삭제 |
| `how` | `'any'` | `'any'`=하나라도 NaN이면 삭제 / `'all'`=모두 NaN일 때만 삭제 |
| `subset` | `None` | 검사할 특정 컬럼(행)만 지정 (예: `subset=['남자']`) |
| `thresh` | `None` | 정상값(non-NaN)이 N개 미만인 행/열 삭제 (`how`보다 우선) |
| `inplace` | `False` | 원본 반영 여부 |

```python
popdf.dropna(axis=0, how='any', inplace=True)
popdf.dropna(subset=['남자'], inplace=True)   # '남자' 컬럼이 NaN인 행만 삭제
popdf.loc[popdf['남자'].isnull(), :]          # 결측치 행 추출
```

---

## 8. 인덱스 재설정

### `df.reset_index()` — 인덱스 초기화
| 인자 | 설명 |
|------|------|
| `drop=False` | 기본값. 기존 인덱스를 컬럼으로 올림 |
| `drop=True` | 기존 인덱스 제거하고 새 정수 인덱스 부여 |
| `inplace` | 원본 반영 여부 |

```python
popdf.reset_index(inplace=True, drop=True)   # 결측치 삭제 후 인덱스 초기화 권장
```

### `df.set_index()` — 특정 컬럼을 인덱스로 설정
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `keys` | — | 인덱스로 쓸 **컬럼명**. 첫 번째 위치 인자 |
| `drop` | `True` | 인덱스로 올린 컬럼을 원본 컬럼에서 제거 (`False`면 컬럼으로도 남겨둠) |
| `append` | `False` | `True`면 기존 인덱스를 **유지한 채** 추가 → 멀티인덱스 |
| `verify_integrity` | `False` | `True`면 인덱스에 중복값이 있는지 검사(있으면 에러) |
| `inplace` | `False` | 원본 반영 여부 |

> **`keys`(첫 인자) 주는 방법** — 어떤 형태로 주느냐에 따라 결과가 달라진다.
> - **문자열 1개** → 그 컬럼 하나를 인덱스로: `df.set_index('자치구')`
> - **리스트 `[...]`** → 여러 컬럼을 묶어 **멀티인덱스(계층 인덱스)**: `df.set_index(['시도', '자치구'])`
>   (리스트 안 순서대로 바깥→안쪽 레벨이 된다)
> - 반드시 **DataFrame에 실제로 존재하는 컬럼명**이어야 한다(없으면 `KeyError`).
> - 정수 인덱스로 되돌리려면 [[#8-인덱스-재설정]]의 `reset_index()` 사용.

```python
popdf.set_index('자치구', inplace=True)              # 단일 컬럼 → 인덱스
my_df.set_index('기준_날짜', inplace=True, drop=True) # 올린 컬럼은 제거(기본)
df.set_index('이름', drop=False)                     # 인덱스로 쓰되 컬럼으로도 유지
df.set_index(['시도', '자치구'])                      # 리스트 → 멀티인덱스
```

---

## 9. 정렬

### `df.sort_values()` — 값 기준 정렬
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `by` | — | 정렬 기준 컬럼 (리스트로 여러 컬럼 가능) |
| `ascending` | `True` | `True`=오름차순, `False`=내림차순 (리스트로 컬럼별 지정 가능) |
| `inplace` | `False` | 원본 반영 여부 |
| `na_position` | `'last'` | NaN 위치 (`'last'`=뒤 / `'first'`=앞) |

> 참고: 값이 아닌 **인덱스 기준** 정렬은 `df.sort_index()` 사용.

```python
myDf.sort_values('Freq', ascending=False, inplace=True)
df.sort_values(by=['Video'], ascending=False, inplace=True)
df.sort_values(by=['gender'], ascending=True, inplace=True)
```

---

## 10. 조건 / 필터링

### `df['col'].isin()` — 특정 값 포함 여부
- 인자로 **리스트** 전달 (단일 값이어도 리스트로), 불린 배열 반환

```python
my_df['호선_명칭'].isin(['3호선','7호선','9호선'])
subset = df.loc[df['day'].isin(['Sat','Thur']), :].copy()
subset = df.loc[df['time'].isin(['Lunch']), 'tip':'time']
```

### 불린 색인 (Boolean Indexing)
```python
df['Kim'] >= 70                        # 불린 배열 생성
subset = df.loc[df['Kim'] >= 70, 'Kim':'Park'].copy()

# isin()이 만든 불린 배열을 loc의 행 조건으로 그대로 사용
df['time'].isin(['Lunch'])             # 불린 배열 생성
subset = df.loc[df['time'].isin(['Lunch']), 'tip':'time']
# → 행: time이 'Lunch'인 행만 / 열: 'tip'~'time' 슬라이싱
```
> `>=` 같은 비교 연산뿐 아니라 `isin()`처럼 **불린 배열을 반환하는 것은 모두** `loc`의 행 색인으로 쓸 수 있다.

---

## 11. 함수 적용 (Function Apply)

> DataFrame/Series의 각 요소에 함수를 일괄 적용. (최신 버전에서 `applymap`은 `map`으로 통합됨)

### `Series.map()` — 매핑/치환
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `arg` | — | 적용할 대상: 함수 / lambda / 사전(dict) 모두 가능 |
| `na_action` | `None` | `'ignore'`면 NaN은 함수 적용 없이 건너뜀 |

```python
df['성별'].map(DataControl)                  # 함수 전달
df['gender'].map({'Male':0, 'Female':1})     # 사전으로 값 치환
df['ChannelName'].map(lambda x: x.split()[0])  # lambda
df['Video'].map(lambda x: int(re.sub(r'[,개]','',x)))
```

### `Series.apply()` / `DataFrame.apply()` — 함수 적용
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `func` | — | 적용할 함수 / lambda |
| `axis` | `0` | (**DataFrame.apply 전용**) `0`=열 단위 / `1`=행 단위로 함수 적용 |
| `args` | `()` | 함수에 넘길 추가 위치 인자 (튜플) |

```python
df['Hong'] = df['Hong'].apply(lambda x: x+5)
df['ChannelName'] = df['ChannelName'].apply(Shorter)
df.loc[df['호선_명칭'].apply(Find), :]
df.apply(lambda row: row['kor'] + row['eng'], axis=1)   # 행 단위 적용
```

> ⚠️ `df['col'] = df['col'].map(...)` 처럼 **재할당해야 원본이 갱신**됨.

---

## 12. 집계 / 통계

넘파이와 동일한 집계 메서드 제공: `sum`, `min`, `max`, `mean`

```python
df['a'].mean()
df['a'].max()
df.loc['eng'].sum()
subset['size'].mean()

# 집계 응용
df['subjectTotal'] = [df.loc[x].sum() for x in df.index]   # 행별 합계
df.loc['mean'] = [df[x].mean() for x in df.columns]        # 열별 평균
```

---

## 13. 타입 변환

### `df['col'].astype()` — 컬럼 타입 일괄 변환
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `dtype` | — | 변환할 타입 (`'int64'`, `'float'`, `'str'`, `'category'` 등). 첫 번째 위치 인자 |
| `errors` | `'raise'` | `'raise'`=변환 실패 시 에러 / `'ignore'`=실패 시 원본 유지 |

> **`astype`이란** — 컬럼(Series) 전체의 **데이터 타입(dtype)** 을 한 번에 바꾼다.
> CSV/엑셀로 읽으면 숫자가 문자열(`object`)로 들어오는 경우가 많은데, 계산·정렬을 하려면 숫자 타입으로 변환해야 한다.
>
> **`dtype`(첫 인자) 주는 방법** — 문자열로 타입 이름을 넘긴다.
> - 정수: `'int'` / `'int64'`  · 실수: `'float'` / `'float64'`
> - 문자열: `'str'`  · 범주형(메모리 절약): `'category'`  · 불린: `'bool'`
> - 파이썬 타입 객체로도 가능: `df['a'].astype(int)`
> - 사전으로 **여러 컬럼을 한 번에**: `df.astype({'kor':'int', 'eng':'float'})`
>
> ⚠️ 주의
> - **재할당해야 반영**된다: `df['col'] = df['col'].astype(...)`
> - 문자열에 `,`·`개`·공백 등이 섞여 있으면 `int` 변환이 실패한다 → 먼저 `map`/`replace`로 제거한 뒤 변환.
>   (예: [[#11-함수-적용-function-apply]]의 `df['Video'].map(lambda x: int(re.sub(r'[,개]','',x)))`)
> - NaN이 섞인 컬럼은 정수(`int`)로 못 바꾼다(NaN은 float) → `dropna` 후 변환하거나 `'Int64'`(대문자, nullable 정수) 사용.

```python
df['Video'].astype('int64')                       # 변환 결과만 반환(원본 그대로)
df['Video'] = df['Video'].astype('int64')         # 재할당해야 반영됨
df['gender'] = df['gender'].astype('category')    # 범주형으로(메모리 절약)
df = df.astype({'kor':'int', 'eng':'float'})      # 사전으로 여러 컬럼 한 번에
```

### `pd.to_datetime()` — 문자열 → 시계열
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `arg` | — | 변환할 대상 (Series, 문자열 등). 첫 번째 위치 인자 |
| `format` | `None` | 날짜 형식 직접 지정 (예: `'%Y-%m-%d'`) → 속도·정확도 향상 |
| `errors` | `'raise'` | `'coerce'`면 변환 실패 값을 `NaT`로 처리 |
| `dayfirst` | `False` | `True`면 `'01/02/2025'`를 2월 1일이 아닌 **1월 2일**로 해석 안 함(일을 앞으로) |

> **인자 주는 방법**
> - `df.set_index`와 마찬가지로 **첫 인자(`arg`)는 변환할 컬럼(Series)** 을 그대로 넘긴다: `pd.to_datetime(df['데이터기준일자'])`
> - 변환 결과는 새 Series이므로 **재할당해야 원본 컬럼이 datetime으로 바뀐다**: `df['col'] = pd.to_datetime(df['col'])`
> - `format`은 **원본 문자열 생김새**에 맞춘다 (`'20250101'` → `'%Y%m%d'`, `'2025-01-01'` → `'%Y-%m-%d'`, `'2025/01/01 13:30'` → `'%Y/%m/%d %H:%M'`).
>   - 자주 쓰는 서식: `%Y`(4자리 연), `%m`(월), `%d`(일), `%H`(시), `%M`(분), `%S`(초)
> - 깨진/빈 날짜가 섞여 있으면 `errors='coerce'`로 에러 대신 `NaT`(결측) 처리 → 이후 `dropna()`로 정리.
> - 변환 후에는 `df['col'].dt.year`, `.dt.month`, `.dt.day` 처럼 `.dt` 접근자로 연·월·일을 꺼낼 수 있다.

```python
my_df['기준_날짜'] = pd.to_datetime(my_df['기준_날짜'])               # 기본
df['데이터기준일자'] = pd.to_datetime(df['데이터기준일자'])           # 재할당해야 반영
pd.to_datetime(my_df['기준_날짜'], format='%Y-%m-%d', errors='coerce') # 서식 지정 + 실패는 NaT
df['연도'] = pd.to_datetime(df['날짜']).dt.year                       # 변환 후 연도 추출
```

### `pd.date_range()` — 시계열 범위 데이터 생성
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `start` | — | 시작 날짜 |
| `end` | `None` | 끝 날짜 (`periods` 대신 사용 가능) |
| `periods` | `None` | 생성할 개수 |
| `freq` | `'D'` | 주기 (`'D'`=일, `'W'`=주, `'M'`=월말, `'H'`=시간 등) |

```python
index_data = pd.date_range('2025.12.25', periods=30, freq='D')
```

---

## 14. 결합

### `pd.concat()` — DataFrame 이어붙이기
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `objs` | — | 이어붙일 DataFrame들의 **리스트** |
| `axis` | `0` | `0`=세로(행 방향)로 쌓기 / `1`=가로(열 방향)로 붙이기 |
| `ignore_index` | `False` | `True`면 기존 인덱스 무시하고 0부터 새 인덱스 부여 |
| `join` | `'outer'` | `'outer'`=합집합 / `'inner'`=교집합(공통 컬럼만) |

```python
subset_concat = pd.concat([subset1, subset2, subset3, subset4])
pd.concat([df1, df2], ignore_index=True)     # 인덱스 새로 부여
pd.concat([df1, df2], axis=1)                # 옆으로 붙이기
```

---

## 15. 이름 변경

### `df.rename()` — 컬럼/인덱스명 변경
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `columns` | `None` | `{'기존':'변경'}` 사전 형태로 **컬럼명** 변경 |
| `index` | `None` | `{'기존':'변경'}` 사전 형태로 **행 인덱스명** 변경 |
| `inplace` | `False` | 원본 반영 여부 |

```python
dataDf.rename(columns={'count':'CategoryFreq'}, inplace=True)
df.rename(index={'kor':'국어', 'eng':'영어'}, inplace=True)   # 인덱스명 변경
```

---

## 16. 파일 입출력 (I/O)

### 읽기

#### `pd.read_csv()`
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `filepath` | — | 파일 경로 (`r'...'` raw 문자열이면 `\` 이스케이프 불필요) |
| `encoding` | `'utf-8'` | 인코딩 (`'CP949'`=한글 csv) |
| `header` | `'infer'` | `None`이면 첫 행을 데이터로 취급(자동 컬럼 인식 해제) |
| `names` | `None` | 컬럼명 직접 지정 (리스트) |
| `sep` | `','` | 구분자 (탭이면 `'\t'`) |
| `index_col` | `None` | 인덱스로 쓸 컬럼 (번호/이름) |

> **`index_col` 자세히**
> - 지정 안 하면(`None`) 0,1,2… 정수 인덱스가 **자동 추가**되고, 파일의 모든 컬럼은 데이터(컬럼)로 들어온다.
> - `index_col=0` → **0번째(맨 왼쪽) 컬럼**을 행 인덱스로 사용. 이미 식별자(이름·날짜 등)가 첫 컬럼에 있을 때, 불필요한 정수 인덱스가 추가되는 걸 막아준다.
> - 번호 대신 **컬럼명**도 가능: `index_col='자치구'`.
> - 여러 컬럼을 리스트로 주면 **멀티인덱스**: `index_col=[0, 1]`.
> - 안 주고 읽은 뒤 나중에 [[#8-인덱스-재설정]]의 `set_index()`로 바꿔도 결과는 같다.

```python
df = pd.read_csv('파일.csv', encoding='CP949')
df = pd.read_csv('scoreData.csv', header=None)
df = pd.read_csv('scoreData.csv', names=['kor','eng','math','total'])
df = pd.read_csv(r'C:\...\tips.csv')   # raw 문자열로 윈도우 경로
df = pd.read_csv('youtube.csv', index_col=0)        # 맨 왼쪽 컬럼을 인덱스로
df = pd.read_csv('seoul.csv', index_col='자치구')   # 컬럼명으로 지정
```

#### `pd.read_excel()`
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `io` | — | 엑셀 파일 경로 (`.xls`, `.xlsx`) |
| `index_col` | `None` | 인덱스로 쓸 컬럼 번호/이름 (`index_col=0` = 맨 왼쪽 컬럼) |
| `sheet_name` | `0` | 읽을 시트 (번호 또는 이름) |
| `header` | `0` | 헤더로 쓸 행 번호 |

> `index_col` 동작은 `read_csv`와 동일하다(위의 "`index_col` 자세히" 참고).
> 엑셀은 맨 왼쪽에 라벨 컬럼(이름·날짜 등)이 있는 경우가 많아 `index_col=0`을 자주 쓴다.

```python
popdf = pd.read_excel('population_in_seoul.xls')
df = pd.read_excel('youtube_rank_1000.xlsx', index_col=0)
```

### 쓰기

#### `df.to_excel()` / `df.to_csv()`
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `path` | — | 저장 경로 |
| `index` | `True` | `False`면 인덱스 저장 안 함 |
| `sheet_name` | `'Sheet1'` | (to_excel) 시트명 |
| `encoding` | — | (to_csv) 저장 인코딩 (`'CP949'`, `'utf-8-sig'` 등) |

```python
myDf.to_excel('Mydata.xlsx', index=False)
df.to_excel('youtube_data.xlsx')
df.to_csv('out.csv', index=False, encoding='utf-8-sig')
```

---

## 17. 시각화 (Plot)

> matplotlib의 plot 기능을 pandas에 내장

| 메서드 | 설명 |
|--------|------|
| `df.plot.bar()` | 막대 그래프 |
| `df.plot.pie()` | 파이 차트 |

`plot.pie()` 핵심 인자:
| 인자 | 설명 |
|------|------|
| `y` | 값으로 쓸 컬럼 |
| `colors` | 조각별 색상 리스트 |
| `legend` | 범례 표시 여부 |
| `startangle` | 시작 각도 (예: `90`) |
| `autopct` | 비율 표시 포맷 (예: `'%.2f%%'`) |
| `explode` | 조각 분리 정도 (리스트) |
| `wedgeprops` | 조각 테두리/너비 스타일 (사전) |

`plot.bar()` 핵심 인자: `color`(막대 색상 리스트) 등

```python
df.plot.bar(color=['lightskyblue','lightsalmon','lightpink'])
plt.show()

dataDf_top5.plot.pie(
    y='CategoryFreq',
    colors=color,
    legend=False,
    startangle=90,
    wedgeprops={'width':0.5, 'edgecolor':'black', 'linewidth':3},
    autopct='%.2f%%',           # 비율 표시 포맷
    explode=[0.1]*len(dataDf_top5.index)   # 조각 분리
)
plt.show()
```

---

## 18. 반복 / 순회

### `df.itertuples()` — 행 단위 순회 (튜플)
| 인자 | 기본값 | 설명 |
|------|--------|------|
| `index` | `True` | `True`면 튜플 첫 요소로 인덱스 포함 |
| `name` | `'Pandas'` | 반환 namedtuple 이름 (`None`이면 일반 튜플) |

```python
for row in df.itertuples():
    table.add_row(row)

for rows in popdf.index:   # 인덱스 순회
    print(rows)
```

---

## 19. 출력 옵션 제어 (display options)

```python
pd.set_option('display.max_rows', 1000)      # 최대 출력 행 수
pd.set_option('display.max_columns', 500)    # 최대 출력 열 수
pd.set_option('display.width', 1000)         # 출력 너비
pd.set_option('max_colwidth', 1000)          # 컬럼 너비
pd.set_option('display.float_format', '{:.3f}'.format)  # float 소수점 3자리

# numpy 출력 옵션
np.set_printoptions(precision=3)             # 소수점 3자리
np.set_printoptions(threshold=np.inf)        # 무한 출력
np.set_printoptions(suppress=True)           # 과학적 표기법 억제
```

---

## 부록: 핵심 인자 요약

| 인자 | 주로 쓰이는 메서드 | 의미 |
|------|-------------------|------|
| `inplace` | drop, dropna, set_index, reset_index, sort_values, rename | `True`=원본 직접 수정(None 반환) |
| `axis` | drop, dropna, concat, apply | `0`=행, `1`=열 |
| `how` | dropna | `'any'`=하나라도 NaN / `'all'`=전부 NaN |
| `drop` | set_index, reset_index | 인덱스 처리한 컬럼 제거 여부 |
| `subset` | dropna | 검사할 특정 컬럼만 지정 |
| `by` | sort_values | 정렬 기준 컬럼 |
| `ascending` | sort_values, value_counts | `True`=오름차순 |
| `na_position` | sort_values | NaN 위치 (`'last'`/`'first'`) |
| `normalize` | value_counts | `True`=비율로 반환 |
| `encoding` | read_csv, to_csv | 파일 인코딩 (`'CP949'`) |
| `header` | read_csv, read_excel | 헤더 행 지정 (`None`=헤더 없음) |
| `names` | read_csv | 컬럼명 직접 지정 |
| `index_col` | read_csv, read_excel | 인덱스로 쓸 컬럼 |
| `index` | DataFrame, to_excel, rename | 행 인덱스 / 저장 시 인덱스 포함 여부 |
| `columns` | DataFrame, drop, rename, from_dict | 컬럼 인덱스 |
| `orient` | from_dict | `'index'`=key를 행으로 |
| `ignore_index` | concat | `True`=인덱스 새로 부여 |
| `deep` | copy | `True`=완전 독립 복제 |
