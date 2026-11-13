# 파일명: dataEx.py
import pandas as pd
import streamlit as st

주문 = {
    "주문번호": [2001, 2002, 2003, 2004, 2005, 2006, 2006],
    "메뉴": ["아메리카노", "카페라떼 ", "크로플", "딸기스무디", "카페라떼", "아메리카노", "아메리카노"],
    "수량": [1, 2, 1, 99, 2, 1, 1],
    "가격": [4500, 5000, 6500, 6000, 5000, 4500, 4500],
    "결제수단": ["카드", "현금", None, "카드", "카드", None, None],
}
df = pd.DataFrame(주문)

# 빈 값, 공백 처리하기
# dropna() : 빈 값이 있는 행을 삭제!
# fillna(값) : 빈 값을 다른 값으로 채움
# 둘 다 새 표를 돌려준다. (원본은 그대로 유지)

# 주문 통계에서 결제 수단이 비어있을 때 주문을 빼버리면
# 매출이 줄어든다. 값을 채우고 매출을 유지한다.
# 전체 행 수 출력

# 전체적인 내용 확인
print(df)

# 1. 안전하게 기존 원본을 복사한다.
new_df = df.copy()

# 2. 새로운 복사된 표를 먼제 결제수단 열을 가져온다.
new_df["결제수단"] = new_df["결제수단"].fillna("미확인")


# # 추가 코드
# def 결제수단_채우기(df):
#     new_df = df.copy
#     new_df["결제수단"] = new_df["결제수단"].fillna("미확인")
#     return new_df

# print(결제수단_채우기(df)["결제수단"].to_list)
# print(df["결제수단"].isna().sum())

# 3. 확인
print(new_df)
# -------------------------------------------------------

st.title("데이터 분석")
st.header("카페 주문 데이터")
# 원본 데이터 출력
st.data_editor(df)
st.write("전체 행 수 :", len(df))

st.subheader("빈 값 처리된 결과")
st.data_editor(new_df)
st.write("처리 후 행 수", len(new_df))

# --------------------------------------------------------
# 중복 제거
# duplicated - 중복인지 확인
# drop_duplicates - 중복값 제거 (확인 후 제거)

# 모든 열이 같은 중복 행 확인
# 웹 화면에 소주제 보여줘
st.subheader("중복 확인")
# streamlit True,False 타입 Bool
# st.write(new_df.duplicated())

print(new_df.duplicated())
# 중복 확인 개수 세기
print("중복확인", new_df.duplicated().sum())

# 중복 제거
print("중복 제거", new_df.drop_duplicates())

print(df)
print(new_df)


# 위에서 아래로 가며 행마다 "앞에 모든 열이 똑같은 행이 있었다"
# 처음나온 행 False 두 번째 True 비교하고 다르면 False

# 자주 사용하는 옵션
# 주문 번호가 같으면 중복
df.drop_duplicates(subset = ["결제수단"])

# 마지막 것만 남기는 옵션
df.drop_duplicates(keep = "last")

# 중복되는 행을 전부 삭제
df.drop_duplicates(keep = False)

# 코드를 작성하는 순서
# 1. 중복확인 duplicated()
# 2. .sum() 중복되는 개수 세기
# 3. drop_duplicates() 중복 제거
# 4. 기존 길이와 중복 제거된 개수 비교, 확인

# ------------------------------------------------------------

# 공백 지우기
# - 공백 때문에 세어지는 값 // 불필요한 값들 

주문 = {
    "주문번호": [2001, 2002, 2003, 2004, 2005, 2006, 2006],
    "메뉴": ["아메리카노", "카페라떼 ", "크로플", "딸기스무디", "카페라떼", "아메리카노", "아메리카노"],
    "수량": [1, 2, 1, 99, 2, 1, 1],
    "가격": [4500, 5000, 6500, 6000, 5000, 4500, 4500],
    "결제수단": ["카드", "현금", None, "카드", "카드", None, None],
}
df = pd.DataFrame(주문)

new_df = df.copy()
# 공백 제거할 때 사용하는 기능
# 1. 어떤 열 선택? 메뉴
# 2. strip() : 앞, 뒤 공백만 제거. (글자 열에만 사용)

# 문제점
# - 공백이 있으면 같은 이름이라고 해도 다르게 세어질 수 있음

print(new_df["메뉴"].str.strip())

# 공백이 제거 되었는지 모를 때 확인 방법
# value_counts() 값 별로 개수 센다.
# 열에 들어있는 메뉴 이름 하나 하나 셈

print(new_df["메뉴"].value_counts())

print(new_df["메뉴"].str.strip().value_counts())

