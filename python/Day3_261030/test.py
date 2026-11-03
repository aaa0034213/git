

# passward = int(input("비밀번호를 입력하세요: "))

# while True:

#     if passward == 1234:
#         print("비밀번호가 맞습니다.")

#     elif 틀린횟수 == 5:
#         print("10분뒤 다시 실행하세요")
#         break

#     else:
#         print("비밀번호를 다시 입력하세요.")
#         틀린횟수 += 1
#         print("틀린횟수 :" , 틀린횟수)

# ---------------------------------------------------------------
for i in range(5):
    if int(input("비밀번호 입력")) == 1234:
        print("비밀번호 맞음")
        break
        print("틀린횟수", i+1)
    else:
        print("다시입력")
        

#---------------------------------------------------------------

count = 0

while count < 5:
    passward = int(input("비밀번호를 입력하세요: "))

    if passward == 1234:
        print("비밀번호 맞습니다")
        break

    else:
        count += 1
        print("비밀번호를 다시 입력하세요.")
        print("틀린 횟수: ", count)

if count == 5:
    print("10분뒤 다시 실행")



def password():
    for i in range(5):
        if input("비밀번호: ") == "1234":
            print("비밀번호가 맞습니다.")
            return

        print("비밀번호가 틀렸습니다.", i + 1, "회")

    print("10분 뒤 다시 실행하세요.")

password()

