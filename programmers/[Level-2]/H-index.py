def solution(citations):
    citations.sort(reverse=True)
    answer = max(list(map(min, enumerate(citations, start=1))))
    return answer