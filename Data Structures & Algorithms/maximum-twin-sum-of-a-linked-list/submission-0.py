# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mylist=[]
        temp = head
        while temp:
            mylist.append(temp.val)
            temp=temp.next
        lp,rp=0,len(mylist)-1
        maxSum=0
        while rp > lp:
            maxSum= max(maxSum,mylist[lp]+mylist[rp])
            lp+=1
            rp-=1
        return maxSum

        