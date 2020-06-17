import math
def findMissing(arr):
 if arr is None:
  return None
 n=len(arr)
 #Take sum of numbers from 0 to n
 res=(n*(n+1))/2
 res_a=0
 #Take sum of all elements
 for i in range(n):
  res_a+=arr[i]
 return(res-res_a)

def findDuplicate(arr):
 if arr is None:
  return None
 n=len(arr)
 res=0
 #taking XOR from 0 to n-1 even though there are n elements as one element will repeat
 for i in range(0,n-1):
  res^=i
 #taking XOR for all elements and the previous one
 for i in range(n):
  res^=arr[i]
 return(res)

def findMissingAndDuplicateUsingCounter(arr):
 if arr is None:
  return None
 n=len(arr)
 res=[0]*n #keep counter
 for i in arr:
   res[i]+=1
 print(res)
 for i in range(n):
  if res[i]==0:
   print("Missing element:",i)
  if res[i]>1:
   print("Repeating element:",i)

def findMissingAndDuplicate(arr):
"""
let A be the duplicate element and B be the missing element
Thus,
Sum of n natural numbers and square of n natural numbers
sumN=(n(n+1))/2 and sumSqN=(n(n+1)(2n+1))/6
i.e. sumN=1+2+..+A+B+..+n sumSqN=1^2+2^2+...+A^2+B^2+...+n^2
Sum of the array is having no B and one extra A to the SumN
thus,
SumA=SumN+A-B
A-B=SumA-SumN	.....(1)
Similarly
A^2-B^2=SumSqA-SumSqN
(A+B)(A-B)=SumSqA-SumSqN ....(2)
Thus,
A+B=(SumSqA-SumSqN)/(SumA-SumN) ...(3)
On solving 1 and 3
 2B=((SumSqA-SumSqN)/(SumA-SumN))+SumN-SumA
 A=SumA-SumN+B
"""
 if arr is None:
  return None
 n=len(arr)-1
 sumN=(n*(n+1))/2
 sumSqN=(n*(n+1)*(2*n+1))/6
 sumA=0
 sumSqA=0
 for i in range(n+1):
  sumA+=arr[i]
  sumSqA+=math.pow(arr[i],2)
 #missing element
 B=(((sumSqA - sumSqN) / (sumA - sumN)) + sumN - sumA) / 2
 A=sumA-sumN+B
 print("Duplicate element:",int(A)," and missing element:",int(B))
  

arr=[0,1,2,3,3,4]
print(findDuplicate(arr))
arr=[0,1,3,4]
print(findMissing(arr))
arr=[0,1,2,3,3,5]
findMissingAndDuplicateUsingCounter(arr)
findMissingAndDuplicate(arr)