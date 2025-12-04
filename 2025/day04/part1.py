# The following was coded at speed!

def count_adjacent_grid_squares(origin_row, origin_col, grid_rows):
  count = 0

  last_row = len(grid_rows)
  last_col = len(grid_rows[0])

  for curr_row in range (-1, 2): # loops from -1, 0, and 1
    for curr_col in range (-1, 2):

      # Ignore the original grid square
      if curr_row == 0 and curr_col == 0:
        continue

      peek_row = origin_row + curr_row
      peek_col = origin_col + curr_col

      if peek_row >= 0 and peek_row < last_row and peek_col >= 0 and peek_col < last_col:
         adjacent_grid_squares = grid_rows[peek_row][peek_col]
         if adjacent_grid_squares == '@':
           count += 1
           
  return count

def count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(grid_rows):
  counter = 0
  
  last_row = len(grid_rows)
  last_col = len(grid_rows[0])
  
  for curr_row in range(last_row):
    for curr_col in range(last_col):
      if grid_rows[curr_row][curr_col] == '@':
        if count_adjacent_grid_squares(curr_row, curr_col, grid_rows) < 4:
          counter += 1
          
  return counter


with open('input.txt', mode="r", encoding="utf-8") as file:
  lines = [line.rstrip() for line in file]
  print (count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(lines))

# 1540


# The below attempt (showhow) counted 1550, which was 10 too many

# def count_rolls_surrounded_by_fewer_than_four_rolls(grid_rows):
#   counter = 0
  
#   last_row_indx = len(grid_rows) - 1
#   last_col_indx = len(grid_rows[0]) - 1
  
#   for curr_row_indx in range(0, last_row_indx + 1):
#     for curr_col_indx in range(0, last_col_indx + 1):

#       if grid_rows[curr_row_indx][curr_col_indx] == '@':
#         adjacent_grids = ""

#         # Above row squares...
#         if (curr_row_indx - 1) >= 0:
#           # Get top-left grid square, if exists
#           if (curr_col_indx - 1) >= 0:
#             adjacent_grids += grid_rows[curr_row_indx - 1][curr_col_indx - 1]
          
#           # Get top grid square, if exists
#           adjacent_grids += grid_rows[curr_row_indx - 1][curr_col_indx]

#           # Get top-right grid square, if exists
#           if (curr_col_indx + 1) <= last_col_indx:
#             adjacent_grids += grid_rows[curr_row_indx - 1][curr_col_indx + 1]

#         # Get left grid square, if exists
#         if (curr_col_indx - 1) >= 1:
#           adjacent_grids += grid_rows[curr_row_indx][curr_col_indx - 1]

#         # Get right grid square, if exists
#         if (curr_col_indx + 1) <= last_col_indx:
#           adjacent_grids += grid_rows[curr_row_indx][curr_col_indx + 1]

#         # Below row squares...
#         if (curr_row_indx + 1) <= last_row_indx:
#           # Get top-left grid square, if exists
#           if (curr_col_indx - 1) >= 0:
#             adjacent_grids += grid_rows[curr_row_indx + 1][curr_col_indx - 1]
          
#           # Get top grid square, if exists
#           adjacent_grids += grid_rows[curr_row_indx + 1][curr_col_indx]

#           # Get top-right grid square, if exists
#           if (curr_col_indx + 1) <= last_col_indx:
#             adjacent_grids += grid_rows[curr_row_indx + 1][curr_col_indx + 1]

#         if adjacent_grids.count("@") < 4:
#           counter += 1

#   return counter