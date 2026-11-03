# 연속된 기록의 차이를 원래 조작 문자로 되돌린다.
MOVES = {1: "w", -1: "s", 10: "d", -10: "a"}


def solution(numLog):
    # 이웃한 기록을 짝지어 차이를 구하고 문자들을 이어 붙인다.
    return "".join(
        MOVES[current - previous]
        for previous, current in zip(numLog, numLog[1:])
    )
