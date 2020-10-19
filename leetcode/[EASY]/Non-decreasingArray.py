class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        prepre = -10 ** 5
        pre = 'not'
        
        count = 0
        
        for idx,num in enumerate(nums):
            if pre =='not':
                pre = num
            else:
                if pre > num:
                    if prepre <= num:
                        pre = prepre
                    else:
                        nums[idx] = pre
                    count += 1
                    if count > 1:
                        return False
                prepre, pre = pre, nums[idx]
                
        return True
                    