"""
levelTraversingBT
"""
levelOrder={}
def levelTravel(root,level=0):
 if root is None:
  return
 if level not in levelOrder:
  levelOrder[level]=[root.val]
 else:
  levelOrder[level].append(root.val)
 levelTravel(root.left,level+1)
 levelTravel(root.right,level+1)

def levelOrder(root):
 if root is None:
  return
 levelOrder.clear()
 levelTravel(root)
 result=[]
 for i in levelOrder:
  result.append(levelOrder[i])
 return result

def levelOrderUsingQ(root: TreeNode) -> List[List[int]]:
 q1 = deque()
 q2 = deque()
 if not root:
     return []
 ans = []
 q1.append(root) 
 while q1 or q2:
     for node in q1:
  if node.left:
      q2.append(node.left)
  if node.right:
      q2.append(node.right)
     level1 = []
     while q1:
  val = q1.popleft().val
  level1.append(val)
     if level1:
  ans.append(level1)
     
     for node in q2:
  if node.left:
      q1.append(node.left)
  if node.right:
      q1.append(node.right)
     level2 = []
     while q2:
  
  val = q2.popleft().val
  level2.append(val)
     if level2: 
  ans.append(level2)
 return ans