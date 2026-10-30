# 실습 1
심박수 = 150
걸음수 = 6000

if 심박수 >= 140:
    print("심박수가 높습니다\n""잠시 쉬어가세요")
print("측정 종료")

if 걸음수 <= 8000:
    print("목표까지 힘내요")


# 실습 2

전기_사용량 = 320

if 전기_사용량 >= 400:
    메세지= "고지서 확인"
elif 전기_사용량 >= 300:
    메세지= "누진 구간에 들어갔어어요."
elif 전기_사용량 >= 200:
    메세지= "평균 수준입니다."
else:
    메세지= "절약중 이에요"

print(메세지)


# 응용 문제. 1

남은_일수 = 2
천재_지변 = False 

if 남은_일수 >= 3 or 천재_지변:
    print("전액 환불")
elif 남은_일수 >= 1:
    print("50%환불")
else:
    print("환불 불가")


# 응용 문제 2.

passward = 7931
a_passward = int(input("비밀번호 입력 :"))
fail_num = 3

if (fail_num >= 3 ):
    print("잠금 상태입니다.")
elif (passward == a_passward):
    print("열림")
else:
    print("안내")


# 심화 문제 1.

출석률 = 80 ; 과제 = 6 ; 시험 = 90

if (출석률 < 80):
    학생 = "수료 불가 (출석미달)"
elif (시험 >= 90 and 과제 >= 9):
    학생 = "우수 수료"
elif (시험 >= 60 and 과제 >= 7):
    학생 = "수료"
else:
    학생 = "수료 불가 (성적 미달)"

print(학생)


# 문제 2.
나 = str(input("가위바위보 입력하세요."))
너 = str(input("가위바위보 입력하세요"))

선택지 = ["가위", "바위", "보"]

if 나 not in 선택지 or 너 not in 선택지:
    result = "잘못된 선택입니다."

if (나 == 너):
    result = "비겼습니다."
elif (나 == "가위" and 너 == "보") or (나 == "주먹" and 너 =="가위") or (나=="보" and 너 == "주먹"):
    result = "이겼습니다."
else:
    result = "졌습니다"

print(result)
    