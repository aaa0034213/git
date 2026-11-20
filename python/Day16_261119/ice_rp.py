from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

기온     = [20, 25, 30, 22, 28, 24, 27, 31, 23, 29]
주말     = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]          # 1 = 주말, 0 = 평일
점원번호 = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
판매량   = [20, 50, 30, 44, 28, 48, 27, 62, 23, 58]  # 정답

# 1. baseline

average = sum(기온[0:8]) / 8

# 예측할 값 앞에 8개 -> 평균을 계산에 사용 / 뒤에 2개는 맟혀 볼 정답

baseline_predict = [average,average]

print("basline average : ", round(average, 1) )
print("predict :", baseline_predict, " answer :", 판매량[8:])
print("mean_error :", round(mean_absolute_error(판매량[8:], baseline_predict)))


힌트 = [
        [20], [25], [30],
        [22], [28], [24],
        [27], [31], [23], [29]
      ]

# 주말

힌트1 = [[20, 0], [25, 1], [30, 0], [22, 1], [28, 0],
         [24, 1], [27, 0], [31, 1], [23, 0], [29, 1]]

# 점원번호 
힌트2 = [[20, 0, 3], [25, 1, 1], [30, 0, 2], [22, 1, 3], [28, 0, 1],
         [24, 1, 2], [27, 0, 3], [31, 1, 1], [23, 0, 2], [29, 1, 3]]


def 학습(힌트, 판매량):

    model = LinearRegression()

    model.fit(힌트[:8], 판매량[:8])

    예측 = model.predict(힌트[:8])

    total = 0

    for 정답, 답 in zip(판매량, 예측):
        틀린크기 = abs(정답 - 답)
        total += 틀린크기
        print(f"정답: {정답}, 답: {답}, 틀린크기: {틀린크기}")

    print("틀린크기의 합계: ", total)
    print("평균 오차: ", total / 2 )





