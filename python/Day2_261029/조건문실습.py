# 놀이동산 입장 프로그램
# 뱐수 나이, 시간, 주말, vip
# 나이 제한, 시간 제한, 주말인지 아닌지, vip인지 아닌지

age = int(input("현재 나이를 입력해주세요: "))
time = int(input("현재 시간을 입력해주세요: "))
week = input("주말이신가요? (y/n)")
vip = input("vip신가요? (y/n)")

print("\n------ 놀이동산 입장 안내 ---------\n")

if age < 0:
    print("잘못된 나이입니다.")

elif time < 0 or time > 22:
    print("잘못된 시간입니다. 시간을 다시 입력해주세요.")

elif week != "y" and week != "n":
    print("정보를 다시 입력해주세요. ")

elif vip != "y" and week != "n":
    print("vip 정보를 다시 입력해주세요.")

elif time < 10:
    print("아직 놀이동산 입장시간이 아닙니다.")
    print("오전 10시부터 입장 가능합니다.")

elif time >= 21:
    print("놀이동산 운영이 종료되었습니다. 다음에 또 이용해주새요. ")
    print("오후 9시 이후에는 입장 불가입니다.")


elif age < 5 :
    print("5세 미만은 입장할 수 없습니다.")


else:
    print("놀이동산 입장 가능합니다.")

    if age <= 18:
        print("청소년입니다.")

    elif age < 65:
        print("성인입니다.")

    else:
        print("65세 이상 입장객입니다.")

    if vip == "y":
        print("vip님 환영합니다! vip 혜택을 사용하실 수 있습니다!")

    else:
        print("일반 입장객입니다.")

    if week == "y":
        print("주말 특별 이벤트가 진행중입니다. 참여해보세요!")

    else:
        print("평일에는 이벤트가 진행하지 않습니다. ")

print("\n--------안내종료--------------\n")


