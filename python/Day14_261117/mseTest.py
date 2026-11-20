# mseTest.py

# MAE 틀린 평균을 낸다
# MSE 틀린 크기에 제곱을 해서 평균을 낸다 
# 큰 실수를 훨씬 크게 벌 준다
# Mean Squared Error

import pandas as pd
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 실제 = [30, 30, 30, 30]
# A예측 = [32, 32, 32, 32]
# B예측 = [30, 30, 30, 38]

# print("A MAE:", mean_absolute_error(실제, A예측))
# print("B MAE:", mean_absolute_error(실제, B예측))

# 오차 = [abs(a - b) for a, b in zip(실제, B예측)]
# print("가장 큰 오차: ", max(오차))

# MSE 가 없으면
# 평균이 같은 모델의 차이를 못봄, 큰 실수를 찾으려 코드를 따로 짬, 사고 난 뒤에야 문제를 알게됨

# MSE 가 있으면
# 큰 실수를 막을 수 있고, 지표 하나로 비교, 배포 전에 위험 걸러내기 가능

# 응급실 환자 수 예측
# 약국 약 재고 예측
# 전력 수요 예측
# 폭염, 태풍 피해 예측

# 모델이 여러 개 일 때 점수로 비교해서 더 좋은 모델 구하기
# 숫자 하나로 이 모델이 얼마나 틀리는가?(MAE, MSE)
# 점수가 낮을수록 좋은 모델
# 오차 = 정답과 예측이 얼마나 다른가
# 오차의 평균 (틀린만큼 벌주기)
# 오차 제곱한 값의 평균(크게 틀릴수록 벌을 더 크게준다)

# 학습하고 예측한 값들
# 현재 정답은 10 기준

A_model = [9,11,9,11]       # 틀린정도 [1,1,1,1]
B_model = [10,10,10,14]     # 틀린정도 [0,0,0,4]

# 확인 검증 MSE
# A (1+1+1+1) / 4 = 1
# B (0+0+0+4) / 4 = 1

# Rule : 현재 값에 제곱을 해서 평균
# A (1x1 + 1x1 + 1x1 + 1x1 ) / 4 = 1점
# B (0x0 + 0x0 + 0x0+ 4+4 ) / 4 = 4점       # A < B 오차확률

# 실행 순서
# 1. 정답과 모델별 예측값을 준비
# 2. 모델마다 오차 점수(MAE, MSE) 계산
# 3. 점수 비교
# 4. 점수가 낮은 모델을 선택

answer = [10,10,10,10]
A_model = [9,11,9,11]       # 틀린정도 [1,1,1,1]
B_model = [10,10,10,14]     # 틀린정도 [0,0,0,4]

print()
print("A mae: ", mean_absolute_error(answer, A_model))      # mean_absolute_error(정답, 비교할 모델)
print("B mae: ", mean_absolute_error(answer, B_model))
print()
print("A mse: ", mean_squared_error(answer, A_model))       # mean_squared_error(정답, 비교할 모델)
print("B mse: ", mean_squared_error(answer, B_model))

print()
mse_a = mean_squared_error(answer, A_model)
mse_b = mean_squared_error(answer, B_model)

print("선택된 모델은?: ", "A" if mse_a < mse_b else "B")

# 예측값은 직접 적지 않고 model.predict(data)로 모델이 만들어진 값
# 비교할 때는 기준선(baseline)을 꼭 둔다.
# 점수가 낮다고 해서 확정짓지 않음.(속도, 비용, 안전성)

# 치킨집 주문량 예측
# 치킨집의 하루 실 주문량 [20,30,40]
정답 = [20,30,40]
X_model = [22, 28, 42]
y_model = [20, 30, 46]

# 각 모델의 MAE, MSE를 출력해보시요
print("X  MAE:", mean_absolute_error(정답, X_model), " MSE:", mean_squared_error(정답, X_model))
print("Y  MAE:", mean_absolute_error(정답, y_model), " MSE:", mean_squared_error(정답, y_model))


# 수요 예측(주문량, 판매량, 재고 발주)

def MAE(y_true, y_pred):
    return sum(abs(a-b) for a,b in zip(y_true, y_pred)) / len(y_true)

def MSE(y_true, y_pred):
    return sum((a-b)**2 for a, b in zip(y_true, y_pred)) / len(y_true)

print(f"X_model MSE: {MAE(정답, X_model)}, X_model MSE: {MSE(정답, X_model)}")
print(f"y_model MSE: {MAE(정답, y_model)}, y_model MSE: {MSE(정답, y_model)}")

# 배달 시간 예측 예측 오차가 2배가 되면 점수?
# 실제 데이터 - 실제 배달 시간 4건
정답 = [30, 30, 30, 30]

X_예측 = [32, 34, 38]
y_예측 = [30, 30, 30, 50]

# 입력을 바궈가면서 어떻게 변하는지 봄, 서비스 운영중에 오차 점수를 매일 계산해 그래프로 모니터링
# 점수가 오른 원인은 데이터 오류, 시장변화, 모델 노후화 -> 다양하게 수집해서 점수는 "문제를 찾으러갈 신호"

for x in [32, 34, 28]:
    예측 = [30, 30, 30, x]
    print(x, "MAE:", mean_absolute_error(정답, 예측),
             "MSE: ", mean_squared_error(정답, 예측))

