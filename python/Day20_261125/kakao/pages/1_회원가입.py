# 1_회원가입.py
import streamlit as st
import sqlite3 as db

db저장소 = db.connect("kakao.db")
마우스 = db저장소.cursor()

st.title("🙋 카카오 회원가입")
아이디 = st.text_input("아이디").strip()
비밀번호 = st.text_input("비밀번호", type="password").strip()
이름 = st.text_input("이름").strip()
전화번호 = st.text_input("전화번호 (예: 010-1234-5678)").strip()

if st.button("가입하기"):
    if 아이디 == "" or 비밀번호 == "" or 이름 == "" or 전화번호 == "":
        st.warning("아이디, 비밀번호, 이름, 전화번호는 꼭 입력하세요!")
    else:
        # 중복검사
        마우스.execute("""
            SELECT
                * 
            FROM 
                members
            WHERE 
                아이디 = ? OR
                전화번호 = ?

        """, (아이디, 전화번호))
        
        이미있음 = 마우스.fetchone()

        if 이미있음 is not None:
            st.warning("이미 사용 중인 아이디 또는 전화번호예요!")
        else:
            마우스.execute("""
                insert into members (아이디, 비밀번호, 이름, 전화번호)
                values (?, ?, ?, ?)
            """, (아이디, 비밀번호, 이름, 전화번호))
            db저장소.commit()
            st.success(f"{이름}님 가입 완료!")

st.page_link("main.py", label="로그인하러 가기")

