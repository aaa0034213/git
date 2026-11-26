#2_채팅목록.py
#  - 카카오톡 채팅목록

import streamlit as st
import sqlite3 as db

#데이테비이스 연결
db저장소 = db.connect("kakao.db")
마우스 = db저장소.cursor()

# 채팅방 테이블
#  - 방이름 비어 있으면 안된다
#  - 방이름 겹치면 안된다!
#  - 채팅방을 구별할 수있는 번호!(primary key)
#   자동으로 숫자가 증가될 수있도록 설정

# 데이터가 정확해야된다.
# 이상한 데이터를 들어오지 못하게 막는 규칙(제약조건)
# 무결성
마우스.execute("""
    create table if not exists rooms(
        방번호  integer  primary key  autoincrement,
        방이름  text     not null  unique
    )
""")

# 로그인 안하고 바로 들어온 사람대비
if "로그인한유저" not in st.session_state:
    st.session_state["로그인한유저"] = None

st.title("채팅방 목록")

회원 = st.session_state["로그인한유저"]

if 회원 == None:
    st.title("카카오 채팅방")
    st.write("로그인 부터 하세요!")
    st.page_link("main.py",label="로그인하러 가기")

else:
    st.write(회원)

    #누구의 목록인지 (회원 이름)
    st.write(f"**{회원[3]}**님의 채팅 목록")

    # 새 채팅방 입력
    새방 = st.text_input("새 채팅방 이름:").strip()

    # 방 만들기
    if st.button("방 만들기"):
        # 확인: 빈 이름?
        if 새방 == "":
            st.warning("방 이름을 입력하세요!")
        else:
            # 확인 select 이미 있는 방인가?
            마우스.execute(f"""
                select
                    *
                from
                    rooms
                where
                    방이름 = '{새방}'
            """)
            결과 = 마우스.fetchone()

            if 결과 != None:
                # 채팅방이 이미 있다.
                st.warning("이미 있는 방이예요!")
            else:
                # 저장 : 새방 추가
                # insert 추가 되는 순간 autoincrement
                # 동작한다.
                # 개발자들이 직접 번호를 넣으면 중복될 수 있음

                마우스.execute(f"""
                    insert into
                        rooms (방이름)
                    values
                        ('{새방}')
                """)

                #확정
                db저장소.commit()

                #새로고침(새로 추가된 내용이 안보임)
                st.rerun()

    # 조회: 방 목록을 DB에서 가져오기
    # 순서
    # 1. 내 채팅방 목록(DB조회)
    마우스.execute("""
        select
              *
        from
            rooms
    """)
    # 2. 하나씩 목록을 출력(화면)
    방목록 = 마우스.fetchall() # [(값1,),(값2)] 형태로 돌아온다

    # 3. 확인: 방이 하나도 없나?
    if len(방목록) == 0:
        st.info("아직 채팅방이 없어요! 위에서 방을 만들어 보세요")

    #4. 출력 : 방 하나
    for 줄 in 방목록:
        방 = 줄[1]   # 방 이름을 꺼내라
        st.write(방)

        # 박스
        with st.container(border=True):
            st.write(f"**{방}**")

            # key 설정 이유: streamlit 버틀 구별하기 위해서 사용
            if st.button("입장", key=방):
                st.session_state["채팅방"] = 방
                st.switch_page("pages/3_채팅방.py")

# page_link() 우리가 직접 클릭을 했다
# switch_page()  코드가 실행되면 자동으로
#                다른 페이지로 이동한다

# 클릭한 채팅방에 메시지들만 보이게 하겠다
# 세션(session)
#  - 웹 페이지들끼리 데이터를 공유하기 위해서 사용하는
#    개념
# 스트림릿에서는 session(접속한 동안)_state(상태)
#  딕셔너리로 되어있다
# key를 이용해서 value을 저장한다.