# The following was coded at speed!

def find_repeated_patterns_in_number_range(lbound, ubound):
  invalid_ids = []

  for x in range(lbound, ubound + 1):
    length = len(str(x))
  
    # No patterns in odd lengthed numbers
    if length % 2 == 0:    
      half_length = int(length / 2)
      first_half = str(x)[0:half_length]
      second_half = str(x)[half_length:]

      if first_half == second_half:
        invalid_ids.append(x)

  return invalid_ids

def total_invalid_ids_in_range(range_string):
  # `ranges_string` e.g. "11-12"
  total = 0
  
  range_list = range_string.split('-')
  invalid_ids = find_repeated_patterns_in_number_range(int(range_list[0]), int(range_list[1]))

  for invalid_id in invalid_ids:
    total += invalid_id

  return total

def grand_total_invalid_ids_from_range_list(ranges_list):
  # `ranges_list` e.g. ["11-12","95-115",...]
  grand_total = 0
  for range_string in ranges_list:
    grand_total += total_invalid_ids_in_range(range_string)

  return grand_total


with open('input.txt', mode="r", encoding="utf-8") as file:
  content = file.read()
  ranges_list = content.split(',')
  print (grand_total_invalid_ids_from_range_list(ranges_list))