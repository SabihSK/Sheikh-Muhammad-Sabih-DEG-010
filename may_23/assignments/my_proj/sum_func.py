def add(a, b):
  return a + b

def add_positive(a:int, b:int)->int:
  if (a > 0 and b > 0):
    return add(a, b)
  else:
    pass

print(add_positive(6,6))