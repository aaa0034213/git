def solution(arr, queries):
    for s, e, k in queries:
        for i in (s, e+1):
            if i % k ==0 :
                arr[i] += 1

    return arr

#---------------------------------------
# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 
# 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
#만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.


# 순서: 빈 리스트 값 만들고 l~r+1 까지 반복출력 , 숫자 정수 >> 문자형으로 형변환 한후 05 포함된 것들만 출력하게 아닌 것들은 -1 로 출력
def solution(l ,r):
    answer = []

    for i in range(l, r+1):
        if all(c in "05" for c in str(i)):
            answer.append(i)

    if len(answer) == 0:
        return [-1]

    return answer


# --------------------------------------------------------
def solution(start_num, end_numm):
    answer = []

    for i in range(start_num, end_numm +1):
        answer.append(i)

    return answer
   

#-----------------------------------------------------------

def solution(n):
    answer = []

    while n != 1:
        answer.append(n)

        if n % 2 == 0:
            n = n // 2

        else:
            n = 3*n + 1

    answer.append(1)

    return answer

# 리팩

def solution(n):

    answer = [n]

    while n != 1:
        answer.append(n)

        if n % 2 == 0:
            n = n // 2

        else:
            n = 3 * n + 1

    return answer

# 배열 만들기 4

def solution(arr):
    stk = []
    i = 0

    for i in range(1, len(arr)):
        while i < len(arr):
            if stk and stk[-1] >= arr[i]:
                stk.pop()

            else: 
                stk.append(arr[i])
                i += 1

    return stk
    
