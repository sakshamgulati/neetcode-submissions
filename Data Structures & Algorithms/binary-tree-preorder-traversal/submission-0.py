# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.stack=[]
        temp = root
        ans= []
        while temp or self.stack:
            if temp:
                self.stack.append(temp)
                ans.append(temp.val)
                temp=temp.left
            else:
                temp=self.stack.pop()
                temp= temp.right
        return ans
