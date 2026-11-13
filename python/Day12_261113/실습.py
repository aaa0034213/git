# import streamlit as st

# def find_friend(friends, num):
#     try:
#         return friends[num - 1]

#     except IndexError as e:
#         print("개발자 확인용", e)
#         print("오류 종류: ", type(e).__name__)
#         return "그 번호의 친구는 없습니다."


# friend_list = ["민수", "지영", "철수"]

# st.subheader("친구 이름 찾기")
# st.write("친구 이름 목록", friend_list)

# my_friend = st.number_input("몇 번째 친구를 입력하세요: ", min_value= 1, step =1)

# result = find_friend(friend_list, my_friend)

# st.write("결과:", result)

# 리팩토링
import streamlit as st

def find_friend(friends, num):
    try:
        return friends[num - 1]
    except IndexError as e:
        print("개발자 확인용", e)
        print("오류 종류:", type(e).__name__)
        return None


friend_list = ["민수", "지영", "철수"]

st.subheader("친구 이름 찾기")
st.write("친구 이름 목록", friend_list)

my_friend = st.number_input(
    "몇 번째 친구를 입력하세요:",
    min_value=1,
    value=1,
    step=1,
)

result = find_friend(friend_list, int(my_friend))

if result is None:
    st.error("그 번호의 친구는 없습니다.")
else:
    st.success(f"결과: {result}")