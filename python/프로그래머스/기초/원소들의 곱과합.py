# 원소들의 곱과 합
def solution(num_list):
    multiple = 1

    for num in num_list:
        multiple *= num

    total = sum(num_list)

    if multiple < total ** 2 :
        return 1
    else:
        return 0