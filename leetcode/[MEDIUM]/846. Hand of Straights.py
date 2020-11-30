class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        
        di = dict()
        
        for h in hand:
            di[h] = 1 if h not in di else di[h] + 1                
        
        for key in sorted(di.keys()):
            if di[key] > 0:
                for w in range(1,W):
                    if key + w not in di:
                        return False
                    if di[key + w] < di[key]:
                        return False
                    di[key+w] = di[key+w] - di[key]
        return True
                