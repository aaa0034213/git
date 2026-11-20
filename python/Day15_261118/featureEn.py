# featureEn.py
# 특성(힌트)공학(바꾸다) = AI가 알아보기 쉽게 힌트를 바꾸는 일
# 1. 섞기
# 2. 글자를 숫자로
# 3. 빼기

# 편의점.csv 파일을 다운로드 해서 data폴더 안으로 집어넣으세요!
# # 1.도구
# # csv파일을 불러오기 ,예측
import pandas as pd

# # 모델,학습,예측,채점

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 데이터 불러오기
# file의 위치가 변경됨
# 같은 폴더는 상관없지만 다른 폴더에 있을 때 ex) Data 폴더 안에 편의점.csv 존재

데이터 = pd.read_csv("Data/편의점.csv")
# print(데이터.head(3))

X = 데이터[["개당가격", "개수", "계산대번호"]]
y = 데이터["총금액"]

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size= 0.2 , random_state= 1)

model = LinearRegression()

model.fit(X_train, y_train)

예측 = model.predict(X_test)

# 기준선
# 평균만 찍기
# 하나는 답으로 쓰는 평균
# 다른 하나는 그냥 계산 평균
# 기준선 쓰는 이유 - AI가 쓸모있는지 판단 하려고 만든 것

# 기준선을 안만들게 되면 학습한 내용의 평균이 10.92원
# 기준선을 만들면 AI가 문제마다 다른 답을 내지않게 기준을 만듦
평균 = y_train.mean()
기준선_예측 = [평균] * len(y_test)
print("[기준선] 평균만 찍기 평균 오차: ", mean_squared_error(y_test, 예측))

# AI가 예측한 평균들을 모아서 평균을 낸 것
print()
print("평균 : ", 예측.mean())
print("[섞기 전] : 평균 오차 : ", round(mean_absolute_error(y_test, 예측)) )

# 