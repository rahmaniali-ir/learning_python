
def fib_range(n = 1):
  if n <= 0: return 0

  n1 = n2 = 1

  for _ in range(2, n):
    n1, n2 = n2, n1 + n2

  return n2
