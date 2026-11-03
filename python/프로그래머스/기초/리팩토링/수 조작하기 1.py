# 각 조작 문자에 대응하는 숫자 변화량이다.
MOVES = {"w": 1, "s": -1, "d": 10, "a": -10}


def solution(n, control):
    # 명령을 순서대로 적용해 최종 값을 구한다.
    for command in control:
        n += MOVES[command]
    return n
