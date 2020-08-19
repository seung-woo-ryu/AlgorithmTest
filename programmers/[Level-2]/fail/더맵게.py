import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    cnt = 0

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        else:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            cnt += 1
    return cnt