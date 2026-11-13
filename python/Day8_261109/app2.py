# app2.py

# 1. app2.py 파일을 실행 할 떄 스트림릿
# 도구를 포함해줘

import streamlit as st

st.title("단어 퀴즈")

st.header("문제 1")
st.write("사람이 정한 규칙에 따라 작동하는 AI는?")

answer1 = st.text_input("정답 입력: ")

# 입력한 글 화면에 보이기
st.write(answer1)


if answer1 != "":
    if answer1 == "머신러닝" or answer1 == "머신 러닝":
        st.success("정답입니다!")
    else:
        st.error("오답, 다시 입력하세요.")




if answer1 == "규칙 기반AI":
    st.write("정답입니다!")
elif answer1 == "":
    st.space()
else:
    st.write("다시 도전하세요!")

st.header("문제 2")
st.write("데이터에서 패턴을 학습하는 기술?")

answer2 = st.text_input("정답 입력")

st.write(answer2)

if answer2 == "머신러닝" or answer2 == "Machine Learning":
    st.write("정답입니다!")
elif answer2 == "":
    st.space()
else:
    st.write("다시 도전하세요!")


# 다른 버전
if answer1 != "":
    if answer1 == "머신러닝":
        st.write("정답")
    else:
        st.write("오답")

