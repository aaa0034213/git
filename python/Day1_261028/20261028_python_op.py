# 기초 1. 영화 관람 연령 확인
age = 17 ; po_age = 19
print(age >= po_age)    # 17 >= 19
print(age < po_age)     # 17 < 20


# 기초 2. 회원가입 비밀번호 확인
password = "abc123" ; password_check = "abc1234"
print(password == password_check)   # 같은지
print(password != password_check)   # 다른지


# 중급 1. 배달 최소 주문금액
짜장면 = 7000
짜장면_수량 = 2
탕수육 = 15000
최소_주문금액 = 20000
sum = (짜장면 * 짜장면_수량) + 탕수육

print("총 주문 금액", sum ,"원")
print(sum >= 최소_주문금액)


# 중급 2. 평균 점수 장학금 판정
korean = 80 ; math = 90 ; english = 90 ; mean = (korean + math + english)/3
print("평균: ", mean)
print("장학금 대상:" , mean >= 80)
print("장학금 대상:" , mean <= 80)


# 심화 1. 행운의 번호 이벤트

num = 727
frist_num = num // 100 
last_num = num % 10

print(f"앞자리:{frist_num}, 뒷자리:{last_num}, 당첨 여부:{frist_num == last_num}")


# 심화 2. 영상 길이 표시와 짧은 영상

총_초 = 3725
시간 = 3600
분 = 60
초 = 1
남은_초 = 총_초 - (시간 + 분 + 초)
print