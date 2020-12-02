class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        li = [str(N) for N in range(1,n+1)]
        li.sort()
        return li