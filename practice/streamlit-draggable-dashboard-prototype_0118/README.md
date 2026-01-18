# README - Streamlit SHAP Dashboard (Prototype)

> **목표:** Streamlit에서 SHAP 기반 모델 해석 대시보드를 만들고,
> 

> **패널을 Drag & Drop 으로 재배치 가능한 UI**까지 도전하는 프로토타입 프로젝트.
> 

현재는 **프로토타입 단계(미완성)**로 남기고,

추후 실력과 이해도가 더 쌓이면 **진짜 드래그 UX 완성 버전으로 재도전**할 예정입니다.

## 📸 스크린샷

-

Dashboard Preview

-

Data Visualization

## ✅ 구현된 것 (현재 상태)

- ✅ 게임 플레이 로그 샘플 데이터 생성
- ✅ RandomForest / XGBoost 학습 후 성능 비교 및 모델 선택
- ✅ SHAP 기반 분석
    - 전체 중요도(Summary plot)
    - 선택 플레이어 단일 분석(기여도)
- ✅ Plotly 기반 EDA 시각화
- ✅ Streamlit UI 구성 (Panel 1 ~ Panel 4)

## ❌ 왜 "미완성"으로 남기나?

### 드래거블의 정의

- **진짜 드래거블 대시보드**는 마우스로 **끌어서(Drag & Drop)** 패널 위치를 바꿀 수 있어야 함
- ⬆️⬇️ 버튼으로 순서만 바꾸는 방식은 **재배치**이지, 드래그는 아님

### Streamlit 기본 한계

- Streamlit 기본 컴포넌트만으로는 진짜 Drag & Drop 구현이 어려움
- `streamlit-elements` 같은 외부 컴포넌트를 활용하는 방식이 현실적

### 실패 원인 (상세)

**핵심 문제:** `streamlit-elements`의 `elements()` 블록 안에서 일반 Streamlit 컴포넌트를 사용할 수 없음

- `elements()` 컨텍스트 = React 기반 렌더링
- `st.pyplot()`, `st.plotly_chart()`, `st.dataframe()` = Streamlit 네이티브 렌더링
- **두 시스템은 혼합 불가능**

> 이 레포는 해당 방향으로 도전한 **실험/연구용 프로토타입 기록**입니다.
> 

## 🚀 실행 방법

### (1) 디렉토리 이동

```bash
cd app
```

### (2) 패키지 설치

```bash
pip install -r requirements.txt
```

또는 conda 사용 시:

```bash
conda install matplotlib seaborn -y
```

- `-y` 옵션은 모든 설치 질문에 자동으로 yes 응답

### (3) 실행 (중요)

```bash
streamlit run game_d_[commented.py](http://commented.py)
```

> ⚠️ `python game_d_[commented.py](http://commented.py)`로 실행하면 경고 또는 오작동이 발생할 수 있습니다.
> 

## 🛠️ 기술 스택

- **Framework:** Streamlit
- **ML Models:** scikit-learn (RandomForest), XGBoost
- **Explainability:** SHAP
- **Visualization:** Matplotlib, Plotly, Seaborn
- **UI Components:** streamlit-elements (실험적)

## 📋 주요 기능

### Panel 1 - 전체 게임 인사이트

- SHAP Summary Plot으로 전체 특성 중요도 파악
- 승/패 비율 및 게임 통계

### Panel 2 - 플레이어 선택

- 개별 플레이어 선택 및 정보 확인
- 승/패 예측 및 확률 표시

### Panel 3 - SHAP 분석

- 선택한 플레이어의 승/패 원인 분석
- 특성별 기여도 시각화

### Panel 4 - 게임 지표 시각화

- Deaths vs Win
- Play Time vs Win
- Items vs Damage Dealt 상관관계

## 🐛 디버깅 & 실행 메모

### ModuleNotFoundError 대응

- 패키지가 설치된 줄 알았어도 **현재 실행 중인 conda 환경**에 설치되지 않았을 수 있음
- 환경이 다르면 패키지가 인식되지 않음

### Streamlit 리로드

- 최초 1회 `streamlit run` 실행 후 서버 유지
- 코드 수정 후 저장 시 자동 리로드
- 반영이 애매하면 브라우저 새로고침(F5)

### 실행 팁

- Streamlit은 파일이 있는 폴더에서 실행하는 것이 가장 안정적

## 🎯 다음 목표 (재도전 시)

- [ ]  Drag handle / layout 저장 로직 완성
- [ ]  streamlit-elements 구조 이해도 강화
- [ ]  진짜 드래그 UX 완성판 구현
- [ ]  또는 Dash/Panel로 프레임워크 전환 검토

## 💡 배운 점

- Streamlit은 빠른 프로토타입에 최적화되어 있음    (간단하게 빠르게 만든다.)
- 복잡한 커스텀 UI는 한계가 있음  (혼합 하는 것이 쉬운게 아니란 것을 깨달음. 충돌 등)
- `streamlit-elements`는 완전한 React 환경이 필요 (학습 필요)
- 프레임워크 선택은 요구사항에 따라 신중하게 결정해야 함

## 📂 프로젝트 구조

```
.
├── app/
│   ├── game_d_[commented.py](http://commented.py)    # 메인 애플리케이션
│   └── requirements.txt        # 의존성 패키지
├── images.png                  # 스크린샷 1
├── images2.png                 # 스크린샷 2
└── [README.md](http://README.md)                   # 이 파일
```



## 👤 Author

** junsu **

---

📌 **Prototype 기록용 레포입니다. 추후 완성 본 으로 업데이트 예정.**
