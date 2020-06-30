def LeftView(root):
 if root is None:
  return
 print(root.data, end=" ")
 if root.left is not None:
  LeftView(root.left)
 elif root.left is None and root.right is not None:
  LeftView(root.right)
 else:
  return None
  