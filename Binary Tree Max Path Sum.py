# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.Max=-1001
        self.MaxPath(root)
        return self.Max
        
        
    def MaxPath(self,root):
        if not root:
            return 0
        
        
        left=max(self.MaxPath(root.left),0)
        right=max(self.MaxPath(root.right),0)
        sum=root.val+left+right
        if sum>self.Max:
            self.Max=sum
        return root.val+max(left,right)
        
        