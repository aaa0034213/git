# 간단한 논리 연산

def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)

   
# 주사위 게임 3

# 주사위 4개 숫자 같은시 p * 1111
# 주사위 3개 숫자 = p / 나머지 q / (10*p+q)
# 두 주사위에서 나온 숫자 2개 = p  나머지 주사위 다른 숫자 p,q  = p*q
# 주사위 모드 다를 시 숫자 가장 작은 숫자만큼 점수 얻음



def solution(a, b , c, d):
    dice = sorted([a,b,c,d])

    if dice[0] == dice[3]:
        return dice[0] * 1111

    elif dice[0] == dice[2]:
        return (10*(dice[0] + dice[3])) **2

    elif dice[1] == dice[3]:
        return (10*(dice[1] + dice[3])) **2

    elif dice[0] == dice[1] and dice[2] == dice[3]:
        return (dice[0] +dice[2]) * abs(dice[0] - dice[2])

    elif dice[0] == dice[1]:
        return dice[2] * dice[3]

    elif dice[1] == dice[2]:
        return dice[0] * dice[3]

    elif dice[2] == dice[3]:
        return dice[0] * dice[1]

    else:
        return dice[0]

# 글자 이어 붙여 문자열 배치
def solution(my_string, index_list):
    answer = ''

    for i in index_list:
        answer += my_string[i]

    return answer

# 9로 나눈 나머지

def solution(number):

    answer = 0

    for i in number:
        answer += number(i)

    return answer % 9 

# 문자열 여러 번 뒤집기

def solution(my_string, queries):
    answer = list(my_string)    # 문자 리스트로 바꿔 순서 변경

    for s,e in queries:
        answer[s:e+1] = answer[s:e+1][::-1]

    return answer


