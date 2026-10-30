# 예제 5-1.

합산 = 0
응원 = 0
챕터 = 0

for 양 in range(1,5):
    총페이지 = 양 * 50
    합산 += 총페이지
print(합산)

for 웅원 in range(1, 3):
    print("응원 ", 응원)

for 챕터 in range(2,7,4):
    print("챕터 ", 챕터)

# 예제 5-2.

개월 = 0
구독자 = 100

while 구독자 < 1000:
    구독자 = 구독자 * 3//2 
    개월 += 1
    print(f"개월: {개월} 구독자수: {구독자}")


# 예제 5-3.

일수 , 총_시간 = 0, 0
for 일 in range(1, 11):
    if 일 % 3 == 0:
        continue

    일수 += 1
    총_시간 += 일 * 5

print(일수, 총_시간)


# 예제 5-4.
일수 , 저금통_금액 = 0, 0
while True:
    if 저금통_금액 >= 10000:
        break
    저금통_금액 += 700
    일수 += 1

print(일수, 저금통_금액)


# 예제 5-5.
빈_좌석수 = 0
for i in range(1,4):
    for j in range(1,5):
        if i == 2 and j == 3 or i == 3 and j == 1:
            continue

        빈_좌석수 += 1

print("빈 좌석수 : ", 빈_좌석수)


# 예제 5-6.
answer = 37
max_value = 100
min_value = 1
attempt = 0

while True:
    attempt += 1
    guess = (max_value + min_value) // 2    # 가운데 값 만들기

    if guess > answer:
        print(f"시도 {attempt} 추측 {guess} 너무 커요")
        max_value = guess - 1

    elif guess < answer:
        print(f"시도 {attempt} 추측 {guess} 너무 작아요")
        min_value = guess + 1

    else:
        print(f"시도 {attempt} 추측 {guess} 정답!")
        break

