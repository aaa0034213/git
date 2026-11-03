# list3.py

# 고객 추가 프로그램 만들기
# -- 고객 추가 프로그램입니다 --
# 1. 고객 추가
# 2. 고객 삭제
# 3. 종료
# 메뉴 >
# 0 누르지 않으면 프로그램 계속 실행

#-------------------------------------

고객이름목록 = []
while True:

    print("---- 고객 추가 프로그램 -----")
    print("1. 고객 추가")
    print("2. 고객 삭제")
    print("0. 종료")
    print("메뉴 >")

    메뉴 = int(input())

    if 메뉴 == 1 :
        이름 = input("추가할 고객 이름 입력: ")
        고객이름목록.append(이름)
        print(고객이름목록)

    elif 메뉴 == 2 :
        이름 = input("삭제할 고객 이름 입력: ")
        if 이름 in 고객이름목록:
            고객이름목록.remove(이름)
        print(고객이름목록)

    # 멈추는 조건 넣기
    if 메뉴 == 0:
        break
print(고객이름목록)
print("종료")



상품목록 = []

while True:
    print("\n=== 위시리스트 메뉴 프로그램 ===")
    print("1. 담기")
    print("2. 빼기")
    print("0. 종료")

    try:
        메뉴 = int(input("메뉴 >> "))
    except ValueError:
        print("숫자를 입력해주세요.")
        continue

    if 메뉴 == 0:
        break

    elif 메뉴 == 1:
        상품이름 = input("구매할 상품 입력하세요 : ").strip()

        if not 상품이름:
            print("상품명을 입력해주세요.")
        elif 상품이름 in 상품목록:
            print("이미 담긴 상품입니다.")
        else:
            상품목록.append(상품이름)
            print("상품이 추가되었습니다.")

    elif 메뉴 == 2:
        상품이름 = input("삭제할 상품 입력하세요 : ").strip()

        if 상품이름 in 상품목록:
            상품목록.remove(상품이름)
            print("상품이 삭제되었습니다.")
        else:
            print("목록에 없는 상품입니다.")

    else:
        print("올바른 메뉴를 선택해주세요.")

    print("현재 상품목록 :", 상품목록)

print("\n최종 상품목록 :", 상품목록)
print("종료")
