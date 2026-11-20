# 0. 라이브러리 설정
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 1. 환경 변수 설정
# 파일 경로, X, y , test_size , random_state

FILE_PATH = "캐릭터_스탯.csv"
FEATURES = ["STR", "CON", "DEX"]
TARGET = "전투력"
TEST_SIZE = 0.2     # 따로 빼서 변경 하기 쉽게 설정 ! ex) 0.2, 0.3 유동적으로 바꾸면서 확인
RANDOM_STATE  = 1   # 마찬가지로 따로 빼서 설정

def load_data(file_path):       # 데이터를 불러오기
    return pd.read_csv(file_path)


def split_data(data, features, target): # 데이터 분할
    
    X = data[features]
    y= data[target]

    return train_test_split(X, y , 
                            test_size= TEST_SIZE, random_state= RANDOM_STATE)


def train_model(model, X_train, y_train):   # 데이터 훈련
    model.fit(X_train, y_train) 

    return model

def evaluate_model(model, X_test, y_test):      # 데이터 예측
    y_pred = model.predict(X_test)  # 예측

    return {
        "예측 평균: " : y_pred.mean(),
        "MAE: " : mean_absolute_error(y_test, y_pred),
        "MSE: " : mean_squared_error(y_test, y_pred)
     }

def print_results(results):             # 결과 보이게 하기
    print("----- 모델 평가 결과 -----")

    for n, v in results.items():
        print(f"{n}: {v:.2f}")


def print_중요도(model, features):          # 중요도 변화       # 중요도는 왜 중요한가?   어떤 변수가 결과에 얼마나 영향을 미치는지 확인하기 위해서?
    print("------ 중요도 -------")  
    for n , w in zip(features, model.coef_):        # coef_ : 컴퓨터가 fit으로 알아낸 곱할 숫자 저장 리스트
        print(f"{n} 1 올리면 전투력: {(round(w, 2))} 변화")

def main():

    data = load_data(FILE_PATH)

    X_train, X_test, y_train, y_test = split_data(data, FEATURES, TARGET)

    model = train_model(LinearRegression(), X_train, y_train)      # 따로 빼서 모델 다른거 넣어서 확인 할 수 있게 구현함.......... ㅇ3ㅇ

    results = evaluate_model(model, X_test, y_test)

    print_results(results)

    print_중요도(model, FEATURES)


if __name__ == "__main__":
    main()