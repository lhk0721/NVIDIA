# Python 학습 저장소

파이썬 기초부터 데이터 전처리까지 일자별로 학습한 연습 코드와 복습 노트를 모아둔 저장소입니다.
각 프로젝트 폴더는 자체 가상환경(venv)을 포함하며, 가상환경 파일은 `.gitignore`로 추적에서 제외됩니다.

## 디렉터리 구조

```
python_project/
├─ python_basic/          # 파이썬 기초 학습
│  ├─ src/
│  │  ├─ 20260518/        # 자료형 · 문자열 · 입출력(print/input)
│  │  ├─ 20260519/        # 리스트 · 딕셔너리 · 튜플 · 모듈 · 엑셀 읽기 · GUI
│  │  ├─ 20260520/        # 조건문 · 반복문 · 함수 · 집합(set) · dict.get
│  │  ├─ 20260521/        # 파일 입출력 · 함수 · 스코프
│  │  ├─ 20260522/        # os/shutil · 정규표현식 · 웹 크롤링(네이버 뉴스·유튜브 랭킹)
│  │  └─ 20260526/        # 클래스 설계
│  └─ requirements.txt
├─ data_preprossesing/    # 데이터 전처리
│  └─ src/
│     ├─ 20260526/        # NumPy 기초 · 연산 · 내적
│     └─ 20260527/        # Pandas · matplotlib(한글 폰트) · Excel/CSV 다루기
├─ reference/             # 참조용 데이터 (Health_info.csv)
└─ .gitignore
```

각 일자 폴더에는 그날 배운 내용을 정리한 `REVIEW.md` 복습 노트가 함께 들어 있습니다.

## 환경

- Python 3.10
- 주요 패키지: `numpy`, `pandas`, `python-dateutil`, `pytz` (전체 목록은 `python_basic/requirements.txt` 참고)

### 가상환경 사용

각 프로젝트 폴더(`python_basic`, `data_preprossesing`)에는 가상환경이 풀려 있습니다.
PowerShell에서 다음과 같이 수동으로 활성화합니다.

```powershell
.\python_basic\Scripts\Activate.ps1
```

> VS Code 통합 터미널에서의 자동 activate는 `.vscode/settings.json`에서 꺼 두었습니다(`python.terminal.activateEnvironment: false`).

## 라이선스

개인 학습용 저장소입니다.
