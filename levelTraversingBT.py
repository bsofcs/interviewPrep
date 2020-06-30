"""
verticalLevelTraversingBT
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
 level.clear()
 levelTravel(root)
 result=[]
 for i in levelOrder:
  result.append(levelOrder[i])
 return result