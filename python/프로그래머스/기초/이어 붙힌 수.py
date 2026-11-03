# 이어 붙힌 수

def solution(num_list):
    홀수 = ""
    짝수 = ""

    for num in num_list:
        if num % 2 == 0 :
            짝수 += str(num)        # 문자열로 해야 짝수들의 값을 이어붙힐 수 있다

        else:
            홀수 += str(num)        # 이와 동일

    return int(홀수) + int(짝수)     # 홀수 값 짝수 값 더해야하므로 int로 바꿔 계산