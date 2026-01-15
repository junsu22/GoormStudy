# 데이터 시각화 9회차 – Streamlit 정리 노트

## 1. Streamlit이란?
- Python 기반 웹 앱 프레임워크
- 웹 개발 지식 없이 데이터 앱 제작 가능
- 데이터 시각화, AI/모델 데모, 베타 테스트용 UI에 활용

## 2. 개발 환경 설정
### Conda 환경
- 프로젝트별 독립 환경 구성
- 팀원과 Python 버전 통일 목적
```bash
conda create -n stenv python=3.9
conda activate stenv
```

### Streamlit 설치
```bash
pip install streamlit
```

### 데모 앱 실행
```bash
streamlit hello
```

## 3. 첫 번째 Streamlit 앱
```python
import streamlit as st
st.write("Hello, world!")
```

```bash
streamlit run app.py
```

## 4. 기본 UI 요소
### 버튼
```python
if st.button("say hello"):
    st.write("hey hello there")
else:
    st.write("goodbye")
```

### st.write()
- 텍스트, Markdown, 숫자, DataFrame, Plotly 그래프 출력 가능

## 5. 입력 위젯
### Slider
```python
age = st.slider("나이", 0, 100)
```

### Selectbox
```python
option = st.selectbox("가장 좋아하는 색은?", ("빨강", "파랑", "초록"))
st.write(option)
```

### Multiselect
```python
options = st.multiselect("선택", ["빨강", "파랑", "초록", "노랑"])
```

### Checkbox
```python
if st.checkbox("커피"):
    st.write("☕ 선택됨")
```

## 6. 시각화
- 기본: st.line_chart
- 권장: Plotly

## 7. 레이아웃
### 컬럼
```python
col1, col2, col3 = st.columns(3)
with col1:
    st.write("왼쪽")
```

### Expander
```python
with st.expander("자세히 보기"):
    st.write("내용")
```

## 8. 고급 기능
- st.progress
- st.form
- st.experimental_get_query_params

## 9. 배포
- GitHub 레포 생성 후 Streamlit Community Cloud로 배포
- git push 시 자동 업데이트

---
정리: Streamlit은 데이터·AI 결과를 빠르게 보여주기 위한 데모 도구
