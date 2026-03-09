import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

import plotly.express as px
import plotly.graph_objects as go

from streamlit_elements import elements, dashboard, mui


# ==========================================
# 페이지 기본 설정
# ==========================================
st.set_page_config(page_title="게임 승/패 예측 대시보드", layout="wide")

# 한글 폰트 설정 (Windows)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

st.title("🎮 게임 승/패 예측 대시보드")
st.markdown("---")


# ==========================================
# 1. 샘플 데이터 생성
# ==========================================
@st.cache_data
def generate_sample_data(n_samples=200):
    np.random.seed(42)
    data = []

    for i in range(n_samples):
        win = np.random.choice([0, 1], p=[0.45, 0.55])

        if win == 1:
            play_time = np.random.normal(35, 8)
            level = np.random.normal(25, 5)
            deaths = np.random.normal(3, 2)
            items = np.random.normal(15, 3)
            damage_dealt = np.random.normal(8000, 1500)
        else:
            play_time = np.random.normal(25, 7)
            level = np.random.normal(18, 5)
            deaths = np.random.normal(8, 3)
            items = np.random.normal(8, 3)
            damage_dealt = np.random.normal(5000, 1200)

        data.append(
            {
                "player_id": f"P{i+1:03d}",
                "play_time": max(10, float(play_time)),
                "level": max(1, int(level)),
                "deaths": max(0, int(deaths)),
                "items": max(0, int(items)),
                "damage_dealt": max(1000, float(damage_dealt)),
                "win": int(win),
            }
        )

    return pd.DataFrame(data)


df = generate_sample_data(200)


# ==========================================
# 2. 모델 학습
# ==========================================
@st.cache_resource
def train_models(df):
    X = df[["play_time", "level", "deaths", "items", "damage_dealt"]]
    y = df["win"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        min_samples_split=5,
    )
    rf_model.fit(X_train, y_train)
    rf_score = rf_model.score(X_test, y_test)

    xgb_model = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss",
    )
    xgb_model.fit(X_train, y_train)
    xgb_score = xgb_model.score(X_test, y_test)

    if xgb_score >= rf_score:
        best_model = xgb_model
        best_model_name = "XGBoost"
        best_score = xgb_score
    else:
        best_model = rf_model
        best_model_name = "RandomForest"
        best_score = rf_score

    return best_model, best_model_name, best_score, X, rf_score, xgb_score


model, model_name, model_score, X, rf_score, xgb_score = train_models(df)


# ==========================================
# 3. SHAP 값 계산
# ==========================================
@st.cache_resource
def compute_shap_values(_model, X):
    explainer = shap.TreeExplainer(_model)
    shap_values = explainer(X)  # 신버전 (Explanation)
    return explainer, shap_values


explainer, shap_values = compute_shap_values(model, X)


# ==========================================
# 세션 상태: 선택 플레이어 / 레이아웃
# ==========================================
if "selected_player_id" not in st.session_state:
    st.session_state.selected_player_id = df["player_id"].iloc[0]

if "layout" not in st.session_state:
    st.session_state.layout = [
        dashboard.Item("Panel 1", 0, 0, 6, 5),
        dashboard.Item("Panel 2", 6, 0, 6, 5),
        dashboard.Item("Panel 3", 0, 5, 6, 5),
        dashboard.Item("Panel 4", 6, 5, 6, 5),
    ]


def handle_layout_change(new_layout):
    st.session_state.layout = new_layout


# ==========================================
# 사이드바 - 설정
# ==========================================
with st.sidebar:
    st.header("⚙️ 설정")

    st.markdown(f"**사용 모델**: {model_name}")
    st.markdown(f"**모델 정확도**: {model_score:.2%}")
    st.markdown(f"- RandomForest: {rf_score:.2%}")
    st.markdown(f"- XGBoost: {xgb_score:.2%}")
    st.markdown("---")

    st.subheader("👁️ 패널 표시 설정")
    show_panels = {}
    for panel in ["Panel 1", "Panel 2", "Panel 3", "Panel 4"]:
        show_panels[panel] = st.checkbox(panel, value=True, key=f"show_{panel}")

    st.markdown("---")

    if st.button("🔄 레이아웃 초기화"):
        st.session_state.layout = [
            dashboard.Item("Panel 1", 0, 0, 6, 5),
            dashboard.Item("Panel 2", 6, 0, 6, 5),
            dashboard.Item("Panel 3", 0, 5, 6, 5),
            dashboard.Item("Panel 4", 6, 5, 6, 5),
        ]
        st.rerun()

    st.info("💡 Tip: 카드 상단(헤더)을 잡고 드래그해봐 🙂")


# ==========================================
# Panel 1 – 전체 게임 인사이트
# ==========================================
def render_panel1():
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🎯 SHAP Summary Plot - 승패에 가장 큰 요인은?")
        st.caption("특성별 중요도: 각 변수가 승/패 예측에 미치는 영향")

        fig, ax = plt.subplots(figsize=(10, 6))
        shap.summary_plot(shap_values, X, show=False)
        st.pyplot(fig)
        plt.close(fig)

        # 중요도 계산: (samples, features) 형태로 맞추기
        shap_importance = np.abs(shap_values.values).mean(axis=0)

        while shap_importance.ndim > 1:
            shap_importance = shap_importance.mean(axis=-1)

        shap_importance = np.ravel(shap_importance)

        if len(shap_importance) != len(X.columns):
            st.warning(f"SHAP 길이 불일치: {len(shap_importance)} vs {len(X.columns)}")
            shap_importance = shap_importance[: len(X.columns)]

        feature_importance = (
            pd.DataFrame({"feature": X.columns, "importance": shap_importance})
            .sort_values("importance", ascending=False)
            .reset_index(drop=True)
        )

        top_feature = feature_importance.loc[0, "feature"]
        st.success(f"✅ **{top_feature}** 이(가) 승패에 가장 큰 영향을 미칩니다!")

        st.dataframe(feature_importance, use_container_width=True)

    with col2:
        st.subheader("🏆 승/패 비율")

        win_counts = df["win"].value_counts()
        win_rate = win_counts.get(1, 0) / len(df) * 100

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=["승리", "패배"],
                    values=[win_counts.get(1, 0), win_counts.get(0, 0)],
                    hole=0.4,
                )
            ]
        )
        fig.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig, use_container_width=True)

        st.metric("승률", f"{win_rate:.1f}%")
        st.metric("총 게임 수", len(df))


# ==========================================
# Panel 2 – 플레이어 선택
# ==========================================
def render_panel2():
    col1, col2 = st.columns(2)

    with col1:
        selected_player_id = st.selectbox(
            "플레이어 ID 선택",
            options=df["player_id"].tolist(),
            index=df["player_id"].tolist().index(st.session_state.selected_player_id),
        )
        st.session_state.selected_player_id = selected_player_id

        player_data = df[df["player_id"] == selected_player_id].iloc[0]

        st.markdown("### 📋 플레이어 정보")
        st.write(f"**플레이 시간**: {player_data['play_time']:.1f}분")
        st.write(f"**레벨**: {player_data['level']}")
        st.write(f"**사망 횟수**: {player_data['deaths']}")
        st.write(f"**획득 아이템**: {player_data['items']}")
        st.write(f"**딜량**: {player_data['damage_dealt']:.0f}")

    with col2:
        player_data = df[df["player_id"] == st.session_state.selected_player_id].iloc[0]
        player_features = (
            player_data[["play_time", "level", "deaths", "items", "damage_dealt"]]
            .to_frame()
            .T
        )

        prediction = model.predict(player_features)[0]
        proba = model.predict_proba(player_features)[0]

        st.markdown("### 🎲 예측 결과")
        if prediction == 1:
            st.success("### ✅ 승리 예측")
            st.metric("승리 확률", f"{proba[1]:.1%}")
        else:
            st.error("### ❌ 패배 예측")
            st.metric("패배 확률", f"{proba[0]:.1%}")

        actual = "승리" if int(player_data["win"]) == 1 else "패배"
        st.info(f"**실제 결과**: {actual}")


# ==========================================
# Panel 3 – 선택한 플레이어 SHAP 분석
# ==========================================
def render_panel3():
    selected_player_id = st.session_state.selected_player_id
    player_idx = df[df["player_id"] == selected_player_id].index[0]

    st.subheader("🔍 선택한 플레이어 SHAP 분석")
    st.markdown(
        f"### {selected_player_id} 가 **{'승리' if df.loc[player_idx,'win']==1 else '패배'}** 한 이유"
    )

    # 플레이어 SHAP 값 추출
    player_shap_values = shap_values[player_idx].values

    if player_shap_values.ndim > 1:
        # (features, 2) 라면 클래스1(승리) 기준으로
        if player_shap_values.shape[-1] == 2:
            player_shap_values = player_shap_values[:, 1]
        else:
            player_shap_values = player_shap_values.flatten()[: len(X.columns)]

    player_shap_values = np.ravel(player_shap_values)

    contribution_df = (
        pd.DataFrame(
            {
                "특성": X.columns,
                "실제 값": X.iloc[player_idx].values,
                "SHAP 값": player_shap_values,
            }
        )
        .assign(abs_shap=lambda d: np.abs(d["SHAP 값"]))
        .sort_values("abs_shap", ascending=False)
        .drop(columns=["abs_shap"])
        .reset_index(drop=True)
    )

    # Bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["green" if v > 0 else "red" for v in contribution_df["SHAP 값"]]
    ax.barh(
        contribution_df["특성"], contribution_df["SHAP 값"], color=colors, alpha=0.75
    )
    ax.axvline(0, color="black", linestyle="--", linewidth=0.8)
    ax.set_xlabel("SHAP 값 (양수=승리 기여, 음수=패배 기여)")
    ax.set_title("특성별 예측 기여도")
    ax.grid(axis="x", alpha=0.3)
    ax.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.dataframe(contribution_df, use_container_width=True)

    top_pos = contribution_df[contribution_df["SHAP 값"] > 0].head(2)
    top_neg = contribution_df[contribution_df["SHAP 값"] < 0].head(2)

    if not top_pos.empty:
        st.success(f"✅ 승리에 기여: {', '.join(top_pos['특성'].tolist())}")
    if not top_neg.empty:
        st.error(f"❌ 패배에 기여: {', '.join(top_neg['특성'].tolist())}")


# ==========================================
# Panel 4 – 게임 지표 시각화
# ==========================================
def render_panel4():
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💀 Deaths vs Win")
        fig1 = px.box(
            df,
            x="win",
            y="deaths",
            labels={"win": "승/패 (0=패배, 1=승리)", "deaths": "사망 횟수"},
            color="win",
        )
        fig1.update_layout(showlegend=False, height=360)
        st.plotly_chart(fig1, use_container_width=True)

        st.caption(
            f"승리 평균 사망: {df[df['win']==1]['deaths'].mean():.1f}회 | "
            f"패배 평균 사망: {df[df['win']==0]['deaths'].mean():.1f}회"
        )

    with col2:
        st.subheader("⏱️ Play Time vs Win")
        fig2 = px.box(
            df,
            x="win",
            y="play_time",
            labels={"win": "승/패 (0=패배, 1=승리)", "play_time": "플레이 시간 (분)"},
            color="win",
        )
        fig2.update_layout(showlegend=False, height=360)
        st.plotly_chart(fig2, use_container_width=True)

        st.caption(
            f"승리 평균 시간: {df[df['win']==1]['play_time'].mean():.1f}분 | "
            f"패배 평균 시간: {df[df['win']==0]['play_time'].mean():.1f}분"
        )

    st.subheader("🎯 Items vs Damage Dealt")
    fig3 = px.scatter(
        df,
        x="items",
        y="damage_dealt",
        color="win",
        labels={"items": "획득 아이템 수", "damage_dealt": "딜량", "win": "승/패"},
        opacity=0.6,
    )
    st.plotly_chart(fig3, use_container_width=True)


# ==========================================
# ✅ 드래그 가능한 대시보드 렌더링 (Panel 1~4 전부 Grid 안!)
# ==========================================
with elements("draggable_dashboard"):
    with dashboard.Grid(
        st.session_state.layout,
        onLayoutChange=handle_layout_change,
        cols=12,
        rowHeight=60,
    ):
        # Panel 1
        if show_panels.get("Panel 1", True):
            with mui.Card(key="Panel 1", sx={"borderRadius": 2, "height": "100%"}):
                mui.CardHeader(
                    title="📊 Panel 1 – 전체 게임 인사이트",
                    sx={"cursor": "grab", "borderBottom": "1px solid #e0e0e0"},
                )
                with mui.CardContent():
                    render_panel1()

        # Panel 2
        if show_panels.get("Panel 2", True):
            with mui.Card(key="Panel 2", sx={"borderRadius": 2, "height": "100%"}):
                mui.CardHeader(
                    title="👤 Panel 2 – 플레이어 선택",
                    sx={"cursor": "grab", "borderBottom": "1px solid #e0e0e0"},
                )
                with mui.CardContent():
                    render_panel2()

        # Panel 3
        if show_panels.get("Panel 3", True):
            with mui.Card(key="Panel 3", sx={"borderRadius": 2, "height": "100%"}):
                mui.CardHeader(
                    title="🔍 Panel 3 – 선택한 플레이어 SHAP 분석",
                    sx={"cursor": "grab", "borderBottom": "1px solid #e0e0e0"},
                )
                with mui.CardContent():
                    render_panel3()

        # Panel 4
        if show_panels.get("Panel 4", True):
            with mui.Card(key="Panel 4", sx={"borderRadius": 2, "height": "100%"}):
                mui.CardHeader(
                    title="📈 Panel 4 – 게임 지표 시각화",
                    sx={"cursor": "grab", "borderBottom": "1px solid #e0e0e0"},
                )
                with mui.CardContent():
                    render_panel4()


# ==========================================
# 푸터
# ==========================================
st.markdown("---")
st.markdown("### 💡 사용 가이드")
st.markdown(
    """
- **Panel 1**: 전체 게임에서 승/패에 영향을 미치는 주요 요인을 확인  
- **Panel 2**: 특정 플레이어를 선택하고 승/패 예측 결과 확인  
- **Panel 3**: 선택한 플레이어의 승/패 원인을 SHAP으로 상세 분석  
- **Panel 4**: 게임 지표 간의 관계를 시각화하여 패턴 발견  
- **드래그**: 카드 상단(헤더)을 마우스로 끌어서 레이아웃을 바꿀 수 있음 
"""
)
