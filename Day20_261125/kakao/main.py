# main.py
# 항상 streamlit은 main 파일에서 실행! - streamlit run main.py
# 

import streamlit as st
import sqlite3 as db

db저장소 = db.connect("kakao.db")
마우스 = db저장소.cursor()

마우스.execute("""
    CREATE TABLE IF NOT EXISTS members(
    회원번호    INTEGER PRIMARY KEY AUTOINCREMENT,
    아이디      TEXT    NOT NULL UNIQUE,
    비밀번호    TEXT    NOT NULL,
    이름        TEXT    NOT NULL,
    전화번호    TEXT    NOT NULL UNIQUE
    )
""")


if "로그인한유저" not in st.session_state:
    st.session_state["로그인한유저"] = None

st.title("💛 카카오 로그인")

아이디 = st.text_input("아이디").strip()
비밀번호 = st.text_input("비밀번호", type="password").strip()

if st.button("로그인"):
    마우스.execute(f"""
        SELECT
            * 
        FROM
            members
        WHERE
            아이디 = '{아이디}' AND 
            비밀번호 = '{비밀번호}'
    """)

    회원 = 마우스.fetchone()

    if 회원 == None:
        st.warning("아이디 또는 비밀번호를 확인해주세요")
    else:
        st.session_state["로그인한유저"] = 회원
        st.switch_page("pages/2_채팅목록.py")

st.page_link("pages/1_회원가입.py", label="아직 회원이 아니라면? 회원가입")
