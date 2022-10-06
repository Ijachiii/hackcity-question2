def Wealth(x):
  lst = []
  for n in x:
    lst.append(sum(n))
  z = max(lst)
  print(z)
  maximum = lst.index(z)
  print(f"The richest person is customer {maximum+1} with a wealth of {max(lst)}")

Wealth([[1,2,3], [2,5,6], [4,2,5]])