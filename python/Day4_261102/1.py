# 기초 문제 1.
키 = 135

if 키 < 140 :
    print("탑승 불가, 안전확인 완료")
else:
    print("탑승 가능, 안전확인 완료")


# 기초 문제 2. 

num = 5

while num > 0:
    print(num)
    num -= 1
print("발사!")

# 기초 문제 3.

진열대 = ["사과", "바나나", "포도", "딸기", "수박"]
print(진열대[0])
print(진열대[-1])
print(진열대[:3])
print(진열대[4:])
print(len(진열대))

# 기초 문제 4.
출석부 = ["민수", "지아", "도윤"]
출석부.append("서연")
출석부.remove("지아")

if "하준" not in 출석부:
    print("명단에 없습니다.")


# 중급 문제 1. 
사용한_쿠폰 = ["A100", "B200", "C300"]

쿠폰번호 = input("쿠폰 번호를 입력해주세요: ")

if 쿠폰번호 == 사용한_쿠폰:
    print("중복입니다.")

else:
    print("사용 가능한 쿠폰입니다!")
    사용한_쿠폰.append(쿠폰번호)

print(사용한_쿠폰)

# 중급 문제 2.
게시판_글 = ["글1", "글2", "글3", "글4"]
게시판_글.append("글5")
게시판_글.append("글6")
print(게시판_글)
print(len(게시판_글))
게시판_글.remove(게시판_글[0])
print(len(게시판_글))

# 심화 문제 1. 

정답_비밀번호 = "1234"
count = 0
max_count = 3

while count < max_count:
    user_input = input("비밀번호를 입력하세요.")

    if user_input == 정답_비밀번호:
        print("로그인 성공")
        break
    else:
        count += 1
        print(f"틀렸습니다 ({count}/3)")

if count == max_count:
    print("계정이 잠겼습니다.")



# 심화 실습 2.
상품목록 = []
while True:
    print("=== 위시리스트 메뉴 프로그램 ===")
    print("1. 담기 ")
    print("2. 빼기 ")
    print("0. 종료 ")

    메뉴 = int(input("메뉴 >>"))

    if 메뉴  == 1 :
        상품이름 = input("구매할 상품 입력하세요 : ")
        if 상품이름 in 상품목록:
            print("이미 담긴 상품입니다. ")
        else:
            상품목록.append(상품이름)
        print(상품목록)

    elif 메뉴 == 2 :
        상품이름 = input("삭제할 상품 입력하세요 : ")
        if 상품이름 in 상품목록:
            상품목록.remove(상품이름)
            print(상품목록)
        else:
            print("목록에 없는 상품입니다.")


    if 메뉴 == 0 :
        break

print(상품목록)
print("종료")
