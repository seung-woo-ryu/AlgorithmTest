# Hint: prefix sum

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dp = list()
        di = dict()
        
        sum = 0
        for a in A:
            sum = (sum+ a) % K
            if sum not in di:
                di[sum] = 1
            else:
                di[sum] += 1
        
        answer = 0
        
        for key in di.keys():
            answer += (di[key] * (di[key] - 1))//2 + (di[key] if key == 0 else 0 )
            
        return answer
