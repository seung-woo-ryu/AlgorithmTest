class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = -2**31
        maxN = -2**31
        for num in nums:
            pre = max(pre+num,num) 
            maxN = max(pre,maxN)
        return maxN