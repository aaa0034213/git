# kakaocoupon.py

import my
from my import db,st

my.st.title("쿠폰 보내기")

conn = my.db.connect("kakao.db")

db조작 = conn.cursor()


# 로그인이 되어있니? 친구목록 조회해야하므로 로그인 확인
my.st.subheader("로그인 실습")
로그인탭, 가입탭 = my.st.tabs(["로그인", "회원가입"])

# 로그인 탭을 누르면 로그인 할 수 있는 화면
with 로그인탭:
    id = st.text_input("아이디", key = "로그인_아이디").strip()
    password = st.text_input("비밀번호", type = "password", key="로그인_비번").strip()

    # DB 조회
    db조작.execute(f"""
        SELECT
            *
        FROM
            members
        WHERE
            id = '{id}' AND
            password = '{password}'

    """)
    
    회원 = db조작.fetchone()

    if 회원 == None:
        my.st.warning("아이디 or 비번을 확인해주세요")

    # elif 회원[2] != password:
    #     st.warning("비밀번호가")

    else:
        st.write("찾은 아이디:", 회원)
    # my.st.write("전화번호:", 회원[4])
        # 채팅방 페이지로 회원정보 이동! 세션
        st.session_state["로그인한유저"] = 회원
        # 채팅방 이동
        st.page_link("pages/database.py", label = "채팅방 이동")

    


# 가입 탭을 누르면 가입창이 뜬다
with 가입탭:
    pass


# 파이선에서 데이터를 가져올 때 - 튜플(tuple)  = 리스트랑 똑같이 여러 개 저장
# - 0번부터 데이터를 1씩 증가시키면서 저장 
# - (값1, 값2, ... ) 괄호 
# - 튜플은 한번 데이터가 저장되면 수정, 삭제 불가

# 마우스.fetchone() - DB 에서 한 줄의 결과 (row)
# 마우스.fetchall() - Db 에서 여러 줄의 결과 (columns)


# (1, qwer, qwer, 김철수, 010-1111-1111)
    # if 회원[2] == 내가입력한비밀번호:
    #     st.success("로그인성공")
    # else:
    #     st.error("로그인에 실패하였습니다")

    # if 문을 직접 작성하다가 오류를 일으킬 수 있다.

# StreamlitPageNotFoundError (404)  
# 스트림릿 동작 방법이 실제 웹 페이지랑 조금 다름










# db조작.execute("""
#     create table if not exists coupons(
#         선물번호        integer     primary key autoincrement , 
#         spend_id       text        not null,
#         revier_id      text        not null,
#         phone_num      text        not null,
#         gift_name      text        not null,
#         coupon_num     text        not null     unique,
#         
#     )
# """)

# st.title("kakao 선물하기")
# spend_id = st.text_input("spend_id").strip()
# revier_id = st.text_input("revier_id").strip()
# phone_num = st.text_input("phone_num (ex: 010-1111-1111)").strip()
# gift_name = st.text_input("gift_name").strip()
# coupon_num = st.text_input("coupon_num").strip()

