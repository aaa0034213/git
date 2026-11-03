def solution(a, b, c):
    dice = (a, b, c)
    # 서로 다른 눈이 3, 2, 1개일 때 각각 1, 2, 3차 합까지 곱한다.
    matching_groups = 4 - len(set(dice))
    score = 1
    # 각 차수의 거듭제곱 합을 점수에 누적한다.
    for power in range(1, matching_groups + 1):
        score *= sum(number**power for number in dice)
    return score
