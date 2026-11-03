def solution(a, d, included):
    # 선택된 위치의 항(a + d × 위치)만 합산한다.
    return sum(a + d * index for index, selected in enumerate(included) if selected == True)


# 기존 코드의 오타가 포함된 함수명으로 호출하는 경우도 지원한다.
soultion = solution
