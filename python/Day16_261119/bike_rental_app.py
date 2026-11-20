from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

st.title("따릉이 대여 건수 · 머신러닝 실습")

# 1. 실제 날씨를 읽고, 숨은 규칙으로 실습용 정답을 만듭니다.
파일 = Path(__file__).with_name("seoul_bike_weather_2026_h1.csv")
if not 파일.is_file():
    st.error("통합 CSV를 파이썬 파일과 같은 폴더에 넣어 주세요.")
    st.stop()

데이터 = pd.read_csv(파일).sort_values("날짜")

기온 = "평균기온(°C)"
강수량 = "일강수량(mm)"
주말 = "주말 여부"  # 평일 0, 토·일 1
정답 = "실습용 정답(건)"

데이터["기상 관측소 번호"] = 108  # 서울 관측소
데이터["대여 집계 지역"] = 1      # 실습에서 서울시 전체를 나타내는 값

데이터[정답] = (
    70_000
    + 데이터[기온] * 2_500
    - 데이터[강수량] * 500
    - 데이터[주말] * 7_000
).round().astype(int)

# 2. X는 모델에 보여주는 힌트, y는 모델이 맞혀야 하는 정답입니다.
힌트_3개 = [기온, 강수량, 주말]
힌트_5개 = 힌트_3개 + ["기상 관측소 번호", "대여 집계 지역"]

X = 데이터[힌트_5개]
y = 데이터[정답]

st.subheader("입력과 정답 예시 6줄")
st.caption("날씨는 실제 관측값이에요. 정답은 숨은 규칙으로 계산한 실습용 값이에요.")
st.dataframe(데이터[["날짜"] + 힌트_5개 + [정답]].head(6), hide_index=True)

# 3. 앞 80%는 공부용, 뒤 20%는 시험용으로 나눕니다.
나눌_위치 = int(len(데이터) * 0.8)
X_공부 = X.iloc[:나눌_위치]
y_공부 = y.iloc[:나눌_위치]
X_시험 = X.iloc[나눌_위치:]
y_시험 = y.iloc[나눌_위치:]

# 4. 베이스라인은 공부용 정답 평균만 사용합니다.
평균 = round(y_공부.mean())
베이스라인_공부_예측 = [평균] * len(y_공부)
베이스라인_시험_예측 = [평균] * len(y_시험)

# 5. fit()은 힌트와 정답을 보고 배우고, predict()는 힌트로 답을 예측합니다.
모델_3개 = LinearRegression()
모델_3개.fit(X_공부[힌트_3개], y_공부)
공부_예측_3개 = 모델_3개.predict(X_공부[힌트_3개]).round()
시험_예측_3개 = 모델_3개.predict(X_시험[힌트_3개]).round()

모델_5개 = LinearRegression()
모델_5개.fit(X_공부, y_공부)
공부_예측_5개 = 모델_5개.predict(X_공부).round()
시험_예측_5개 = 모델_5개.predict(X_시험).round()

# 6. MAE는 날짜마다 |정답 - 예측|을 구한 뒤 평균을 낸 값입니다.
오차표 = pd.DataFrame({
    "모델": ["베이스라인 (평균)", "힌트 3개", "힌트 5개"],
    "공부용 MAE(건)": [
        mean_absolute_error(y_공부, 베이스라인_공부_예측),
        mean_absolute_error(y_공부, 공부_예측_3개),
        mean_absolute_error(y_공부, 공부_예측_5개),
    ],
    "시험용 MAE(건)": [
        mean_absolute_error(y_시험, 베이스라인_시험_예측),
        mean_absolute_error(y_시험, 시험_예측_3개),
        mean_absolute_error(y_시험, 시험_예측_5개),
    ],
})

st.subheader("공부용·시험용 오차 비교")
st.caption(f"공부용 {len(y_공부)}일 · 시험용 {len(y_시험)}일")
st.dataframe(오차표.round(2), hide_index=True)

st.subheader("시험용 날짜별 예측")
시험표 = 데이터.iloc[나눌_위치:][["날짜", 정답]].copy()
시험표["베이스라인 예측"] = 베이스라인_시험_예측
시험표["힌트 3개 예측"] = 시험_예측_3개.astype(int)
시험표["힌트 5개 예측"] = 시험_예측_5개.astype(int)
st.dataframe(시험표, hide_index=True)

# 7. 입력값을 학습할 때와 같은 열 순서로 한 줄에 담아 예측합니다.
st.subheader("새 날씨로 예측하기")
입력_기온 = st.number_input(기온, min_value=-15.0, max_value=35.0, value=20.0)
입력_강수량 = st.number_input(강수량, min_value=0.0, max_value=80.0)
입력_주말 = st.checkbox("토요일 또는 일요일")

if st.button("예측하기"):
    새_힌트 = [[입력_기온, 입력_강수량, int(입력_주말), 108, 1]]
    새_X = pd.DataFrame(새_힌트, columns=힌트_5개)
    예측값 = round(모델_5개.predict(새_X)[0])
    st.write(f"베이스라인 {평균:,}건 · 힌트 모델 {예측값:,}건")

with st.expander("숨은 규칙 보기"):
    st.write("70,000 + 기온 × 2,500 − 강수량 × 500 − 주말 여부 × 7,000")
    st.write("관측소 번호와 집계 지역은 매일 같은 값이에요.")
