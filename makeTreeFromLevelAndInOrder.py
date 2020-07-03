"""
makeTreeFromLevelAndInOrder
"""
class Node:
 def __init__(self,val):
  self.right=None
  self.left=None
  self.data=val

def makeTreeFromLevelAndInOrder(levelOrder,inOrder):
 if levelOrder is None or inOrder is None:
  return
 inStrt=0
 inEnd=len(inOrder)-1
 root=makeTreeUtil(levelorder,inorder,inStrt,inEnd)
 return root

def makeTreeUtil(levelorder,inorder,inStrt,inEnd):
 if levelorder is None or inorder is None or inStrt>inEnd:
  return
 for nodeval in levelorder:
  if nodeval in inorder[inStrt:inEnd+1]:
   node=Node(nodeval)
   inIndex=inorder.index(nodeval)
   break
 if not inIndex:
  return node
 node.left=makeTreeUtil(levelorder,inorder,inStrt,inIndex-1)
 node.right=makeTreeUtil(levelorder,inorder,inIndex+1,inEnd)
 return node

def inOrder(root):
 if root is None:
  return
 inOrder(root.left)
 print(root.data,end=" ")
 inOrder(root.right)


inorder=[4,2,5,1,6,3,7]
levelorder=[1,2,3,4,5,6,7]
print("In Order:",inorder)
print("Level Order:",levelorder)
root=makeTreeFromLevelAndInOrder(levelorder,inorder)
inOrder(root)
