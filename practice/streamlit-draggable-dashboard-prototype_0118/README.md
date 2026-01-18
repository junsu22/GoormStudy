# Streamlit + SHAP 드래거블 대시보드 (Prototype)

> **목표:** Streamlit에서 SHAP 기반 모델 해석 대시보드를 만들고,  
> **패널을 Drag & Drop 으로 재배치 가능한 UI**까지 도전하는 프로토타입 프로젝트.

현재는 **프로토타입 단계(미완성)**로 남기고,  
추후 실력과 이해도가 더 쌓이면 **진짜 드래그 UX 완성 버전으로 재도전**할 예정입니다.

---

## 1) 구현된 것 (현재 상태)

- 게임 플레이 로그 샘플 데이터 생성
- RandomForest / XGBoost 학습 후 성능 비교 및 모델 선택
- SHAP 기반
  - 전체 중요도(Summary plot)
  - 선택 플레이어 단일 분석(기여도)
- Plotly 기반 EDA 시각화
- Streamlit UI 구성 (Panel 1 ~ Panel 4)

---

## 2) 왜 “미완성”으로 남기나?

### 드래거블의 정의
- **진짜 드래거블 대시보드**는 마우스로 **끌어서(Drag & Drop)** 패널 위치를 바꿀 수 있어야 함
- ⬆️⬇️ 버튼으로 순서만 바꾸는 방식은 **재배치**이지, 드래그는 아님

### Streamlit 기본 한계
- Streamlit 기본 컴포넌트만으로는 진짜 Drag & Drop 구현이 어려움
- `streamlit-elements` 같은 외부 컴포넌트를 활용하는 방식이 현실적

> 이 레포는 해당 방향으로 도전한 **실험/연구용 프로토타입 기록**입니다.

---

## 3) 실행 방법

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
streamlit run game_d_commented.py
```

> `python game_d_commented.py`로 실행하면 경고 또는 오작동이 발생할 수 있습니다.

---

## 4) 디버깅 & 실행 메모

### ModuleNotFoundError 대응
- 패키지가 설치된 줄 알았어도 **현재 실행 중인 conda 환경**에 설치되지 않았을 수 있음
- 환경이 다르면 패키지가 인식되지 않음

### Streamlit 리로드
- 최초 1회 `streamlit run` 실행 후 서버 유지
- 코드 수정 후 저장 시 자동 리로드
- 반영이 애매하면 브라우저 새로고침(F5)

### 실행 팁
- Streamlit은 파일이 있는 폴더에서 실행하는 것이 가장 안정적

---

## 5) 다음 목표 (재도전 시)

- Drag handle / layout 저장 로직 완성
- streamlit-elements 구조 이해도 강화
- 진짜 드래그 UX 완성판 구현

---

📌 *Prototype 기록용 레포입니다. 추후 완성판으로 업데이트 예정.*
