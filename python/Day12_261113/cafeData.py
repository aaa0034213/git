# cafeData.py

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# 1. 도구 = 카페 매출 분석하고 예측하는 프로그램

# 상황
# - 어떤 상품군에서 매출이 많이 나왔는지 보여주세요
# 기록된 매출과 반품은 얼마인가요?

# 셀제 파일에서 확인한 내용
# 날짜.시간 - 2024-01-01
# 거래 구분 - 매출 47행 / 반품 2행

# 데이터 분석 6행
# 목적 - 상품군별 금액을 확인하고 커피 수량. 금액 관계체험
# 위험 - 반품을 더하거나 행 수를 주문 수로 오해할 수있음
# 출처 - 공공데이터 확인
# 원인 - 예약일, 할인율의 빈 값, 중복 확인 필요
# 방법 - 원본 유지, 매출 반품 분리, 예측에서는 커피기록 선택
# 기록 - 

# 2. 파일 읽어오기

try:

    df = pd.read_csv("CAFE_DATA.csv")

# 구조 확인, 행과 열 확인
# 구조확인
# SALES_CD - 매출/반품 구분
# MLSFC_CD - 상품군: 커피,케이크 등
# SLE_CO - 해당 행의 수량
# PAYMENT_PRICE - 해당 행의 결제금액
# PRIPT_NO - 영수증 번호
# RESVE_DT - 예약 일시로 해석하는 열
# DSECNT_RT - 할인율로 해석하는 열

# 행 열 수 확인
    print(df.shape)

# 위에서 3개만 확인
# 어떤 크기의 파일인지 먼저확인
    #print(df.head(3))
    # 필요한 열을 눈으로 확인
    # 한 행에는 무엇이 있는지
    # 내가 필요한 열만 골라서 확인
    # 매출, 결제 금액
    print(df[["SALES_CD","MLSFC_CD","PAYMENT_PRICE"]].head(3))
    print("--------------------------------------------------")

    # 빈 값 확인
    # 데이터 분석 시 비어있으면 정확한 데이터분석 x
    print(df.isna().sum())
    print("---------------------------------------------------")

    # 중복 확인
    print("중복되는 행: ", df.duplicated().sum())
    print("---------------------------------------------------")
    
    # 매출만 확인해서 복사
    매출 = df[df["SALES_CD"] == "매출" ].copy()

    반품 = df[df["SALES_CD"] == "반품"].copy()

    # 무엇이 바뀌었고, 결과가 맞는지 확인
    print("원본 행 수:", len(df))
    print("매출 행 수:", len(매출))
    print("반품 행 수:", len(반품))
    
    # 총 매출
    총_매출 = 매출["PAYMENT_PRICE"].sum()
    # 반품액
    반품액 = 반품["PAYMENT_PRICE"].sum()
    # 순 매출 확인
    # 매출이 천단위로 표시될 수 록
    print(f"총_매출:  {총_매출:,.0f}")
    print(f"순매출:  {총_매출 - 반품액:,.0f}")
    print(f"반품액: {반품액:,.0f}")

    # 어떤 상품군에서 금액이 많이 나온지 확인
    print(매출["MLSFC_CD"].unique())

    # 같은 상품군으로 묶고 결제금액을 더해서 출력
    sum_count = 매출.groupby("MLSFC_CD")["PAYMENT_PRICE"].sum()

    # 큰 순서대로 정렬
    sum_count = sum_count.sort_values(ascending = False)
    # 데이터 타입이 안맞아 print()시 에러 발생 >> 어떤 타입이든 문자로 바꿔서 출력 to_string()
    print(sum_count.to_string())

     # 예측
    # 커피 판매기록 선택
    커피 = 매출[매출["MLSFC_CD"] == "커피"].copy()

    # 학습할 자료들 준비 : 몇 잔? 얼마인지?
    # problem = 커피[""]
    # answer = 커피[""]

    # 과거의 몇 잔 팔았는지? 
    판매수량 = 커피[["SLE_CO"]]
    # 얼마 받았지?
    결제금액 = 커피[["PAYMENT_PRICE"]]

    # model 
    model = LinearRegression()

    # 학습했으니 테스트 

    new_problem = pd.DataFrame({
        "SLE_CO": [3]
    })

    # model 학습 >> 필요한 과거 자료들을 넣어줌.
    model.fit(판매수량, 결제금액)

    # 예측
    result = model.predict(new_problem)

    print(result)

except FileNotFoundError :
    print("파일을 읽을 수 없습니다.")


# 중복 확인을 했을 때 직접 그 행을 열어서 확인 !!
# - 여러가지 조건 확인 후 삭제해도 되는지 확인 / 이유: 잘못 삭제하면 매출이 줄어들 수 있기 때문.
# 이상값 발생 시 -> 실제 행 확인 -> 처리 방법 결정
# 삭제할지, 남길지, 채울지 결정
# 매출과 반품이 함께 있을 때 처리 방법 -> 매출만 선택하고 반품은 따로 빼서 순 매출 계산
# 중복처럼 보이는 행
# - 삭제 하지 않음
# - 같은 상품을 여러 개 산 기록
# 0원행 << 삭제 하지 않음 (수량 보존)

# fact
# - 이 샘플에서는 케이크 매출 기록이 563,000원

# insight 
# - 케이크 예약이 포함된 짧은 시간대
# - 케이크 재고 더 준비

# action
# - 재고, 인력 배치 검토.

# machine learning - 예측
# 학습 방법: 학습 -> 예측 -> 검증

# 학습 fit() / 예측 predict()

# 단체 주문 커피 3잔이면 얼마쯤 나올지?

