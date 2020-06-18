def firstOccurence(arr,low,high,val,n):
 if low>high:
  return
 mid=low+(high-low)//2
 if (mid==0 or arr[mid-1]<val) and arr[mid]==val:
  return mid
 elif arr[mid]>val:
  return firstOccurence(arr,low,mid-1,val,n)
 else:
  return firstOccurence(arr,mid+1,high,val,n)

def lastOccurence(arr,low,high,val,n):
 if low>high:
  return
 mid=low+(high-low)//2
 if (mid==n-1 or arr[mid+1]>val) and arr[mid]==val:
  return mid
 elif arr[mid]>val:
  return lastOccurence(arr,low,mid-1,val,n)
 else:
  return lastOccurence(arr,mid+1,high,val,n)


def findOccurenceOfKeys(arr,val):
 if arr is None or val is None:
  return None
 if val not in arr:
  return(-1,-1)
 low,n=0,len(arr)
 firstOcc=firstOccurence(arr,low,n-1,val,n)
 lastOcc=lastOccurence(arr,low,n-1,val,n)
 return(firstOcc,lastOcc)

arr=[1,2,3,3,4,5]
print(findOccurenceOfKeys(arr,0))