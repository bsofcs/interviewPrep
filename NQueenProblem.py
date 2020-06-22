def checkAttack(arr,x,y):
 if arr is None:
  return
 len_a=len(arr)
 for i in range(len_a):
  #no Queen in that row
  if arr[i] is None:
   continue
  #check attack in same row or column
  if i==x or arr[i]==y:
   return 0
  #check attack in diagonal
  if abs(i-x)==abs(arr[i]-y):
   return 0
 return 1

def printChess(arr):
 if arr is None:
  return
 n=len(arr)
 for i in range(n):
  print(f"({i},{arr[i]})",end="")
 print("\n")

"""
"""

def NQueenUtil(n,arr,x=0):
 if x==n:
  printChess(arr)
  return True
 tmp=False
 for i in range(n):
  if checkAttack(arr,x,i)==1:
   arr[x]=i
   tmp=NQueenUtil(n,arr,x+1) or tmp
   arr[x]=None
 return tmp

def NQueenProblem(n):
 if n is None or n<1:
  return None
 arr=[None]*n
 NQueenUtil(n,arr)

n=8
NQueenProblem(n)