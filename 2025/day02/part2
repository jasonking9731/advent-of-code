def find_repeating_pattern_in_numbers_in_range(lbound, ubound):
  invalid_ids = []

  for i in range(lbound, ubound + 1):
    curr_num_string = str(i)
    # print (curr_num_string + "...")

    number_length = len(curr_num_string)
    # traverse through combinations - e.g. 1, 10, 101, 1010
    for x in range(1, number_length):
      pattern = curr_num_string[0:x]
      # print ("  Now looking for: " + pattern + " repeated...")
      pattern_length = len(pattern)

      # walkthrough number, until the end or until the pattern stops
      curr_pos = 0
      is_match = True
      while (is_match) and (curr_pos < number_length):
        # print ("    ...in: " + curr_num_string[curr_pos:curr_pos + pattern_length])
        is_match = (curr_num_string[curr_pos:curr_pos+pattern_length] == pattern)
        curr_pos += pattern_length

      if is_match:
        # print("  FOUND!")
        if int(curr_num_string) not in invalid_ids:
          invalid_ids.append(int(curr_num_string))
      # else:
        # print("  no match.")

  return invalid_ids

def total_invalid_ids_in_range(range_string):
  # `ranges_string` e.g. "11-12"
  print (range_string)
  total = 0
  
  range_list = range_string.split('-')
  invalid_ids = find_repeating_pattern_in_numbers_in_range(int(range_list[0]), int(range_list[1]))

  for invalid_id in invalid_ids:
    total += invalid_id

  return total

def grand_total_invalid_ids_from_range_list(ranges_list):
  # `ranges_list` e.g. ["11-12","95-115",...]
  grand_total = 0
  for range_string in ranges_list:
    grand_total += total_invalid_ids_in_range(range_string)

  return grand_total

def part2():
  with open('input.txt', mode="r", encoding="utf-8") as file:
    content = file.read()
    ranges_list = content.split(',')
    print (grand_total_invalid_ids_from_range_list(ranges_list))

part2()
