# database.py
# DB - 컴퓨터를 꺼도 데이터 유지

import sqlite3 as db
import streamlit as st

# 1. DB-store
# connect() - 저장소가 있으면 저장소 연결만하기
# - 저장소 없으면 저장소 생성하고 연결
conn = db.connect("kakao.db")

# 2. 공간 조작 cursor
마우스 = conn.cursor()

# 3. 한 줄에 어떤 내용들이 들어가는지?
# 한 줄 = 메시지 하나

# 민지와 준호가 "우리반 단톡방"에서 대화한다.
# 메시지를 보냈을 때 보낸사람,내용,보낸시간이 보인다
# 내일 앱을 다시 열어도 대화가 순서대로 그대로 남아있어한다.

# 누가 보냈는지?    
# 어디에 보냈지?
# 무슨말을 보냈지?
# 언제 보냈지?

# 채팅방 : 우리방 단톡방
# 보낸사람: 민지
# 내용: 안녕!
# 보낸 시간: 11월24일 9:$5
# autoincrement - db가 직접 자동으로 숫자를 증가.

# text - 긴 글 (블로그)
# 아이디, 비밀번호, 이메일 글자 수 제한
# varchar(숫자) - db에서 글자 제한할 때 활용

# 자동으로 증가하려면 내가 원하는 한 줄을 콕 집을 수 있게 기본 번호를 줘야함.
# 기본키 (PK)   


마우스.execute("""
        create table if not exists msg (
            메시지번호  integer primary key autoincrement, 
            채팅방      text,
            보낸사람     text,
            내용        text,
            보낸시간    text
        )
""")

st.title("카카오 채팅방")
# 채팅방 추가
채팅방이름 = st.selectbox("채팅방 고르기", ["우리방 단톡방", "점심 메뉴방"])

나 = st.selectbox("누구의 화면인가요?", ["민지", "준호"])

메시지 = st.chat_input("메시지를 입력하세요")

if 메시지 and 메시지.strip():
    # 추가
    마우스.execute(f"""
        insert into
            msg (채팅방, 보낸사람, 내용, 보낸시간)
        values
            ('{채팅방이름}','{나}','{메시지}','2026-11-24 10:18')
""")

    # 확장
    conn.commit()

# 메시지 조회하기 - 저장소에서 데이터 전부 읽어오고 마우스가 가지고 있어라!

마우스.execute(f"""
    select          -- 3. 조회
        보낸사람,
        내용,
        보낸시간
    from            -- 1. 테이블 선택
        msg
    where           -- 2. 특정  조건 확인
        채팅방 = '{채팅방이름}'

""")

# DB 에서 전부 읽었으니 파이썬 스트림릿으로 보내기
for 보낸사람, 내용, 시간 in 마우스.fetchall():
    # st.write(한건)
    아바타 = "🙋" if 보낸사람 == 나 else "👤"
    with st.chat_message(보낸사람, avatar=아바타):
        st.write(f"**{보낸사람}** {시간}")
        st.write(내용)
        


# 서비스를 만들 때 처음 실행하는 비어있는 값
# 어떻게 처리할지?
# 서비스를 처음 실행하면 테스트 데이터를(더미)
# 진짜 데이터가 들어오면 어떻게 처리할지?

# DB에서 조건에 맞는 데이터만 가져오는 명령어 - where
# 파이썬 비교 == / DB 비교 =



