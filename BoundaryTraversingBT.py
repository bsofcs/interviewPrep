"""
BoundaryTraversingBT
"""
result=[]
def LeftView(root):
 if root is None or (root.left is None and root.right is None):
  return
 result.append(root.data)
 if root.left:
  LeftView(root.left)
 else:
  LeftView(root.right)

def RightView(root):
 if root is None or (root.left is None and root.right is None):
  return
 if root.right:
  RightView(root.right)
 else:
  RightView(root.left)
 result.append(root.data)

def LeafView(root):
 if root is None:
  return
 if root.left is None and root.right is None:
  result.append(root.data)
 LeafView(root.left)
 LeafView(root.right)

def printBoundaryView(root):
 result.clear()
 if root is None:
  resturn
 result.append(root.data)
 LeftView(root.left)
 LeafView(root)
 RightView(root.right)
 return result