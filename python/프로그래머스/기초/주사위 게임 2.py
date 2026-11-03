# 주사위 게임 2

def solution (a, b, c):
    answer = 0
    if a == b == c : 
        return (a+b+c)*(a**2+b**2+c**2)*(a**3 + b**3 + c**3)

    elif a == b or b == c or c == a:
        return ( a + b + c ) * ( a**2 + b **2 + c **2)

    else:
        return a + b + c


    return answer

# 리팩토링

def solution(a, b, c):
    nums = [a, b, c]
    count = 4 - len(set(nums))          # set() 함수 : 중복 제거

    answer = 1

    for i in range(1, count + 1):
        answer *= sum(x**i for x in nums)

    return answer