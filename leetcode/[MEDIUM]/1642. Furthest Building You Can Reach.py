import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        li = list()
        
        for i in range(len(heights) - 1):
            if heights[i+1] - heights[i] > 0:
                li.append((heights[i+1] - heights[i],i))
        
        heap = list()
        s = 0
        
        for h,pre in li:
            if s + h > bricks:
                if ladders <= 0:
                    return pre
                else:
                    heapq.heappush(heap,(h*-1,pre))
                    tmp = heapq.heappop(heap)
                    s = s + h + tmp[0]
                    ladders -= 1
            else:
                heapq.heappush(heap,(h*-1,))
                s += h
    
        return len(heights) - 1
        
                