# 0. 라이브러리 설치

import sqlite3 as db
import streamlit as st
from datetime import datetime

# 누가 작성했는지?               준호        작성자
# 어떤 채팅방인지?              점심메뉴방    채팅방
# 무슨 내용을 입력할 것인지       마라탕       내용
# 채팅 내역 순서대로 (시간대로) 저장


# 1. 저장소 생성

con = db.connect("Linechat.db")

# 2. 데이터 저장
# 준호 화면에 점심 메뉴방 채팅방에서 점심 메뉴들 채팅 메세지 입력
# 채팅방 조회시 채팅 내역이 보여야함

# 한 사람이 등록한 채팅방 

# 3. 도구 설정

control = con.cursor()

# 4. 테이블 정의

control.execute("""
    create table if not exists Linechat(
        메시지번호 integer primary key autoincrement,   -- auto 설정 (기본키로)
        작성자화면   text,
        채팅방      text,
        채팅내역    text,
        작성시간    text
    )            
""")

# 5. 화면 구성

st.title("Line (축소판)")
작성자화면 = st.selectbox("누구의 화면인가요?", ["신지", "준호"])
채팅방 = st.selectbox("채팅방", ["아침 메뉴방","점심 메뉴방", "저녁 메뉴방"])


# 6. 채팅 조회
control.execute("""
    select
        *
    from
        Linechat
""")

# 6.5 채팅 목록 가져오기
chatlist = control.fetchall()

# 7. 채팅 출력

for 메시지번호, 보낸사람, 방, 내용, 작성시간 in chatlist:

    if 방 == 채팅방:

        st.write(보낸사람, "·", 작성시간)
        st.write(내용)

        # 삭제 만들기
        if st.button("삭제", key = 메시지번호):

            control.execute(f"""
                delete from 
                    Linechat
                where 
                    메시지번호 = '{메시지번호}'
            """)
            
            con.commit()
            st.rerun()

        st.write("")

msg = st.chat_input("메시지를 입력하세요")

# 메세지 저장
if msg:

    if msg.strip() == "":
        st.warning("메시지 입력하세요!")

    else:
        # datetime 으로 현재 입력시간으로 설정
        작성시간 = datetime.now().strftime("%H:%M") # 시간,분

        # msg 추가

        control.execute(f"""
            insert into
                Linechat (작성자화면, 채팅방, 채팅내역, 작성시간)
            values
                ('{작성자화면}','{채팅방}','{msg}','{작성시간}')
        """)

        con.commit()
        st.rerun()

con.close()