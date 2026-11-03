def solution(num_list):
    # 홀수와 짝수를 각각 입력 순서대로 문자열로 이어 붙인다.
    odd_numbers = "".join(str(number) for number in num_list if number % 2)
    even_numbers = "".join(str(number) for number in num_list if number % 2 == 0)
    # 두 문자열을 정수로 바꾼 뒤 더한다.
    return int(odd_numbers) + int(even_numbers)
