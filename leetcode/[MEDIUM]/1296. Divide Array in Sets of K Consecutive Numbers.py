class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        
        di = dict()
        
        for n in nums:
            di[n] = (1 if n not in di else di[n] + 1)
        
        preNum = 0
        for idx in sorted(di.keys()):
            v = di[idx]
            if v:
                for offset in range(1,k):
                    if idx + offset not in di:
                        return False
                    if di[idx + offset] < v:
                        return False
                    else:
                        di[idx+offset] -= v
        return True
                    
            
            
            