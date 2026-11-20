# game.py
import pandas as pd
import streamlit as st
import time     # 시간과 관련되어있는 도구

# streamlit 10초 세기 그거에 평균 구하는 것!
# 실행 순서 어떻게 될지?
# 시작 버튼을 누른다 -> 목표에 맞춰 횟수번 시도를 한다 -> 

# X = 내가 알고 있는 것
# y = 알고 싶은 것

목표 = 10   # 맞출 시간
횟수 = 5    # 한 라운드에 시도하는 횟수!

st.title("눈 감고 10초 맞추기")
st.caption(f"시작을 누르고, **{목표}초**가 지났다고 느끼면 멈춤을 누르세요. 화면에 시계는 없어요!")

# 연습: 10초가 어떤 느낌인지 눈으로 먼저 보기 (게임에서는 시계가 안 보여요)
if st.button("연습: 10초가 어떤 느낌인지 보기"):
    자리 = st.empty()
    for 초 in range(1, 목표 + 1):
        자리.metric("지금", f"{초}초")
        time.sleep(1)
    자리.success("끝! 이제 시계는 숨기고, 감으로 맞춰 보세요.")

# 기록 저장
if "기록" not in st.session_state:
    st.session_state["기록"] = {"1라운드": [], "2라운드": []}
    st.session_state["시작시각"] = None
    st.session_state["방금"] = ""

라운드 = st.radio("라운드 선택", ["1라운드", "2라운드"], horizontal=True)
if 라운드 == "1라운드":
    st.caption("1라운드: 얼마나 틀렸는지 **알려 주지 않아요**. 5번이 끝나면 한꺼번에 보여 줘요.")
else:
    st.caption("2라운드: 멈출 때마다 **얼마나 틀렸는지 바로 알려 줘요**.")

기록 = st.session_state["기록"][라운드]
st.write(f"**{라운드}: {len(기록)} / {횟수}번 완료**")


칸1, 칸2, 칸3 = st.columns(3)

if 칸1.button("시작"):
    st.session_state["시작시각"] = time.time()
    st.session_state["방금"] = ""

if 칸2.button("멈춤"):
    if st.session_state["시작시각"] is None:
        st.session_state["방금"] = "먼저 시작을 눌러 주세요."
    elif len(기록) >= 횟수:
        st.session_state["방금"] = f"{라운드}는 이미 {횟수}번을 했어요. 다시 하려면 '이 라운드 다시'를 눌러요."
        st.session_state["시작시각"] = None
    else:
        걸린시간 = round(time.time() - st.session_state["시작시각"], 2)
        기록.append(걸린시간)
        st.session_state["시작시각"] = None
        차이 = round(걸린시간 - 목표, 2)
        if 라운드 == "1라운드":
            st.session_state["방금"] = "기록했어요! 결과는 5번이 끝나면 보여 줄게요."
        elif 차이 > 0:
            st.session_state["방금"] = f"{차이}초 늦었어요 (내가 잰 시간 {걸린시간}초)"
        elif 차이 < 0:
            st.session_state["방금"] = f"{-차이}초 빨랐어요 (내가 잰 시간 {걸린시간}초)"
        else:
            st.session_state["방금"] = "딱 맞았어요!"

if 칸3.button("이 라운드 다시"):
    st.session_state["기록"][라운드] = []
    st.session_state["시작시각"] = None
    st.session_state["방금"] = ""
    기록 = []

if st.session_state["시작시각"] is not None:
    st.warning(f"재는 중... {목표}초라고 느껴지면 멈춤을 누르세요.")
if st.session_state["방금"]:
    st.info(st.session_state["방금"])


# 결과 확인

if len(기록) == 횟수:
    st.divider()
    st.subheader(f"{라운드} 결과")

    틀림 = [round(abs(x - 목표), 2) for x in 기록]
    표 = pd.DataFrame(
        {"내가 잰 시간(초)": 기록, "틀린 크기(초)": 틀림},
        index=range(1, 횟수 + 1),
    )
    표.index.name = "시도"
    st.dataframe(표)
    st.bar_chart(표["틀린 크기(초)"])

    st.markdown("**평균 오차 계산 (3칸)**")
    합 = round(sum(틀림), 2)
    mae = round(합 / 횟수, 2)
    st.write(f"1. 틀린 크기를 모두 **더하기**: {' + '.join(str(t) for t in 틀림)} = **{합}초**")
    st.write(f"2. 횟수로 **나누기**: {합} ÷ {횟수} = **{mae}초**")
    st.metric("평균 오차", f"{mae}초")
    st.success(f"**평균 {mae}초 틀렸어요.** 이 숫자의 이름이 **MAE**(평균 절대 오차)예요.")
    st.info(
        f"**결론**: 사람이 감으로 {목표}초를 맞히면 평균 {mae}초 틀려요. "
        "AI의 예측도 똑같이 **'평균 얼마나 틀리는지'**를 MAE로 재서, "
        "고칠지, 비교할지, 서비스에 쓸지를 정해요."
    )

# 5번 반복하면서 평균을 내는 과정 (MAE)
# 고치기, 비교하기, 목표확인
# 모델 선택 -> 학습 -> 예측 -> 채점(MAE)
# 실제 서비스(앱) -> 서비스 활용됨

