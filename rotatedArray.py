def findRotatedIndex(arr,low,high):
 if arr is None or low is None or high is None:
  return
 if low>high:
  return -1
 mid=low+(high-low)//2
 if arr[mid]<arr[mid-1] and mid<=high:
  return mid
 elif arr[mid]<arr[mid-1] and mid>=low:
  return mid-1
 elif arr[mid]>arr[high] and arr[mid]>arr[low]:
  return findRotatedIndex(arr,mid+1,high)
 else:
  return findRotatedIndex(arr,low,mid-1)

def BinarySearch(arr,low,high,val):
 if arr is None or val is None:
  return -1
 if low>high:
  return -1
 mid=low+(high-low)//2
 if arr[mid]==val:
  return mid
 elif arr[mid]>val:
  return BinarySearch(arr,low,mid-1,val)
 else:
  return BinarySearch(arr,mid+1,high,val)

def findElementInRotatedArray(arr,val):
 if arr is None or val is None:
  return None
 pivot=findRotatedIndex(arr,0,len(arr)-1)
 tmp=BinarySearch(arr,0,pivot-1,val)
 if tmp==-1:
  tmp=BinarySearch(arr,pivot,len(arr)-1,val)
 return tmp

arr=[10,11,24,0,1]
low=0
high=len(arr)-1
print(findRotatedIndex(arr,low,high))
val=24
print(findElementInRotatedArray(arr,val))
val=2
print(findElementInRotatedArray(arr,val))
val=1
print(findElementInRotatedArray(arr,val))
"""
#Other Test Cases
arr=[10,15,1,3,8]
low=0
high=len(arr)-1
print(findRotatedIndex(arr,low,high))

arr=[4,5,7,9,10,-1,2]
low=0
high=len(arr)-1
print(findRotatedIndex(arr,low,high))

arr=[4,5,7,9,10]
low=0
high=len(arr)-1
print(findRotatedIndex(arr,low,high))

arr=[4,5,7,9,10,0]
low=0
high=len(arr)-1
print(findRotatedIndex(arr,low,high))
"""