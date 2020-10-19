from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False
        
        else:
            AL, BL= list(), list()
            
            for a,b in zip(A,B):
                if a != b:
                    AL.append(a)
                    BL.append(b)
                    if len(AL) > 2:
                        return False
            if len(AL) == 2 and Counter(AL) == Counter(BL) :
                return True
            elif len(AL) == 0:
                for t, n in Counter(A).items():
                    if n >=2 :
                        return True
                return False