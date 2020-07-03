# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
sumTot=0
class Solution:
 def maxPathSum(self, root: TreeNode) -> int:
  global sumTot
  sumTot=float("-INF")
  if root is None:
    return 0
  if root.left is None and root.right is None and root is not None:
    return root.val
  self.maxPathSumUtil(root)
  return(sumTot)

 def maxPathSumUtil(self,root):
  global sumTot
  if root is None:
   return(0)
  lh=self.maxPathSumUtil(root.left)
  rh=self.maxPathSumUtil(root.right)
  max_single=max(root.val,(max(lh,rh)+root.val))
  max_top=max(max_single,lh+rh+root.val)
  sumTot=max(sumTot,max_top)
  return(max_single)
        