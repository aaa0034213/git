# 실습 1.

import streamlit as st

st.title("1. AI보다 정확하게 세기")
st.write("AI에게 글자 수를 물어보고, 파이썬으로 확인해보자!")


문장 = st.text_input("문장을 입력하세요")

글자 = st.text_input("셀 글자를 입력하세요")

ai개수 = st.text_input("AI가 말한 개수를 입력하세요")


if 문장 == "" or 글자 == "" or ai개수 == "":
    st.error("빈칸이 존재합니다. 입력해주세요")
else:
    문장 and 글자 and ai개수 
    정답 = 문장.count("글자")
    st.write("파이썬이 샌 글자", 정답)


    if ai개수 == str(글자):
        st.success("ai가 맞췄어요!")
    else:
        st.error("ai가 틀렸어요! 정확한 계산이 필요해요.")



st.title("게임 2. 개인정보 가리기")

st.write("AI에게 보냐기 전에 개인정보를 가려보자")

원문 = st.text_input("AI에게 보내는 문장을 입력하세요")

가릴말 = st.text_input("가릴 단어를 입력하세요.(이름, 전화번호)")

if 원문 and 가릴말:
    if 원문.count(가릴말) > 0:
        결과 = 원문.replace(가릴말, "***")
        st.success("가입했어요! 이제 ai에게 보내도 좋아요")
        st.write(결과)

    else:
        st.error("그 단어는 문장에 없어요. 다시 확인하세요")


st.title("게임 3. AI 기억 챌린지")
st.write("AI의 기억 창고가 10칸뿐이라고 가정해보자")

문장 = st.text_input("AI에게 말할 문장을 입력하세요")


창고칸= 10

if 문장:
    조각들 = 문장.split()

    st.header("1. 문장을 조각으로 나누기")
    st.write(조각들)
    st.write("조각 개수", len(조각들))

    if len(조각들) <= 창고칸:
        st.success("모두 기억했어요")
        st.write("기억하는 조각", 조각들)

    else:
        잊은조각 = 조각들[:-창고칸]
        기억조각 = 조각들[-창고칸:]

        st.error(f"{len(잊은조각)}개를 기억창고에서 잃어버렸어요")
        st.write("잊어버린 조각", 잊은조각)
        st.write("기억하는 조각", 기억조각)






