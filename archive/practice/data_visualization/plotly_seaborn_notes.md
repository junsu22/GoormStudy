# Plotly · Seaborn

## 1. Plotly 개요

Plotly는 인터랙티브 시각화를 지원하는 라이브러리이다.

- 마우스 hover를 통한 값 확인
- 확대 / 축소 / 드래그 기능
- 웹 환경 및 대시보드로 확장 가능

> 요약:  
> Plotly는 사용자 상호작용이 가능한 그래프를 생성하는 시각화 도구이다.

---

## 2. Plotly가 필요한 이유

### 라이브러리 특징 비교

| 라이브러리 | 특징 |
|-----------|------|
| matplotlib | 기본적인 정적 시각화 |
| seaborn | 정적 시각화 + 미려한 스타일 |
| plotly | 인터랙티브 시각화 + 웹 환경 활용 |

Plotly는 분석 결과를 보여주고 설명해야 하는 상황에서 사용된다.

---

## 3. Plotly의 두 가지 사용 방식 (가장 중요)

### 1) Plotly Express (`px`)
- 코드가 짧다 (1~2줄)
- 기본 스타일이 적용됨
- 실습 / 과제 / 대부분의 경우 사용

```python
import plotly.express as px
fig = px.scatter(df, x="a", y="b")
fig.show()
```

빠르게 그리고 싶을 때 → `px`

---

### 2) Graph Objects (`go`)
- 세밀한 조정 가능
- 코드 길고 구조가 복잡

```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(...)
fig.update_layout(...)
```

px로 먼저 만들고,  
부족한 부분을 go로 수정한다.

---

## 4. Plotly의 기본 구조 (Figure → Trace → Layout)

Plotly 그래프는 다음과 같은 구조를 가진다.

```
Figure
 ├─ Trace (그래프 요소: 선 하나, 점 하나, 막대 하나 등)
 └─ Layout (제목, 축, 여백, 스타일 설정)
```

자주 사용하는 함수:

- `add_trace()` → 그래프 추가
- `update_traces()` → 그래프 스타일 수정
- `update_layout()` → 전체 레이아웃 수정
- `update_xaxes()`, `update_yaxes()` → 축 설정

---

## 5. 주요 옵션 (참고)

다음 옵션들은 필요할 때 찾아 사용한다.

- width / height
- margin (l, r, t, b)
- font 설정
- tick 간격 / 범위
- log scale / reverse axis

---

## 6. Subplot (여러 그래프 한 화면)

- 하나의 Figure 안에 여러 그래프 배치
- 대시보드 형태의 시각화
- 팀 프로젝트/미션에서 자주 사용

여러 시각화를 한 화면에 구성할 수 있다.

---

## 7. Seaborn 개요 (실습용 데이터셋)

Seaborn은 Plotly와 비교하기 위한 용도가 아니라,  
빠른 시각화 실습을 위한 데이터 제공 목적이다.

```python
import seaborn as sns
sns.load_dataset("tips")
```

주로 사용되는 데이터셋:
- tips (식당 팁 데이터)
- titanic (생존 여부 데이터)
- iris (붓꽃 데이터)
- diamonds (다이아몬드 데이터)
