class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        li = set([_ for _ in range(n)])
        
        for fr,to in edges:
            if to in li:
                li.remove(to)
        
        return list(li)