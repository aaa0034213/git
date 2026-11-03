def solution(numLog):
    answer = ''

    for i in range (1, len(numLog)):
        diff = numLog[i] - numLog[i-1]

        answer += {1: 'w', -1: 's', 10: 'd', -10: 'a'}[diff]

    return answer