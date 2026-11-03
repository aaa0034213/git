def solution(num_list):
    # 마지막 값이 직전 값보다 크면 차이를, 아니면 두 배를 추가한다.
    previous, last = num_list[-2:]
    next_number = last - previous if last > previous else last * 2
    num_list.append(next_number)
    return num_list
