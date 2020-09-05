import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    heap = []
    
    for value in works:
        heapq.heappush(heap,(-value,value))

    for _ in range(n):
        new_value = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-new_value, new_value))
    
    return sum(map(lambda x: x[0]**2, heap))