# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        dummy = ListNode()
        dummy.next= temp
        prev = dummy
        while temp:
            if temp.val == val:
                t1= temp.next
                prev.next= t1
                temp= t1
            else:
                prev=prev.next
                temp=temp.next
        return dummy.next



