# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        
        reverse = head
        preM = head
        flag = False
        for i in range(1,m):
            preM = head
            head = head.next
            flag = True
        
        for i in range(m,n):
            pre = head
            temp = head = head.next
            
            pre.next = temp.next
            if not flag:
                temp.next = preM
                preM = temp
            else:
                temp.next = preM.next
                preM.next = temp
            
            head = pre
        if  not flag:
            return preM
        else:
            return reverse
            
     
            
            