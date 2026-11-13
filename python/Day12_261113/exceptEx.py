# exceptEx.py
# 예외 처리 - 프로그램이 에러가 나도 죽지 않게 막고, 에러가 무엇인지 알아내는 방법
# - 비정상적인 종료 막기
# 실생활 - 에어백 같은 역할을 함. 멀티탭 (차단기)

# try
# 문제가 발생할 수 있는 코드들!
# except
# 에러나 예외가 발생하면 처리할 수 있는 코드들!


# try:
    
#     age = int(input("나이를 입력하세요: "))
    
#     if age > 19 :
#         print("성인")
#     else:
#         print("청소년")

# except:
#     print("에러발생!")

# print("정상종료!")

# 웹 사이트 만들 시 -> 도구들 가져오기(포함하기) 
import streamlit as st

# st.title("예외처리")
# st.header("try-except")

# st.subheader("나이를 입력받아서 내년 나이 출력하세요!")

# try:

#     age = st.text_input("나이를 입력하세요: ")  # text_input() 모든 데이터 문자로 옴

#     age = int(age)
#     st.write("내년엔", age + 1 , "살")

# except ValueError as e: # 발생한 에러에 대한 내용을 e 변수에 저장한다
#     print("개발자 확인용: ", e)     # 개발자가 확인하는 용도 
#     st.write("문자가 아니라 숫자를 입력해주세요! ")  # 고객한테 쉽게 바꿔 보여주기위한 용도

# 리팩토링
# 함수는 하나의 기능만 함

# def to_age(나이):
#     try:
#         return int(나이)
#     except ValueError as e:
#         # 개발자가 에러를 직접 작성해서 보여주기 raise
    
#         print("변환 실패: ", e)
#         return None

# 나이 = st.text_input("나이를 입력하세요: ")

# if 나이 == "":
#     st.write("나이를 입력하세요")
# else:
#     나이 = to_age(나이)

#     if 나이 is None:
#         st.write("문자가 아니라 숫자로 입력하세요.")
#     else:
#         st.write("내년엔", 나이 + 1, "살")


#-------------------------------------------------------------------------------------------------------
# 주문 평균 금액
# 오늘 하루의 주문 평균을 계산해서 화면에 보여주는 간단한 코드

st.subheader("주문 평균 금액")
try:
    total_sum = st.number_input("총 매출: ", value = 1000000)     # value 설정은 기본값 설정
    order_num = st.number_input("주문 건수: ", value = 100)

    st.write("평균: ", total_sum / order_num , "원")

except ZeroDivisionError as e:
    print("개발자 확인용: ", e)
    print("에러 종류: ", type(e).__name__)      # 에러 타입 종류 보는 키워드 type().__name__
    st.write("현재 에러 발생중입니다. 곧 해결하겠습니다.")

# 리팩토링

import streamlit as st
import logging

logging
def get_average(total, count):
    if count < 1:
        return 0 


#-------------------------------------------------------------------------------------------------
# 친구 이름 찾기

friend_list = ["민수","지영","철수"]

# 1. 친구 목록을 전체 출력

# 2. 몇 번째 친구를 입력할지? number_input()

# 3. 선택한 친구의 이름을 출력하시오. 있으면 출력 없으면 "그 번호의 친구는 없습니다."

st.subheader("친구 이름 찾기")

st.write("친구 목록 ", friend_list)
num_friend = st.number_input("몇 번째 친구를 입력하세요: ", value= 2, step=1)
try:
    st.write("친구 이름", friend_list[num_friend])
except IndexError as e:
    print("개발자 확인용: ", e)
    print("오류 종류", type(e).__name__)
    st.write("그 번호의 친구는 없습니다.")


# 함수 리팩토링

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

# result = find_friend(friend_list, num_friend)

# st.write("결과:", result)

