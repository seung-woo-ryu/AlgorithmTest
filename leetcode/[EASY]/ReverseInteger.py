class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1]) if x >= 0 else int(str(x)[-1:0:-1]) * -1
        
        if -2**31 <= x and x <= 2**31 -1:
            return x
        else:
            return 0