def multiplePainterProblem(A,B,C):
 if A is None or B is None or C is None:
  return None
 n=len(C)
 block=min(A,n)
 result,i=0,0
 while i<n:
  m=max(C[i:i+block])
  result+=m*B
  i+=block
 return result


A = 2
B = 5
C = [1, 10]
print(multiplePainterProblem(A,B,C))
A = 10
B = 1
C = [1, 8, 11, 3]
print(multiplePainterProblem(A,B,C))
