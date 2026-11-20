# train.py
# 학습/시험용 데이터 나누기
# 데이터를 두 가지로 묶는다
# 학습용 데이터 (train Data) - 모델이 공부하는 데이터! (연습문제)
# 테스트 데이터 (test Data) - 모델이 처음보는 데이터!  (시험문제)

# 모델 공정하게 비교하려고
# 실행 순서: 1. 전체 데이터 준비 2. 학습용/시험용 분리 3. 학습용 데이터로 모델을 공부시킴 4. 시험용 데이터로 예측하고 MSE 계산 5. 점수보고 모델 평가 선택

# 데이터를 나누려면 도구가 필요함

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. 전체 데이터 준비
공부시간 = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]   # X: 문제 (대괄호 안에 대괄호 형태)
점수 = [12, 22, 29, 43, 48, 62, 68, 83, 88, 97]                 # y: 정답


# 2. 학습용/시험용 분리
# 나누는 기준 train: 80, test: 20 
X_train, X_test, y_train, y_test = train_test_split(공부시간, 점수, test_size= 0.2 , random_state= 1)

# 3. 잘 나눠어졌는지 확인
print("총 데이터: ", len(공부시간))
print("공부용 개수: ",len(X_train), "시험용 개수: ",len(X_test))
print("공부용 개수: ",len(y_train), "시험용 개수: ",len(y_test))

# 4. 모델의 학습
# 학습을 해서 숫자로 결과를 보여주는 모델 선형 회귀 모델
model = LinearRegression()

# 5. 학습 
model.fit(X_train,y_train)

# 6. 예측
# 공부용, 시험용 데이터로 예측
공부용학습예측 = model.predict(X_train)
시험용학습예측 = model.predict(X_test)

print("공부용 MSE : ", mean_squared_error(y_train, 공부용학습예측))
print("시험용 MSE : ", mean_squared_error(y_test, 시험용학습예측))


# 리팩토링

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

RANDOM_STATE = 1
test_size = 0.3

def load_data():
    기온 = np.arange(15, 25).reshape(-1, 1)
    판매량 = np.array([21, 24, 33, 35, 42, 47, 52, 56, 66, 70])
    return 기온, 판매량


def evaluate(model, X, y , name):
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"{name} MSE: {mse:.2f}")
    return mse


def main():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size= test_size, random_state= RANDOM_STATE
    )
    print(f"학습용 개수: X={len(X_train)}개, y={len(y_train)}개",)
    print(f"시험용 개수: X={len(X_test)}개, y={len(y_test)}개",)

    model = LinearRegression()
    model.fit(X_train, y_train)

    evaluate(model, X_train, y_train, "학습용")
    evaluate(model, X_test, y_test, "시험용")

    # 어제 배운 기울기 절편
    print(f"기울기: {model.coef_[0]:.2f}, 절편: {model.intercept_ :.2f}")

if __name__ == "__main__":
    main()



    