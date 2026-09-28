# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.stack=[]
        ans= []
        temp= root
        while temp or self.stack:
            if temp:
                ans.append(temp.val)
                self.stack.append(temp)
                temp= temp.right
            else:
                temp = self.stack.pop()
                temp= temp.left
        
        return ans[::-1]
        