def add(a,b):
  return a+b

def test_add():
  assert add(1, 3) == 4
  assert add(1, -4) == -3

def sub(a,b):
  return a-b

def test_sub():
  assert sub(1, 3) == -2
  assert sub(1, -4) == 5
