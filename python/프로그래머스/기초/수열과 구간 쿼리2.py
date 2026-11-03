def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]

    return arr


# ---------------------------------------------------------------


def solution(arr, queries):
    brr = []

    for s,e,k in queries:
        minimum = -1

        for i in range (s, e + 1):
            if arr[i] > k :
                if minimum == -1 or arr[i] < minimum:
                    minimum = arr[i]

        brr.append(minimum)

    return brr

    
#-------------------------------------------------------------
# 리팩토링
def solution(arr, queries):
    answer = []

    for start, end, threshold in queries:
        smallest = None

        for index in range(start, end + 1):
            value = arr[index]

            if value <= threshold:
                continue

            if smallest is None or value < smallest:
                smallest = value

        answer.append(smallest if smallest is not None else -1)

    return answer