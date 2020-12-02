class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices < cheeseSlices *2:
            return []
        
        mok, na = divmod(tomatoSlices - cheeseSlices * 2, 2)
        
        if na or cheeseSlices - mok < 0:
            return []
        
        return [mok,cheeseSlices - mok]