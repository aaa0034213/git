# pagelink.py

# 모든 서비스의 기본 기능 4가지
#  - CRUD
#  - Create (만들기)
#  - Read (읽기)
#  - Upate (고치기)
#  - Delete ( 지우기 )

# 페이지이동
# - 페이지(page) + 연결(link)
# -  누르면 다른 페이지로 가는 링크!

import streamlit as st

st.title("1번 페이지")

# page_link("페이지 경로")
# 현재 실행중인 pagelink.py 위치를 기준으로 경로를 찾는다()
# streamlit으로 여러 페이지 이동 시키고 싶을 경우에 pages 폴더를 만든다. pages 이름 지정!
# 파이썬 파일 이름은 자유롭게 지정 가능 / 폴더만 pages 고정

st.page_link("pages/second.py", label= "2번 페이지로 가기" , icon = "🚕")

# 현제 페이지에서 로그인한 아이디를 2번 페이지로 이동
# 로그인 아이디 변수는 현재 파일에서만 사용 가능
# 다른 페이지로 이동 불가능!

# session - 내가 사이트에 들어와있는 동안 나를 기억해주는 것
# - 사이트들끼리 정보 공유

# session_state()
# - session(접속해있는동안) + state(상태)
# - 페이지를 이동해도 지워지지 않은 상자 (딕셔너리)
# - key, value 로 구성


로그인아이디 = "eryna"

# 세선 저장
st.session_state["로그인아이디"] = "eryna"
st.session_state["이름"] = "이서희"

# 로그인 시 id, 전화번호, 이메일, 이름 -> 한번에 넘기려면 딕셔너리로 만들어서 생성 

st.write(로그인아이디)



