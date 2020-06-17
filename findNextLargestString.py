def findNextLargestString(arr,val):
 if arr is None or val is None:
  return None
 if val>=arr[-1] or val<arr[0]:
  return arr[0]  
 low,high=0,len(arr)-1
 while low<high:
  mid=low+(high-low)//2
  if arr[mid]<=val and arr[mid+1]>val:
   return(arr[mid+1])
  if arr[mid]>val:
   high=mid-1
  else:
   low=mid+1

arr=['b','c','g','h']
val='g'
print(findNextLargestString(arr,val))