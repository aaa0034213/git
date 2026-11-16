# fitTest.py

# 틀린 정도 (예측과 실제값의 차이)
# 오차 (error / loss)
# machine learning 은 오차가 가장 작아지는 기울기와 절편을 찾는 일.
# fit() 

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# 머신러닝 도구 모델을 가져오는 import

st.title("컴퓨터가 직접 요금을 찾는다")

영수증 = pd.DataFrame({
    "개수" : [1,2,3],
    "총액" : [15000,27000,39000],
})

# 2. X = 문제 (표 모양, 대괄호가 두 겹) 
#    Y = 정답 (한 줄, 대괄호가 한 겹)

X = 영수증[["개수"]]
Y = 영수증["총액"]

st.write(X)
st.write(Y)

# 3. 모델 가져오기
model = LinearRegression()

# 4. 학습 시키기
model.fit(X, Y)


# 5. 컴퓨터가 찾은 두 숫자
st.write("메뉴 1개당 가격(기울기): ", model.coef_[0])
st.write("배달비(절편): ", model.intercept_)

# 6. 개수 입력

개수 = st.number_input("몇 개 시킬까요?", value = 5, min_value= 1)

# 7. 예측
# 학습때와 똑같은 표 모양, 같은 열 이름으로 만든다.

예측 = model.predict(pd.DataFrame({
    "개수" : [개수] 
}))[0]

st.metric("예측: ", f"{예측:,.0f}원") 

