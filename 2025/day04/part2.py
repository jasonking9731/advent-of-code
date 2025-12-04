# The following was coded at speed!

def count_adjacent_grid_squares(origin_row, origin_col, grid_rows):
  count = 0

  last_row = len(grid_rows)
  last_col = len(grid_rows[0])

  for curr_row in range (-1, 2): # loops from -1, 0, and 1
    for curr_col in range (-1, 2):

      # Ignore the origin grid square
      if curr_row == 0 and curr_col == 0:
        continue

      peek_row = origin_row + curr_row
      peek_col = origin_col + curr_col

      # Don't peek outside of the grid, obvs
      if peek_row >= 0 and peek_row < last_row and peek_col >= 0 and peek_col < last_col:
         adjacent_grid_squares = grid_rows[peek_row][peek_col]
         if adjacent_grid_squares == '@':
           count += 1
           
  return count

def count_rolls_removed_until_remaining_are_surrounded_by_fewer_than_four_rolls_in_grid(grid_rows):
  counter = 0
  changed = True
  
  last_row = len(grid_rows)
  last_col = len(grid_rows[0])
  
  # Keep traversing grid until no more rolls have been removed
  while changed:
    changed = False
    for curr_row in range(last_row):
      for curr_col in range(last_col):
        if grid_rows[curr_row][curr_col] == '@':
          if count_adjacent_grid_squares(curr_row, curr_col, grid_rows) < 4:
            counter += 1
            changed = True
            # Remove roll from current grid square (i.e. change '@' to a '.')
            # (Note: Python doesn't allow simply replacing the character in the string.)
            grid_rows[curr_row] = grid_rows[curr_row][:curr_col] + '.' + grid_rows[curr_row][curr_col + 1:]
          
  return counter


with open('input.txt', mode="r", encoding="utf-8") as file:
  lines = [line.rstrip() for line in file]
  print (count_rolls_removed_until_remaining_are_surrounded_by_fewer_than_four_rolls_in_grid(lines))

# 8972