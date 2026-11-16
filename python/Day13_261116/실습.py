# 실습 1.

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

기본요금 = 4800
km당요금 = 1000
거리 = st.number_input("거리를 입력하세요 (1~7): ", value=1, min_value= 0)

새_요금표 = 거리 * km당요금 + 기본요금

# 생각해보기 
# 1. km당 요금 기울기 , 기본요금 절편
# 2. 거리가 0이면 절편값 4800 그대로 있으므로


#------------------------------------------------------------------------------

# 실습 2.

st.title("컴퓨터 요금표 찾기")

영수증 = pd.DataFrame({
    "개수" : [1,2,3],
    "총액" : [13000,22000,31000]
})

X = 영수증[["개수"]]
y = 영수증["총액"]

model = LinearRegression()
model.fit(X,y)

st.write("메뉴 1개당 가격(기울기): ", model.coef_[0])
st.write("배달비 (절편): ", model.intercept_)

개수 = st.number_input("예측 총액: ", value=5, min_value = 1)

예측_총액 = model.predict(pd.DataFrame({
    "개수" : [개수]
}))[0]

st.metric(f"예측 총액: ({개수}개) : ({예측_총액:.0f}원)")

#------------------------------------------------------------------------------

# 실습 3.

영수증1= pd.DataFrame({
    "무게": [1,2,3,4],
    "요금": [4000,5000,6000,7000]
})

X = 영수증[["무게"]]
y = 영수증["요금"]

model = LinearRegression()
model.fit(X,y)

st.write("1kg당 요금(기울기): ", model.coef_[0])
st.write("기분 운임(절편): ", model.intercept_)

예측 = model.predict(pd.DataFrame({"무게" : [10]}))[0]
st.write(f"10kg 예측: {예측:.0f}원")

#------------------------------------------------------------------------------

# 실습 4.

영수증3 = pd.DataFrame({
    "곡 수" : [1,2,3],
    "요금" : [500,1000,1500]
})

X = 영수증3[["곡 수"]]
y = 영수증3["요금"]

model = LinearRegression()
model.fit(X,y)

st.write(f"1곡당 요금(기울기):  {model.coef_[0]}, 기본값 (절편): {model.intercept_}")
예측 = model.predict(pd.DataFrame({"예측": [8]}))[0]
st.write(f"8곡 예측 : {예측:.0f}원")

#------------------------------------------------------------------------------

# 실습 5.

배달 = pd.DataFrame({
    "개수" : [1,2,3,2,1],
    "거리" : [1,2,1,3,2],
    "총액" : [14500, 27000, 38500, 27500, 15000]
})

X = 배달[["개수"],["거리"]]
y = 배달["총액"]

st.write(f"X 크기: {X.shape}")

model = LinearRegression()
model.fit(X,y)

st.write(f"기울기 개수:  {round(model.coef_[0])}, 거리: {round(model.coef_[1])}")              # round 이용하기
st.write(f"절편: {model.intercept_}" )

예측 = model.predict(pd.DataFrame({"개수:"[4],"예측:"[4]}))[0]
st.write(f"4개, 4km 예측: {예측:.0f}")

# --------------------------------------------------------------------------------

# 실습. 6

st.title("이 예측을 믿어도 될까?")

표 = pd.DataFrame({
    "공부시간" : [1,2,3,4,5],
    "점수": [52,58,71,78,88]
})

X = 표[["공부시간"]]
y = 표["점수"]
model = LinearRegression()
model.fit(X,y)

st.write(f"기울기: {model.coef_[0]:1f}, 절편: {model.intercept_ :.1f}")

for 시간 in [3, 6 ,10]:
    에측 = model.predict(pd.DataFrame({"시간" : [시간]}))[0]
    st.write(f"{시간}시간 예측, 예측:{예측:.1f}점")