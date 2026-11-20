# csv파일을 불러오기 ,예측
import pandas as pd

# 모델,학습,예측,채점

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. 실습
# STR(공격력) 하나로 전투력을 예측 결과확인
# STR, DEX, CON ( 공격, 속도, 방어 ) 힌트로 주었을 때 전투력 예측
# 예측하는 결과확인

data = pd.read_csv("캐릭터_스탯.csv")

X = data[["STR","CON","DEX"]]
y = data["전투력"]

X_train, X_test, y_train, y_test = train_test_split(X , y , test_size= 0.2, random_state= 1)

model = LinearRegression()
model.fit(X_train,y_train)

예측 = model.predict(X_test)

print()
print(f"예측 평균: {예측.mean()}")
print("MAE: ", mean_absolute_error(y_test, 예측))
print("MSE: ", mean_squared_error(y_test, 예측))


#--------------------------------------------------
# 리팩토링
# 1. 데이터 준비 및 분할

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

def 데이터준비(file):
    data = pd.read_csv(file)

    X = data[["STR", "CON", "DEX"]]
    y = data["전투력"]

    return train_test_split(X , y , test_size= 0.2, random_state= 1)


def 모델_학습(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model


def 모델_평가(model, X_test, y_test):
    예측 = model.predict(X_test)

    print(f"예측 평균: {예측.mean()}")
    print("MAE: ", mean_absolute_error(y_test, 예측))
    print("MSE: ", mean_squared_error(y_test, 예측))


X_train, X_test, y_train, y_test = 데이터준비("캐릭터_스탯.csv")

model = 모델_학습(X_train, y_train)

모델_평가(model ,X_test, y_test)

# import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# 환경 설정
FILE_PATH = "캐릭터_스탯.csv"
FEATURES = ["STR", "CON", "DEX"]
TARGET = "전투력"
TEST_SIZE = 0.2
RANDOM_STATE = 1


def load_data(file_path):
    """CSV 데이터를 불러온다."""
    return pd.read_csv(file_path)


def split_data(data, features, target):
    """독립변수와 종속변수를 설정하고 데이터를 분할한다."""
    X = data[features]
    y = data[target]

    return train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )


def train_model(model, X_train, y_train):
    """모델을 학습한다."""
    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):
    """모델의 예측 성능을 평가한다."""
    y_pred = model.predict(X_test)

    return {
        "예측 평균": y_pred.mean(),
        "MAE": mean_absolute_error(y_test, y_pred),
        "MSE": mean_squared_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "R2": r2_score(y_test, y_pred)
    }


def print_results(results):
    """모델 평가 결과를 출력한다."""
    print("===== 모델 평가 결과 =====")

    for name, value in results.items():
        print(f"{name}: {value:.4f}")


def main():
    data = load_data(FILE_PATH)

    X_train, X_test, y_train, y_test = split_data(
        data, FEATURES, TARGET
    )

    model = train_model(LinearRegression(), X_train, y_train)

    results = evaluate_model(model, X_test, y_test)

    print_results(results)


if __name__ == "__main__":
    main()