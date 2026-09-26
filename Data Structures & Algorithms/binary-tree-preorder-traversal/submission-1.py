# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,temp):
            if not temp:
                return None
            self.ans.append(temp.val)
            self.dfs(temp.left)
            self.dfs(temp.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.dfs(root)
        return self.ans


