
def get_sequence_until(n = 1):
  if n <= 0: return False
  if n == 1: return [1]

  sequence = [1, 1]

  for i in range(2, n):
    sequence.append(sequence[i - 2] + sequence[i - 1])

  return sequence

def fib_index(n = 1):
  if n <= 0: return 0

  n1 = n2 = 1

  for _ in range(2, n):
    n1, n2 = n2, n1 + n2

  return n2
