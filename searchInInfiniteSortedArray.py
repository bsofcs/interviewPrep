"""
since the array size is infinite, so it will be waste to calculate the length of array.
so the we need to find a small range in which the val is likely to exist like
val>arr[low] and val<arr[high]
as the array is sorted so the number must exist in between them or not
once range is obtained we can use Interpolation Search
We use Interpolation as the array is infinite in size and sorted so the elements will be evenly distributed
"""
import math
def interpolationSearch(arr,low,high,val):
 if low>high:
  return -1
 mid=low+int(((val-arr[low])*(high-low))/(arr[high]-arr[low]))
 if arr[mid]==val:
  return mid
 elif arr[mid]>val:
  high=mid-1
 else:
  low=mid+1
 return interpolationSearch(arr,low,high,val)

def searchInInfiniteSortedArray(arr,val):
 if arr is None or val is None:
  return None
 i=0
 low=0
 high=int(math.pow(2,i))
 while True:
  if arr[low]<=val and arr[high]>val:
   break
  else:
   i+=1
   low=high
   high=int(math.pow(2,i))
 return interpolationSearch(arr,low,high,val)

arr=[i for i in range(10000) if i%2==0]
val=233
print(arr,"\n",val)
print(searchInInfiniteSortedArray(arr,val))