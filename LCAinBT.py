class Node:
 def __init__(self,val):
  self.left=None
  self.right=None
  self.data=val


def LCA(root,p,q):
 if root is None or p is None or q is None:
  return
 if root.data==p or root.data==q:
  return root
 lh=LCA(root.left,p,q)
 rh=LCA(root.right,p,q)
 if lh and rh:
  return root
 return (lh if lh else rh)
 


root=Node(4)
root.right=Node(5)
root.right.right=Node(6)
root.left=Node(2)
root.left.left=Node(1)
root.left.right=Node(3)
p=1;q=16
print(LCA(root,p,q).data)