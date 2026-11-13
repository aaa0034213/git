# 배열 만들기 5

def solution(intStrs, k, s, l):
    answer = []

    for num in intStrs:
        values = int(num[s:s+l])

        if values > k:
            answer.append(values)
    
    return answer

# ----------------------------------

# 부분 문자열 이어 붙이기 문자열 만들기

def solution(my_strings, parts):
    answer = ''

    for i in range(len(my_strings)):
        s = parts[i][0]
        e = parts[i][1]

        answer += my_strings[i][s:e+1]
        
    return answer

# --------------------------------------

# 문자열 뒤에 n 글자

def solution(my_string, n):
    answer = my_string[-n:]
    return answer

# --------------------------------------

# 접미사 배열

def solution(my_string):
    answer = []

    for i in range(len(my_string)):
        answer.append(my_string[i:])

    answer.sort()

    return answer

# ----------------------------------------

# 접미사인지 확인하기

def solution(my_string, is_sufflx):
    if my_string[-len(is_sufflx):] == is_sufflx:
        return 1
    else:
        return 0