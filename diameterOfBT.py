"""
diameterOfBT
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
if the following tree:
	1
       / \
      2   3
     / \
    4   5
diameter=4 i.e. keeping the node count i.e. [4,2,1,3] or [5,2,1,3]
"""
class Solution:
 def __init__(self):
  self.diameter=0
 def diameterOfBinaryTree(self,root):
  if root is None:
   return 0
  lh=self.diameterOfBinaryTree(root.left)
  rh=self.diameterOfBinaryTree(root.right)
  dia=lh+rh+1
  if dia>self.diameter:
   self.diameter=dia
  else:
   dia=max(lh,rh)+1
  return dia



"""
if the following tree:
	1
       / \
      2   3
     / \
    4   5
diameter=3 i.e. keeping the edge count i.e. [4->2->1->3] or [5->2->1->3]
"""
class Solution1:
 def __init__(self):
    self.maxd=0
    
 def height(self,root):
    if root is None or (root.left is None and root.right is None):
        return 0
    lh=self.height(root.left)
    rh=self.height(root.right)
    if root.left is not None and root.right is not None and rh+lh+2>self.maxd:
        self.maxd=rh+lh+2
    elif (root.left is not None or root.right is not None) and rh+lh+1>self.maxd:
        self.maxd=rh+lh+1
    return(max(lh,rh)+1)

 def diameterOfBinaryTree(self,root):
    if root is None:
        return 0
    self.height(root)
    return(self.maxd)
  