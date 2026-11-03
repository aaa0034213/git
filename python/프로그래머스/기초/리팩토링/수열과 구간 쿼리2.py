def solution(arr, queries):
    results = []
    for start, end, threshold in queries:
        # 지정된 구간에서 기준값보다 큰 원소만 후보로 삼는다.
        candidates = (value for value in arr[start : end + 1] if value > threshold)
        # 후보가 없으면 -1을 기록한다.
        results.append(min(candidates, default=-1))
    return results
