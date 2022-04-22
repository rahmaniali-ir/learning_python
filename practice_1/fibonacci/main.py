import fibonacci

s = int(input("Please enter the starting index in fibonacci sequence: "))
e = int(input("Please enter the ending index in fibonacci sequence: "))

for i in range(s, e):
  f = fibonacci.fib_range(i)
  print(f'The { i }th fibonacci number is {f}')
