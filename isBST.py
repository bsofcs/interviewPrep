"""
isBST
there are 2 ways of doing it:
1. Recursive: Use DFS and check left<node<right
2. Iterative: Use stack
"""
class Node:
 def __init__(self,val):
  self.left=None
  self.right=None
  self.data=val

def isBSTusingDFS(root,mini,maxi):
 if root is None:
  return True
 if root.data<mini or root.data>maxi:
  return False
 return((isBSTusingDFS(root.left,mini,root.data-1)) and (isBSTusingDFS(root.right,root.data+1,maxi)))

def isBSTusingStack(root):
 if root is None:
  return True
 stack=[(root,float("-INF"),float("INF"))]
 size=1
 while stack:
  root,mini,maxi=stack.pop()
  if not root:
   continue
  if root.data<=mini or root.data>=maxi:
   return False
  stack.append((root.right,root.data,maxi))
  stack.append((root.left,mini,root.data))
 return True

root=Node(4)
root.right=Node(5)
root.right.right=Node(6)
root.left=Node(2)
root.left.left=Node(1)
root.left.right=Node(3)
print(isBSTusingDFS(root,float("-INF"),float("INF")))
print(isBSTusingStack(root))