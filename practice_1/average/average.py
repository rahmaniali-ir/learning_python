
def average(*nums):
  s = 0
  for n in nums:
    s += n

  return s / len(nums)
