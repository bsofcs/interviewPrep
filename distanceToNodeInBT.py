from collections import deque

class Node:
 def __init__(self,val):
  self.left=None
  self.data=val
  self.right=None

adj={}
result=[]
visited={}

def buildTree(s):
 if len(s)==0 or s[0]=='N':
  return
 ip=list(s.split())
 print(ip)
 root=Node(int(ip[0]))
 size=0
 q=deque()
 q.append(root)
 i=1
 size+=1
 while size>0 and i<len(ip):
  currNode=q[0]
  q.popleft()
  size=size-1
  currVal=ip[i]
  if currVal != 'N':
   currNode.left = Node(int(currVal))
   q.append(currNode.left)
   size+=1
  i+=1
  if i>=len(ip):
   break
  currVal=ip[i]
  if currVal!='N':
   currNode.right = Node(int(currVal))
   q.append(currNode.right)
   size+=1
  i+=1
 return root

def ConvertTreeToGraph(root):
 if root is None:
  return
 visited[root.data]=0
 if root.left is not None:
  adj[(root.left).data]=root
  ConvertTreeToGraph(root.left)
 if root.right is not None:
  adj[(root.right).data]=root
  ConvertTreeToGraph(root.right)
 
def findTarget(root,target):
 if root==None:
  return -1
 if root.data==target:
  return root
 tmp=findTarget(root.left,target)
 if tmp==-1:
  tmp=findTarget(root.right,target)
 return tmp

def KDistanceNodes(root,target,k):
 visited.clear()
 adj.clear()
 result.clear()
 ConvertTreeToGraph(root)
 targetNode=findTarget(root,target)
 #find in children
 KDistanceNodesChild(targetNode.left,target,k-1)
 KDistanceNodesChild(targetNode.right,target,k-1)
 print("find in parents")
 level=k-1
 while targetNode.data in adj:
  print("Parent",targetNode.data,level)
  parent=adj[targetNode.data]
  KDistanceNodesChild(parent,target,level)
  targetNode=parent
  level-=1
 return(sorted(result))
 
def KDistanceNodesChild(root,target,k):
 if root is None or k<0:
  return
 elif k==0 and root.data!=target and visited[root.data]==0:
  print("Added:",root.data)
  visited[root.data]=1
  result.append(root.data)
 else:
  print("Running:",root.data,k)
  visited[root.data]=1
  KDistanceNodesChild(root.left,target,k-1)
  KDistanceNodesChild(root.right,target,k-1)
 


s="1 2 3 N N 4 6 N 5 N N 7 N"
root=buildTree(s)
target=4
k=2

KDistanceNodes(root,target,k)


s="20 7 24 4 3 N N N N 1"
root=buildTree(s)
target=7
k=2

KDistanceNodes(root,target,k)

s="20 8 22 4 12 N N N N 10 14"
root=buildTree(s)
target=8
k=2

KDistanceNodes(root,target,k)


s="1 N 2 N 3 N 4 5"
root=buildTree(s)
target=5
k=4

KDistanceNodes(root,target,k)