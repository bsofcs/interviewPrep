"""
makeTreeFromPreAndInOrder
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
"""
class TreeNode:
 def __init__(self, val=0, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right

def buildTreeUtil(inorder,preorder,inStrt,inEnd):
 if inStrt>inEnd:
  return None
 currNode=TreeNode(preorder[preIndex])
 preIndex+=1
 if inStrt==inEnd:
  return currNode
 index=inorder.index(currNode.val)
 currNode.left=buildTreeUtil(inorder,preorder,inStrt,index-1)
 currNode.right=buildTreeUtil(inorder,preorder,index+1,inEnd)
 return currNode

def buildTree(preorder,inorder):
 preIndex=0
 if preorder is None or inorder is None:
  return
 inEnd=len(inorder)-1
 inStrt=0
 root=buildTreeUtil(inorder,preorder,inStrt,inEnd)
 return root
 