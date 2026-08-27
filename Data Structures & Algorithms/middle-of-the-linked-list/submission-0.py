# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp,sp= head,head
        while fp is not None and fp.next is not None:
            fp=fp.next.next
            sp=sp.next
        return sp
        