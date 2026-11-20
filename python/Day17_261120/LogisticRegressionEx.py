# LogisticRegressionEx.py
# 분류 (정답이 숫자가 아니라 문자(종류)로 나옴)
# 실행 순서
# 1. 과거 기록 준비 2. 필요한 도구 만들기(model)  3. fit(학습)  4. predict() 답을 줌
# 5. predict_proba(확률) 6. 화면 출력

# 상황
#  - 택시 앱이 "이 사용자는 택시를 탈까?" 를 맞히려고 한다
#   과거 기록
# 1km -> 안 탄다   0
# 2km -> 안 탄다   0
# 3km -> 안 탄다
# 4km -> 안 탄다
# 5km -> 탄다      1
# 6km -> 탄다      1
# 7km -> 탄다
# 8km -> 탄다

# 규칙을 찾아서 예측! 숫자 , 확률
# linear 결과 확인
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# 과거 기록 (힌트 + 정답
# 힌트: 이동거리
# 거리 = [[1], [2], [3], [8], [9], [10]]

# 정답: 회귀는 숫자만 받으니 0,1 로 바꿨다.
# 0: 안탄다     1: 탄다
# 탑승 = [0, 0, 0, 1, 1, 1]

# # 공부 시키기
# model = LinearRegression()
# model.fit(거리, 탑승)

# # 화면
# st.title("택시를 탈까요?(회귀)")

# 입력거리 = st.number_input("이동거리 (km)", value = 0, min_value= 0)

# # 버튼을 눌렀으면 예측하기 실행
# if st.button("예측하기"):
#     # 예측한 결과가 리스트로 나온다.
#     # 직선에서 거리의 값을 읽는다.
#     result = model.predict([[입력거리]])
#     st.write("회귀가 계산한 값:", round(float(result[0]), 2))

#-----------------------------------------------------------------------------------------

# 거리 = [[1], [2], [3], [8], [9], [10]]
# 탑승 = ["안 탄다", "안 탄다", "안 탄다", "탄다", "탄다", "탄다"]

# # 학습 시키기 (분류를 하는 모델로)
# st.subheader("로지스틱 회귀")
# model = LogisticRegression()
# model.fit(거리, 탑승)

# st.title("택시를 탈까요?(분류)")

# 입력거리 = st.number_input("이동거리 (km)", value= 0, min_value= 0)

# if st.button("예측하기"):
#     result = model.predict([[입력거리]])
#     확률 = model.predict_proba([[입력거리]])
#     탄다칸 = list(model.classes_).index("탄다")

#     # 결과 리스트 첫 번째 값(글자)
#     if result[0] == "탄다":
#         st.write("택시를 탄다")
#     else:
#         st.write("택시를 안탄다")


#     st.write("택시를 탈 확률: ", round(float(확률[0][탄다칸]) * 100), "%")

    # 로지스틱 회귀: 0 ~ 100 사이의 규칙을 찾아서 알려주는 도구
    # predict()는 확률이 더 높을쪽을 답해준다. (50%)
    # predcit_proba() 확률 그래로 보여준다.

    # 상황
#  - 메일 서비스가 "이 메일은 스팸일까?" 맞힙니다.
#  - 힌트는 메일 속 링크 개수

# 과거 기록(힌트 : 링크 , 스)
링크 = [[0], [1], [2], [6], [7], [8]]
스팸 = ["정상", "정상", "정상", "스팸", "스팸", "스팸"]

# title
st.title("스팸일까요? (분류)")
입력링크= st.number_input("링크 개수: ", value = 0, min_value = 0)

# 공부 시키기
model = LogisticRegression()
model.fit(링크, 스팸)

# 예측하기
if st.button("예측하기"):
    result = model.predict([[입력링크]])
    확률 = model.predict_proba([[입력링크]])
    스팸칸 = list(model.classes_).index("스팸")

    st.write(확률)
    st.write(스팸칸)
    st.write(list(model.classes_))

    if result[0] == "스팸":
        st.write("스팸 메일!")
    else:
        st.write("정상 메일!")


    st.write("스팸일 확률: ", round(float(확률[0][스팸칸]) * 100), "%")

# predict_proba

# ----------------------------------------------------------------------------------

안한날 = [[1],[2],[3],[8],[9],[10]]
해지 = ["유지","유지","유지","해지","해지","헤지"]

st.title("구독 서비스! (분류)")
입력구독 = st.number_input("구독 (해지,유지): ", value = 0, min_value= 0 )

model = LogisticRegression()
model.fit(안한날, 해지)

if st.button("해지할까?"):
    result = model.predict([[안한날]])
    확률 = model.predict_proba([[안한날]])
    해지칸 = list(model.classes_).index("해지")

    st.write(확률)
    st.write(해지칸)
    st.write(list(model.classes_))

    if result[0] == "해지":
        st.write("구독 해지!")
    else:
        st.write("구독 유지!")

    st.write("구독 해지 할 확률: ", round(float(확률[0][해지칸]) * 100), "%")


#------------------------------------------------------------------------------

import streamlit as st
from sklearn.linear_model import LogisticRegression

안한날 = [[1],[2],[3],[8],[9],[10]]
해지 = ["유지","유지","유지","해지","해지","헤지"]

st.title("구독 서비스! (분류)")
입력구독 = st.number_input("구독 (해지,유지): ", value = 0, min_value= 0 )

model = LogisticRegression()
model.fit(안한날, 해지)

if st.button("해지할까?"):
    result = model.predict([[안한날]])
    확률 = model.predict_proba([[안한날]])
    해지칸 = list(model.classes_).index("해지")

    st.write(확률)
    st.write(해지칸)
    st.write(list(model.classes_))

    if result[0] == "해지":
        st.write("구독 해지!")
    else:
        st.write("구독 유지!")

    st.write("구독 해지 할 확률: ", round(float(확률[0][해지칸]) * 100), "%")


