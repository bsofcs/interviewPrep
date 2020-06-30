"""
verticalLevelTraversingBT
"""
verLevel={}
def verticalLevelTravel(root,Vlevel):
 if root is None:
  return
 if Vlevel not in verLevel:
  verLevel[Vlevel]=[root.val]
 else:
  verLevel[Vlevel].append(root.val)
 verticalLevelTravel(root.left,Vlevel-1)
 verticalLevelTravel(root.right,Vlevel+1)

def verticalTraversal(root):
 if root is None:
  return
 Vlevel=0
 verticalLevelTravel(root,Vlevel)
 result=[]
 for i in sorted(verLevel):
  result.append(verLevel[i])
 return result
