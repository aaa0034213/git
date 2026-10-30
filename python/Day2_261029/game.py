# 게임 만들기 

정답 = 8

# 1. 숫자 입력!

# 2. 비교
# 정답보다 크면 up 작으면 down
result = []
game_num = int(input("숫자를 입력하세요."))

if game_num > 정답 :
    result = "up"
else:
    result = "down"

print(result)