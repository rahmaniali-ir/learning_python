import fibonacci

# s = int(input("Please enter the starting index in fibonacci sequence: "))
# e = int(input("Please enter the ending index in fibonacci sequence: "))

# for i in range(s, e):
#   f = fibonacci.fib_index(i)
#   print(f'The { i }th fibonacci number is {f}')

i = int(input("Please enter an index: "))
print(fibonacci.get_sequence_until(i))
