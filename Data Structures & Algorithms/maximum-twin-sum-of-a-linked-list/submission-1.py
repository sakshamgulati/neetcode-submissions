# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:
            
        prev= None
        fp,sp= head,head
    
        while fp and fp.next:
            fp= fp.next.next
            temp = sp.next
            sp.next= prev
            prev= sp
            sp= temp
        
        #reach the end
        res=0
        #reverse slow
        while sp:
            res= max(res, sp.val+prev.val)
            sp= sp.next
            prev= prev.next
        return res
        