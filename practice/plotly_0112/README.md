# Plotly Scatter & Hover Customization Practice

수업시간 학습한 Plotly를 사용해 iris 데이터셋으로 산점도를 생성하고,
trace 추가, axis 조작, trace 업데이트를 실습한 코드입니다.

수업에서 다루지 않은 기능으로 `hovertemplate`을 사용해  
마우스를 올렸을 때 출력되는 tooltip 내용을 직접 커스터마이징했습니다.

---

## 실습 내용

### 1. 기본 산점도 생성
- `px.scatter`를 사용해 iris 데이터 산점도 생성
- `color="species"` 옵션으로 종별 색상 구분

### 2. Trace 추가
- `add_trace()`를 사용해 종별 평균값 위치를 표시하는 trace 추가

### 3. Axis 조작
- 축 범위 직접 지정 (`range`)
- 자동 범위로 복귀 (`autorange`)
- y축 뒤집기, x축 줌 고정

### 4. Trace 업데이트
- `update_traces()`로 모든 scatter 스타일 일괄 수정
- selector를 사용해 평균값 trace만 강조 표시

### 5. Hover 커스터마이징 (수업 외 기능)
- `hovertemplate`을 사용해 hover 출력 문장과 구조를 직접 정의
-
---

## 실행 파일
- `plotly_task_0112_basic_trace.py`

---

## 느낀 점
코드로 눈에 보이는 변화를 직접 만들어낸다는 점이 신기하고 재밌었습니다.  
투명도, 색상, 두께 같은 수치를 조금씩 바꾸는 것만으로도  
그래프의 인상이 달라지는 것을 체감할 수 있었습니다.

또한 Plotly에서 hovertemplate을 사용하면서  
HTML 태그(`<br>` 등)와 함께 코드를 작성할 수 있다는 점이 인상 깊었습니다.  
단순히 값이 자동으로 출력되는 게 아니라,
마우스를 올렸을 때 어떤 문장이 어떤 순서로 보일지까지
내가 직접 정할 수 있다는 점이 인상적이었습니다.

