# kakaojoin.py

import sqlite3 as db
import streamlit as st

# 1. 저장소 만들기
conn = db.connect("kakao.db")

# 2. 조작도구 만들기
마우스 = conn.cursor()

# 3. 카카오톡 회원가입 페이지
# id, password, name, phone_number 는 꼭 입력!
# 칸마다 3질문
# - 이 칸으로 정확히 한 사람을 가르키나?
# - 이 칸이 비어있으면 안되나?
# - 이 칸이 중복이면 안되나?

# 데이터베이스에서 테이블을 관리하기 위해서
# 카톡 비유 친구,쇼핑,선물하기 등등
# 회원 테이블을 같이 쓴다.
# 오픈채팅탭 개발자가 비어있는값을 확인하는 if문
# 까먹음?

# 제약 조건 종류
# primary key (대표키)  # not null  (비우면 안됨!)   # unique   (겹치면 안된다(중복데이터 x))
# 규칙은 칸마다 다르다
 
# 대표 키를 작성할 때는 대부분 숫자로 작성 (문자 중복 발생 확률 높음.)  // uuid 찾아보기

마우스.execute("""
    create table if not exists members(
        회원번호    integer primary key autoincrement , 
        id             text         not null unique,
        password       text         not null ,
        name           text         not null,
        phone_number   text         not null unique
    )
""")

# not null 만 컬럼에 지정하면 값을 필수!
# 중복되는 값들이 들어올 수 있음.
# unique로 중복되면 안되는 칸들에게 추가 설정 (데이터 무결성)
# 모든 데이터를 저장하는 테이블에 대표 번호
# DB관리자(성능,백업,튜닝,권한,계정관리) - DBA   //  ++ OCP 자격증 얻어야함
# 제약조건 꼭 확인

st.title("kakao 회원가입")
id = st.text_input("id").strip()
password = st.text_input("password", type = "password").strip()
name = st.text_input("name").strip()
phone_number = st.text_input("전화번호 (ex: 010-1234-5678)").strip()

# 입력값들은 공백이 들어가면 문제가 발생할 수 있음
# VARCHAR() 글자 수 제한, not null은 값을 무조건 가져오고 값이 비면 안된다!

if st.button("가입하기"):
    마우스.execute(f"""
        insert into
            members (id, password, name, phone_number)
        values
            ('{id}','{password}','{name}','{phone_number}')
    """)

    conn.commit()         

# AI 챗봇 회원별 대화 기록 PK
# 머신러닝 학습 데이터
# 같은 회원이 들어가면 쏠림 현상 발생 -> unique로 막기
# 업무 자동화   



