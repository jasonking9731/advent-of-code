# The following was coded at speed!

input = open('input.txt').read()

# Get the two secions of the file input
[ranges, ingredients] = input.split("\n\n")

# Extract the ranges into a 2D list of integers
# (Ref. https://www.w3schools.com/python/ref_func_map.asp)
# (Ref. https://www.w3schools.com/python/python_lambda.asp)
lmbd = lambda a: list(map(int, a.split('-')))
ranges = list(map(lmbd, ranges.split('\n')))

# Extract the ingredients into a list of integers
ingredients = list(map(int, ingredients.split("\n")[:-1]))

# Loop through each ingredient
# and see if it falls with a range
counter = 0
for ingredient in ingredients:
  for range in ranges:
    if ingredient >= range[0] and ingredient <= range[1]:
      # Ingredient found within a range
      counter += 1
      break

print (counter)

# 775