# maeTest.py
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
# 1. 모델 선택
# model = LinearRegression()

# 2. 학습
# model.fit(X,y) (내가 알고 있는 것, 내가 알고 싶은 것!)

# 3. 예측
# model.predict(새로 알고 싶은 것)

# 4. 테스트 (얼마나 틀렸는지 알기 위해서)
# mean_absolute_error(실제, 예측)

# 틀린 크기를 +로 맞춰서 평균을 낸 것!

# 게임 들어갈 때 예상 대기 시간
st.title("게임 매칭 대기 시간")

st.info(
    "평균 두 번 써요!\n"
    "1 예상시간을 만들 때: 과거 기록의 평균\n"
    "2 잘 맞는지 점검 할 때: 평균(오차(MAE))"
)

st.caption(
    "연습용이라 예상을 만든 기록으로 그대로 점검했어요"
    "진짜 서비스는 **새 기록**으로 점검해요 (다음 시간; 훈련/테스트 분할)"
)

st.subheader("게임 매칭 앱")
st.write("매칭 버튼을 누르면 예상 대기 시간이 20초가 뜬다.")
st.markdown("**1단계. 지난 기록** (매칭을 12번 돌렸을 때 기다린 시간, 초)")
기록2 = {
        "저녁": [15, 20, 18, 23],
        "낮": [30, 40, 35, 45],
        "새벽": [90, 110, 100, 120],
}
st.write(기록2)

# 시간대별 평균 = 예상
st.markdown("**2단계 앱이 예쌍을 만드는 방법: 시간대별 평균**")

평균 = {}

for 이름, 값들 in 기록2.items():
    평균[이름] = sum(값들) / len(값들)

st.write(평균)

선택 = st.selectbox("지금 시간대를 골라보세요", ["저녁","낮","새벽"])
예상 = 평균[선택]
st.metric(f"{선택} 시간대 예상 대기", f"{예상:.1f}초")

# 채점 (MAE)
st.markdown("**3단계. 잘 맞는지 점검 (MAE)**")
표 = []
틀린크기들 = []
전체 = []
for 이름, 값들 in 기록2.items():
    for 값 in 값들:
        틀림 = abs(값 - 평균[이름])
        표.append({"시간대": 이름, "실제(초)": 값, "예상(초)": 평균[이름], "틀린 크기(초)": 틀림})
        틀린크기들.append(틀림)
        전체.append(값)
st.table(표)

mae = sum(틀린크기들) / len(틀린크기들)
전체평균 = sum(전체) / len(전체)
기준선 = sum(abs(값 - 전체평균) for 값 in 전체) / len(전체)
허용 = st.slider("앱이 허용할 수 있는 평균 오차 (초)", 1, 30, 10)

칸1, 칸2, 칸3 = st.columns(3)
칸1.metric("시간대 평균의 MAE", f"{mae:.1f}초")
칸2.metric("전체 평균으로 찍기 MAE", f"{기준선:.1f}초")
칸3.metric("허용 오차", f"{허용}초")


st.markdown("**앱 화면에 이렇게 보여 줄 수 있어요**")
st.info(f"{선택} 시간대: 예상 대기 약 {예상:.0f}초 (±{mae:.0f}초)")

if mae <= 허용 and mae < 기준선:
    st.success("사용 OK: 허용 오차 이하이고, 시간대를 나누지 않은 평균보다 정확해요.")
else:
    st.error("개선 필요: 오차가 크거나, 시간대를 나눠도 나아지지 않았어요.")

with st.expander("진짜 서비스는 이렇게만 할까요?"):
    st.markdown(
        "- 진짜 서비스는 **지금 대기 중인 사람 수, 실력(티어), 게임 모드** 같은 정보를 더 써서 예측해요. (서비스마다 달라요)\n"
        "- 이 앱은 **가장 단순한 방식(평균)**이에요. 그래도 **점검 방법(MAE)**은 똑같아요.\n"
        "- 새벽에는 대기가 길고 들쭉날쭉해서 **허용 오차를 크게** 잡아야 해요. "
        "**서비스와 상황마다 허용 오차가 달라요.**"
    )

st.divider()
st.markdown("**코드로 평균 예측과 MAE는 이 두 줄이에요**")
st.code(
    '평균 = sum(값들) / len(값들)                     # 예상 = 시간대별 평균\n'
    'mae = sum(틀린크기들) / len(틀린크기들)           # 점검 = 평균 오차(MAE)',
    language="python",)

