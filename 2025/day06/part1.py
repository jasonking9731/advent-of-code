import re

with open('input.txt') as file:
  lines = file.read().split('\n')

worksheet = []
for line in lines:
  worksheet.append(re.findall("(\d+|\+|\*)", line))

# Extract numbers section
numbers = worksheet[:-1]
numbers = [list(map(int, row)) for row in numbers]

# Extract maths operations from the last line
operations = worksheet[-1]

# Loop through each column an perform maths operation
accumulator = 0
calc = lambda num1, num2, op: (num1 + num2) if op == '+' else (num1 * num2) if op == '*' else 0
for col_indx in range(0, len(operations)):
  col_total = 0
  for num_set in numbers:
    if col_total == 0:
      col_total = int(num_set[col_indx])
    else:
      col_total = calc(col_total, int(num_set[col_indx]), operations[col_indx])

  accumulator += col_total

print(accumulator)

# 4364617236318