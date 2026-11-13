import streamlit as st
friend_list = ["민수","지영","철수"]

# 1. 친구 목록을 전체 출력

# 2. 몇 번째 친구를 입력할지? number_input()

# 3. 선택한 친구의 이름을 출력하시오. 있으면 출력 없으면 "그 번호의 친구는 없습니다."

st.subheader("친구 이름 찾기")

st.write("친구 목록 ", friend_list)
num_friend = st.number_input("몇 번째 친구를 입력하세요: ", value= 1)
try:
    st.write("친구 이름", friend_list[num_friend])
except IndexError as e:
    print("개발자 확인용: ", e)
    print("오류 종류", type(e).__name__)
    st.write("그 번호의 친구는 없습니다.")
