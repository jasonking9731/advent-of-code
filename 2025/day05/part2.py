# The following was coded at speed!

input = open('input.txt').read()

# Get the two secions of the file input
[ranges, ingredients] = input.split("\n\n")

# Extract the ranges into a 2D list of integers
# (Ref. https://www.w3schools.com/python/ref_func_map.asp)
# (Ref. https://www.w3schools.com/python/python_lambda.asp)
lmbd = lambda a: list(map(int, a.split('-')))
ranges = list(map(lmbd, ranges.split('\n')))

# Put ranges in ascending order to help counting
ranges.sort()

# Loop through ranges, skipping over any range overlaps
counter = 0
prev_max = 0
for range in ranges:
  curr_min = range[0]
  curr_max = range[1]
  prev_max = max(prev_max, curr_min)

  if prev_max <= curr_max:
    counter += (curr_max - prev_max) + 1
    prev_max = curr_max + 1

print (counter)

# 350684792662845