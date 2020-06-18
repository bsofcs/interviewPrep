def findPivotInBitonicArray(arr,low,high,n):
 mid=low+(high-low)//2
 if low>high:
  return low
 if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1] and (mid==0 or mid==n-1):
  return mid
 elif arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
  low=mid+1
 else:
  high=mid-1
 return findPivotInBitonicArray(arr,low,high,n)

def BinarySearchAsc(arr,low,high,val):
 if low>high:
  return None
 mid=low+(high-low)//2
 if arr[mid]==val:
  return mid
 elif arr[mid]>val:
  high=mid-1
 else:
  low=mid+1
 return BinarySearchAsc(arr,low,high,val)

def BinarySearchDsc(arr,low,high,val):
 if low>high:
  return None
 mid=low+(high-low)//2
 if arr[mid]==val:
  return mid
 elif arr[mid]<val:
  high=mid-1
 else:
  low=mid+1
 return BinarySearchDsc(arr,low,high,val)

def searchMaxInBitonicArray(arr):
 if arr is None:
  return None
 n=len(arr)
 return findPivotInBitonicArray(arr,0,n-1,n)

def searchInBitonicArray(arr,val):
 if arr is None or val is None:
  return None
 n=len(arr)
 high,low=n-1,0
 pivot=findPivotInBitonicArray(arr,low,high,n)
 tmp=BinarySearchAsc(arr,low,pivot,val)
 if tmp is None:
  tmp=BinarySearchDsc(arr,pivot+1,high,val)
 return tmp

arr=[1,2,4,6,8,10,11,7,4,2,0]
val=4
print(arr,val)
print(searchInBitonicArray(arr,val))
print(arr[searchMaxInBitonicArray(arr)])