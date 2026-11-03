from math import prod


def solution(num_list):
    # 원소의 곱이 원소 합의 제곱보다 작으면 1, 아니면 0이다.
    return int(prod(num_list) < sum(num_list) ** 2)
