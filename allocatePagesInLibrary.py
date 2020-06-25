def checkIfPossible(A,B,n,mid):
 noOfStudent=1
 curSum=0
 for i in range(n):
  if A[i]>mid:
   return False
  if curSum+A[i]>mid:
   noOfStudent+=1
   curSum=A[i]
   if noOfStudent>B:
    return False
  else:
   curSum+=A[i]
 return True

def allocatePagesInLibrary(A,B):
 n=len(A)
 if n not in range(1,10**5+1) or any(x not in range(1,10**5+1) for x in A) or n<B:
  return None
 high,low,result=0,0,float("INF")
 for i in A:
  high+=i
 while(low<=high):
  mid=low+(high-low)//2
  if checkIfPossible(A,B,n,mid):
   high=mid-1
   result=min(result,mid)
  else:
   low=mid+1
 return result

A = [12, 34, 67, 90]
B = 2
print(allocatePagesInLibrary(A,B))
A = [5, 17, 100, 11]
B = 4
print(allocatePagesInLibrary(A,B))