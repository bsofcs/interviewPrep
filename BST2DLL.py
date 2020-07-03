"""
BST2DLL
"""

class Node:
    
 def __init__(self, value):

  self.left = None

  self.data = value

  self.right = None



def bToDLL(root):

 if root is None:
  return
 head,tail=bToDLLUtil(root)
 return head



def bToDLLUtil(root):

 if root is None:
  return(None,None)
 if root.left is None and root.right is None:
  return(root,root)
 head_dl,tail_dl=bToDLLUtil(root.left)
 head_dr,tail_dr=bToDLLUtil(root.right)
 root.left=tail_dl
 root.right=head_dr
 if tail_dl:
  tail_dl.right=root
 if head_dr:
  head_dr.left=root
 if not head_dl:
  head_dl=root
 if not tail_dr:
  tail_dr=root
 return(head_dl,tail_dr)

def printDLL(head):
 if head is None:
  return None
 while head is not None:
  print(head.data,end=" ")
  prev=head
  head=head.right
 print()
 while prev is not None:
  print(prev.data,end=" ")
  prev=prev.left
 
root=Node(4)
root.right=Node(5)
root.right.right=Node(6)
root.left=Node(2)
root.left.left=Node(1)
root.left.right=Node(3)
head=bToDLL(root)
printDLL(head)