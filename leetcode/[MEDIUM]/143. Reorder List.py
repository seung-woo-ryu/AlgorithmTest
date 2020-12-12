# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        li = list()
        temp = head
        while temp:
            li.append(temp)
            temp = temp.next
        
        new_head = li.pop(0)
        
        flag = True
        
        while li:
            new = li.pop(-1) if flag else li.pop(0)    
            new_head.next = new
            new_head = new_head.next
            flag = False if flag else True
        new_head.next = None
        