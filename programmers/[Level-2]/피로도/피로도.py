from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    def func(k, per):
        for i, dun_i in enumerate(per):
            min_k, use_k = dungeons[dun_i]
            if(min_k <= k):
                k -= use_k
            else:
                return i + 1
        return 0
    
    for per in permutations(list(range(len(dungeons)))):
        answer = max(answer, func(k, per))
        
    return answer


print(solution(80,	[[80,20],[50,40],[30,10]]	))