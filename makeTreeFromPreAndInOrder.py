"""
makeTreeFromPreAndInOrder
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
"""
preIndex=0
postIndex=0
class TreeNode:
 def __init__(self, val=0, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right

def buildTreePreUtil(inorder,preorder,inStrt,inEnd):
 global preIndex
 if inStrt>inEnd:
  return None
 currNode=TreeNode(preorder[preIndex])
 preIndex+=1
 if inStrt==inEnd:
  return currNode
 index=inorder.index(currNode.val)
 currNode.left=buildTreePreUtil(inorder,preorder,inStrt,index-1)
 currNode.right=buildTreePreUtil(inorder,preorder,index+1,inEnd)
 return currNode

def buildTreePostUtil(postorder,inorder,inStrt,inEnd):
 global postIndex
 print(postorder[postIndex],inStrt,inEnd,postIndex)
 if inStrt>inEnd:
  return None
 currNode=TreeNode(postorder[postIndex])
 postIndex-=1
 if inStrt==inEnd:
  return currNode
 index=inorder.index(currNode.val)
 currNode.left=buildTreePostUtil(postorder,inorder,inStrt,index-1)
 currNode.right=buildTreePostUtil(postorder,inorder,index+1,inEnd)
 return currNode

def buildTreeFromPreAndInOrder(preorder,inorder):
 global preIndex
 preIndex=0
 if preorder is None or inorder is None:
  return
 inEnd=len(inorder)-1
 inStrt=0
 root=buildTreePreUtil(inorder,preorder,inStrt,inEnd)
 return root

def buildTreeFRomPostAndInOrder(postorder,inorder):
 global postIndex
 if postorder is None or inorder is None:
  return
 postIndex=len(postorder)-1
 inStrt=0
 inEnd=postIndex
 root=buildTreePostUtil(postorder,inorder,inStrt,inEnd)
 return root

def inorderTravel(root):
 if root is None:
  return
 inorderTravel(root.left)
 print(root.val,end=" ")
 inorderTravel(root.right)

def postorderTravel(root):
 if root is None:
  return
 postorderTravel(root.left)
 postorderTravel(root.right)
 print(root.val,end=" ")

def preorderTravel(root):
 if root is None:
  return
 print(root.val,end=" ")
 preorderTravel(root.left)
 preorderTravel(root.right)


inorder=[4,2,5,1,6,3,7]
postorder=[4,5,2,6,7,3,1]
print("Inorder:",inorder)
print("Postorder:",postorder)
root=buildTreeFRomPostAndInOrder(postorder,inorder)
inorderTravel(root)
print()
postorderTravel(root)
print()
preorderTravel(root)