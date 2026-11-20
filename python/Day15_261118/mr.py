# 파일명:mr.py
# 폴더명 : Day15_20261118
# 질문 잡담방 안에 20261118메시지 댓글에 파일있습니다.
# 다중회귀
# 단순회귀
#  - 힌트가 하나를 가지고 예측한다.
# 키 -> 신발 사이즈 예측
# 온도 -> 커피 수량 예측

# 1.도구
# csv파일을 불러오기 ,예측
import pandas as pd

# 모델,학습,예측,채점

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 상황
# - 내일 커피가 얼마나 팔릴까?

# # 1.데이터 (파일을 읽어서 저장)
# #  - 표 형식
# 데이터 = pd.read_csv("카페.csv")

# #print(데이터)
# # 2. 데이터변수에서 기온만 출력하기
# #print(데이터["기온"])

# # X 내가 알고있는것! (온도)
# # y 내가 알고 싶은것! (판매량)
# X = 데이터[["기온"]]
# y = 데이터["판매량"]

# # 학습용/ 테스트용 나눈다.
# # 진짜 점수를 확인하려고!
# # 무작위로 뽑는다

# X_train,X_test,y_train,y_test = train_test_split(X,
#                                                  y,
#                                                  test_size=0.2,
#                                                  random_state=1)

# # 모델 *숫자로 예측한다*
# 모델 = LinearRegression()
# 모델.fit(X_train,y_train)

# 예측 = 모델.predict(X_test)

# print("MAE", mean_absolute_error(y_test, 예측))
# print("MSE", mean_squared_error(y_test, 예측))

# 다중회귀
#  여러개의 힌트를 이용해서 더 정확한 예측을하자

# 키 -> 신발 사이즈를 예측하는 프로그램
# 1. csv파일에서 162, 170 검색해서 신발 사이즈가 똑같은지? 확인
# 162 2개는 270, 162 250

# 평균 255 사이즈
# 내 실제 사이즈 250
# 실제 사이즈 270
# 하나의 힌트만 보면 예측이 틀릴 수있어
# 여러가지의 힌트를 보고 정확하게 예측해줄려고 (오차를 줄인다는것!)
# 다중회귀

# 1.데이터 (파일을 읽어서 저장)
#  - 표 형식
데이터 = pd.read_csv("신발.csv")

#print(데이터)
# 2. 데이터변수에서 기온만 출력하기
#print(데이터["기온"])

# X 내가 알고있는것! (온도)
# y 내가 알고 싶은것! (판매량)
X = 데이터[["키","몸무게"]]
y = 데이터["신발사이즈"]

# 학습용/ 테스트용 나눈다.
# 진짜 점수를 확인하려고!
# 무작위로 뽑는다

X_train,X_test,y_train,y_test = train_test_split(X,
                                                 y,
                                                 test_size=0.2,
                                                 random_state=1)

# 모델 *숫자로 예측한다*
모델 = LinearRegression()
모델.fit(X_train,y_train)

예측 = 모델.predict(X_test)

print()
print(예측.mean())
print("MAE", mean_absolute_error(y_test, 예측))
print("MSE", mean_squared_error(y_test, 예측))

# 1. 실습
# STR(공격력) 하나로 전투력을 예측 결과확인
# STR, DEX, CON ( 공격, 속도, 방어 ) 힌트로 주었을 때 전투력 예측
# 예측하는 결과확인

data = pd.read_csv("캐릭터_스탯.csv")

X = [["STR","CON","DEX"]]
y = ["전투력"]

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size= 0.2, random_state= 1)

model = LinearRegression()
model.fit(X_train,y_train)

예측 = model.predict(X_test)

print()
print(예측.mean())
print("MAE", mean_absolute_error(y_test, 예측))
print("MSE", mean_squared_error(y_test, 예측))
