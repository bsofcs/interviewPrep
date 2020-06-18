def minimumDiffSortedArray(arr,val):
 if arr is None or val is None:
  return None
 if arr[0]>val:
  return arr[0]
 elif arr[-1]<val:
  return arr[-1]
 else:
  low,high=0,len(arr)-1
  tmp=minimumDiffSortedArrayUtil(arr,val,low,high)
  return arr[tmp]

def minimumDiffSortedArrayUtil(arr,val,low,high):
 if low>high:
  return low
 mid=low+(high-low)//2
 if arr[mid]<=val and arr[mid+1]>val:
  left=abs(val-arr[mid])
  right=abs(arr[mid+1]-val)
  return(mid if left<=right else mid+1)
 elif arr[mid]>val and arr[mid+1]>val:
  high=mid-1
 else:
  low=mid+1
 return minimumDiffSortedArrayUtil(arr,val,low,high)

arr=[1,2,5,6,18,110,123]
val=34
print(minimumDiffSortedArray(arr,val))
  
 