import average

nums = []
count = 3

for i in range(count):
  nums.append(int(input(f'Please enter the { i + 1 }th number: ')))

print("AVG: " + str(average.average(*nums)))
