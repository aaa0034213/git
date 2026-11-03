def soultion(a, d, included):
    answer = 0                           # answer = 0 인 변수를 생성한 후

    for i in range(len(included)):       # 길이만큼 순환을 돌고
        if included[i]== True:           # True 일 경우 등차수열 값 True 
            answer += a + d * i          # 결과 저장


    return answer

