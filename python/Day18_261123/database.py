# database.py

# python
# - sqlite3 (데이터 저장하는 도구) - 컴퓨터가 종료되도 데이터가 남아있음.
# - DB (DATABASE) - Data 자료, Base 기초, 기반
# - 정리해 둔 기록


# 이름들 = []

# print("시작하고 나서 이름들: ", 이름들)
# 이름 = input("이름을 입력하세요?")

# 이름들.append(이름)
# print("입력 후 이름들: ", 이름들)

# 파일을 실행하면 도구들을 가져옴
# 여러 사람이 함께 쓸 수 있도록 데이터를 정리해서
# 영구적인 곳!
# - 실시간으로 데이터 수정, 삭제 등 추가도 마음대로 할 수 있도록 만든 프로그램
# 데이터를 관리해주는 프로그램(DBMS)

import sqlite3 as db    # 저장소
import streamlit as st  # 웹 화면

# data 를 기반으로 저장할 수 있는 공간 만들기

con = db.connect("검색어.db" )

# DB 공간을 조작할 수 있는 커서
control = con.cursor()

# 데이터를 저장하려면 어떤 기록을 저장할지 미리 알려줘야함
# table (표 형식)
# 사용 키워드 (명령어) - create table table명 (테이블 생성 명령어)
# - 첫 번쨰 실행을 할 대 이미 DB한테 table 만듦
# - 두 번째 실행은 테이블이 이미 있는데 또 만들리고 하니 에러 발생
# - if not exists   

control.execute(""" 
    create table if not exists searchlist (
        message text 
    )
""")





# 네이버, 구글에서 검색한 기록을 저장하는 프로그램
# 검색어목록 = []

st.title("검색어 저장하는 DB 보기")
st.write() 

# 입력창에 입력을 하다 보면 공백이 생길 수 있음. 아예 입력받을 때 공백 제거하는 기능 strip()
검색어 = st.text_input("검색어").strip()

# 버튼을 눌렀을 때 검색어를 searchlist 테이블에 저장
# insert into table명   values 값

# 검색이라는 버튼을 눌렀을 때 비어잇는 값은 저장 안함.

# python 은 if 변수가 만나게 되면 값이 있다면 True 없으면 False

if st.button("검색"):
    if 검색어:

        control.execute(f"""
            insert into searchlist
            values ('{검색어}')

""")
        st.success(f"{검색어} 저장 완료!")

    # 한번 더 저장 (지워지지 않게 저장)
        con.commit()      

    else:
        st.warning

# DB 저장하고 수정하고 제일 마지막에는 닫아야한다
con.close()
# st.write("시작하고 검색어 목록보기")

#     검색어목록.append(검색어)

# st.write("끝나고 검색어 목록보기")
# st.write(검색어목록)


