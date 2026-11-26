# second.py
import streamlit as st

st.title("2번 페이지")

# 2 page -> 1 page 

st.page_link("pagelink.py", label= "1번 페이지로 가기" , icon = "🚕")

# 세션 꺼내기
st.write(st.session_state["로그인아이디"])
st.write(st.session_state["이름"])