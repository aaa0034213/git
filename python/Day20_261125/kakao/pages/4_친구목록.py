# 4_친구목록.py

# 친구 목록 창을 띄우고 그 위에 검색하는 창
# 친구 목록 검색하는 sql 명령어

import streamlit as st
import sqlite3 as db

db저장소 = db.connect("kakao.db")
마우스 = db저장소.cursor()

# 서비스 기본 규칙
# CRUD - Create, Read, Update, Delete   # 규칙 설정
# def create()  def read()  def update()  def delete()


# 친구 목록에 필요한 테이블?
# - members 테이블 활용해서 친구 검색

회원 = st.session_state["로그인한유저"]

# 로그인 회원이 없으면 None 이 나옴
st.title("카카오 친구목록")

# 친구목록 검색창
검색어 = st.text_input("이름으로 검색").strip()


if 회원 == None:
    st.write("로그인부터 하세요")
    st.page_link("main.py", labe= "로그인하러 가기")

else:
    # 1. 준비 : 나는 누구
    나 = 회원[3]

    # 검색했을 때 나오는 친구만 가져오기
    # 조건: 나빼고 나와야함
    # -- 컬럼명 like '%{검색어}%'   어디든 검색어 문자가 포함되어있으면

    # 김% >> 김씨로 시작하는 문자만 검색
    # %김동욱 >> 김동욱으로 끝나는 문자만 검색
    # %김동욱% >> 김동욱 검색 (검색창은 많이씀)

    마우스.execute(f"""
        select
            아이디, 이름
        from
            members
        where
            이름 like '%{검색어}%' 

    """)
    친구목록 = 마우스.fetchall()

    for 아이디, 이름 in 친구목록:
        with st.container(border=True):
            st.write(f"👤 **{이름}** : **{아이디}**")


    # 2. 조회: 나만 빼고 모든 회원가져오기
    # 마우스.execute(f"""
    #     select 
    #         이름
    #     from
    #         members
    #     where
    #         이름 !='{나}'
    
    # """)
    # 친구목록 = 마우스.fetchall()
    
    # # 3. 출력 
    # # 친구 수
    # st.write("친구수", len(친구목록) ,"명" )


    # # 친구 목록
    # # for 문 write()
    # for 이름 in 친구목록:
    #     with st.container(border=True):
    #         st.write(f"👤 **{이름[0]}**")

# 전체 친구목록
# 데이터를 보여줄 때까지 페이지를 끊어서 보여준다
# 15개,5개씩 (pagenation)


