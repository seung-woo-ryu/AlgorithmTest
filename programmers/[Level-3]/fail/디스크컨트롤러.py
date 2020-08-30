'''
    여러 가지 case잘 살펴보기.
'''

import heapq

def solution(jobs):
    answer = 0
    now = 0
    n = len(jobs)
    heap = []
    jobs.sort()
    
    while len(heap) != 0 or len(jobs) != 0:
        if not len(heap):
            now = jobs[0][0]
            heapq.heappush(heap, [jobs[0][1],jobs[0][0]])
            jobs.remove(jobs[0])
        else:
            tmp = heapq.heappop(heap)
            now += tmp[0]
            answer += now - tmp[1]
            tmp2 = []
            for x in jobs:
                if now >= x[0]:
                    heapq.heappush(heap, [x[1],x[0]])
                    tmp2.append(x)
                else:
                    break
            for x in tmp2:
                jobs.remove(x)
        
    return answer // n

'''
    답
    def solution(jobs):
        answer = 0
        start = 0  # 현재까지 진행된 작업 시간
        length = len(jobs)

        jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

        while len(jobs) != 0:
            for i in range(len(jobs)):
                if jobs[i][0] <= start:
                    start += jobs[i][1]
                    answer += start - jobs[i][0]
                    jobs.pop(i)
                    break
                # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
                if i == len(jobs) - 1:
                    start += 1

        return answer // length
'''