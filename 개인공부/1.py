# 공부 실습.py

from myfile import st, db, re


st.title("Kakao Coupon")

# DB 저장소 연결 및 생성
conn = db.connect("kakao.db")

# SQL 명령을 실행할 커서 객체 생성
cursor = conn.cursor()

# 회원 테이블 생성
cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        member_id    INTEGER PRIMARY KEY AUTOINCREMENT,
        username     TEXT NOT NULL UNIQUE,
        password     TEXT NOT NULL,
        name         TEXT NOT NULL,
        phone_number TEXT NOT NULL UNIQUE
    )
""")

conn.commit()

# 로그인 상태 초기화
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "current_username" not in st.session_state:
    st.session_state["current_username"] = None

if "current_name" not in st.session_state:
    st.session_state["current_name"] = None

# 로그인 후 화면
if st.session_state["logged_in"]:
    current_username = st.session_state["current_username"]
    current_name = st.session_state["current_name"]

    st.success(f"{current_name}님, 환영합니다.")
    st.write("로그인 아이디:", current_username)

    logout_button = st.button(
        "로그아웃",
        key="logout_button"
    )

    if logout_button:
        st.session_state["logged_in"] = False
        st.session_state["current_username"] = None
        st.session_state["current_name"] = None

        st.rerun()

    # 로그인 상태에서는 아래 로그인·회원가입 화면을 실행하지 않는다.
    st.stop()

# 로그인 및 회원가입 탭
login_tab, signup_tab = st.tabs(["로그인", "회원가입"])

with login_tab:
    st.subheader("로그인")

    login_username = st.text_input(
        "아이디",
        key="login_username"
    ).strip()

    login_password = st.text_input(
        "비밀번호",
        type="password",
        key="login_password"
    ).strip()

    login_button = st.button(
        "로그인",
        key="login_button"
    )

    if login_button:
        if not login_username:
            st.error("아이디를 입력해 주세요.")

        elif not login_password:
            st.error("비밀번호를 입력해 주세요.")

        else:
            cursor.execute("""
                SELECT
                    member_id,
                    username,
                    name
                FROM members
                WHERE username = ?
                AND password = ?
            """, (
                login_username,
                login_password
            ))

            member = cursor.fetchone()

            if member:
                st.session_state["logged_in"] = True
                st.session_state["current_username"] = member[1]
                st.session_state["current_name"] = member[2]

                st.rerun()

            else:
                st.error("아이디 또는 비밀번호가 일치하지 않습니다.")

with signup_tab:
    st.subheader("회원가입")

    username = st.text_input(
        "아이디",
        key="signup_username"
    ).strip()

    password = st.text_input(
        "비밀번호",
        type="password",
        key="signup_password"
    ).strip()

    name = st.text_input(
        "이름",
        key="signup_name"
    ).strip()

    phone_number = st.text_input(
        "전화번호",
        placeholder="010-1234-5678",
        key="signup_phone_number"
    ).strip()

    signup_button = st.button(
        "가입하기",
        key="signup_button"
    )

    if signup_button:
        if not username:
            st.error("아이디를 입력해 주세요.")

        elif not password:
            st.error("비밀번호를 입력해 주세요.")

        elif not name:
            st.error("이름을 입력해 주세요.")

        elif not phone_number:
            st.error("전화번호를 입력해 주세요.")

        elif len(password) < 8:
            st.error("비밀번호는 8자 이상이어야 합니다.")

        elif not re.search(r"[!@#$%^&*]", password):
            st.error("비밀번호에 특수문자가 포함되어야 합니다.")

        elif not re.fullmatch(
            r"010-[0-9]{4}-[0-9]{4}",
            phone_number
        ):
            st.error("전화번호 형식이 잘못되었습니다.")

        else:
            try:
                cursor.execute("""
                    INSERT INTO members (
                        username,
                        password,
                        name,
                        phone_number
                    )
                    VALUES (?, ?, ?, ?)
                """, (
                    username,
                    password,
                    name,
                    phone_number
                ))

                conn.commit()
                st.success("회원가입을 완료했습니다.")

            except db.IntegrityError:
                conn.rollback()
                st.error("이미 사용 중인 아이디 또는 전화번호입니다.")