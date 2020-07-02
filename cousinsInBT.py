"""
cousinsInBT
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
cousinsInBT
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 def findTarget(self,root,x):
  if root is None or x is None:
   return None,None
  l=root.left
  r=root.right
  if l is not None and l.val==x:
   return(root,l)
  elif r is not None and r.val==x:
   return(root,r)
  parent,child=self.findTarget(root.left,x)
  if parent is None or child is None:
   parent,child=self.findTarget(root.right,x)
  return(parent,child)

 def depth(self,root,x,val=0):
  if root is None:
   return None
  if root.val==x.val:
   return val
  tmp=self.depth(root.left,x,val+1)
  if tmp is None:
   tmp=self.depth(root.right,x,val+1)
  return tmp

 def isCousins(self, root, x, y):
  if root is None or x is None or y is None:
   return 
  xParent,xNode=self.findTarget(root,x)
  yParent,yNode=self.findTarget(root,y)
  if xNode is None or yNode is None or xParent is None or yParent is None:
   return False
  hx=self.depth(root,xNode)
  hy=self.depth(root,yNode)
  print(hx,hy,xParent.val,yParent.val)
  if hx is not None and hy is not None and hx==hy and xParent!=yParent:
   return True
  return False