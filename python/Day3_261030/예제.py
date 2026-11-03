# 예제 1.

합계 = 0
for 일 in range(1,8):
    저금 = 일 + 1000
    합계 += 저금
print("7일 저금 합계: ", 합계)


# 예제 2.

DAYIL_UNIT = 1000
total = 0
for day in range(1, 8):
    total += day * DAYIL_UNIT
print("7일 저금 합계: ", total)

print(sum(range(1,8) ) * DAYIL_UNIT)

# 예제 3.
for 번 in range(3):
    print("웅원 구호", 번 + 1)
for 이닝 in range(1, 10, 4):
    print("이닝", 이닝, "시작")


# 예제 4.
잔액 = 100
년수 = 0
while 잔액 < 200:
    잔액 = 잔액 * 11 / 10
    년수 += 1
    print("년차", 년수, "잔액", 잔액)
print("원금이 2배가 되기까지", 년수 ,"년")

# 예제 5. 
balance, target, years, MAX_YEARS = 100, 200, 0 , 100
while balance < target and years < MAX_YEARS:
    balance = balance * 11 // 10
    years += 1
print("걸린 시간", years, "년")

# 예제 6. 
필요 = 15
모은수 = 0
for 번호 in range(1, 7):
    if 번호 % 2 == 0:
        print(번호, "번 창고는 점검중, 건너뜀")
        continue
    모은수 += 번호 * 2
    print(번호, "번 창고 수량 합계:", 모은수)
    if 모은수 >= 필요:
        print("필요한 수량을 채웠어요")
        break

# 추가.

now_num = 3
my_num = 7
while True:
    print("호출 번호:", now_num)
    if now_num == my_num:
        print("my turn")
        break
    now_num += 1

