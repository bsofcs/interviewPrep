def findCeilingInArray(arr,val,low,high):
 if arr is None or val is None:
  return
 if arr[0]>val:
  return 0
 if arr[-1]<val:
  return -1
 mid=low+(high-low)//2
 if arr[mid]==val:
  return mid
 elif arr[mid]<val and arr[mid+1]>val:
  return mid+1
 elif arr[mid]>val and arr[mid-1]<val:
  return mid
 elif arr[mid]>val:
  return findCeilingInArray(arr,val,low,mid-1)
 else:
  return findCeilingInArray(arr,val,mid+1,high)

arr=[4,6,10]
val=6
low,high=0,len(arr)-1
print(findCeilingInArray(arr,val,low,high))
arr=[1,3,8,10,15]
val=14
low,high=0,len(arr)-1
print(findCeilingInArray(arr,val,low,high))
arr=[4,6,10]
val=17
low,high=0,len(arr)-1
print(findCeilingInArray(arr,val,low,high))
arr=[4,6,10]
val=0
low,high=0,len(arr)-1
print(findCeilingInArray(arr,val,low,high))