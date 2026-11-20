# 실습 1.
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Q1. 키가 커질수록 신발 사이즈 커진다

# =============== Step 2. 학습용 / 시험용으로 나누기 ==========================

data = pd.DataFrame({
    "번호": list(range(1, 31)),
    "키": [
        168, 179, 174, 152, 161, 156, 183, 174, 158, 173,
        164, 158, 182, 162, 181, 174, 174, 181, 164, 176,
        184, 154, 185, 164, 170, 178, 155, 177, 157, 177
    ],
    "신발": [
        260, 280, 260, 230, 240, 230, 285, 270, 240, 260,
        240, 245, 285, 250, 290, 260, 280, 300, 260, 275,
        275, 235, 280, 245, 255, 275, 240, 265, 230, 265
    ]
})

X = data[["키"]]
y = data["신발"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 1)

# ================ step 3 학습용 데이터로만 공부시키기 ==============================

model = LinearRegression()
model.fit(X_train, y_train)


# step 4. 점수 계산
train_에측 = model.predict(X_train)
test_에측 = model.predict(X_test)
공부용_MSE = mean_squared_error(y_train, train_에측)
시험용_MSE = mean_squared_error(y_test, test_에측)
시험용_MAE = mean_absolute_error(y_test, test_에측)

print(공부용_MSE)
print(시험용_MSE)
print(시험용_MAE)


# --------------------------------------------------------------------------------
# 실습 2, 
# step 1.

import pandas as pd

import pandas as pd

data = {
    '번호': [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    ],
    '주행거리(만km)': [
        5.7, 11.1, 5.1, 8.7, 6.5, 11.7, 14.4, 13.4, 9.5, 2.8,
        14.2, 0.8, 4.8, 4.6, 10.2, 7.6, 1.8, 0.7, 9.3, 7.6,
        9.2, 8.7, 13.4, 13.8, 3.2, 14.2, 11.9, 9.8, 10.1, 8.4,
    ],
    '가격(만원)': [
        1600, 820, 1520, 1100, 1460, 1050, 680, 800, 1030, 1950,
        590, 2420, 1750, 1690, 1140, 1330, 2210, 2480, 1160, 1390,
        1080, 1030, 790, 710, 1950, 840, 810, 1130, 1110, 1250,
    ],
}

df = pd.DataFrame(data)

# step 0.

X = data[["주행거리"]]
y = data['가격']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=1)

# step 1.
model = LinearRegression()
model.fit(X_train, y_train)

# step 2. 점수계산

train_예측 = model.predict(X_train)
test_예측 = model.predict(X_test)

print("공부용 MSE: ", mean_squared_error(y_train, train_에측))
print("시험용 MSE: ", mean_squared_error(y_test, test_에측))
print("시험용 MAE: ", mean_absolute_error(y_test, test_에측))

# step 3

평균가격 = y_train.mean()
기준선_예측 = [평균가격] * len(y_test)
기준선_MSE = mean_squared_error(y_test, 기준선_예측)

"선형회귀" if 시험용_MSE < 기준선_MSE else "평균만 찍는 모델"

