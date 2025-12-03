# https://adventofcode.com/2025/day/1
import math

def calc_new_dial_position(curr_dial_position, rotation_direction, rotation_steps):
    # This function assumes a dial range of 0 to 99
    if rotation_direction == "L":
        rotation_steps *= -1 
    
    rotation_end_position = (curr_dial_position + rotation_steps)
    new_dial_position = (rotation_end_position - (rotation_end_position // 100) * 100)
        
    return new_dial_position

def calc_number_of_clicks_onto_zero(curr_dial_position, rotation_direction, rotation_steps):
    # This function assumes a dial range of 0 to 99
    zero_counter = 0
    
    if rotation_direction == "R":
        zero_counter += (curr_dial_position + rotation_steps) // 100
        
    elif rotation_direction == "L":
        new_dial_position = calc_new_dial_position(curr_dial_position, rotation_direction, rotation_steps)
        
        if curr_dial_position == 0:
            # If starting on 0, only count complete loops (not the starting position)
            zero_counter += rotation_steps // 100
        elif rotation_steps > curr_dial_position:
            # Pass 0 at least once during the anti-clockwise rotation
            zero_counter += ((rotation_steps - curr_dial_position - 1) // 100) + 1
            # Then if finishing on 0, then count it too
            if new_dial_position == 0:
                zero_counter += 1
        elif rotation_steps == curr_dial_position:
            # If landing exactly on 0
            zero_counter += 1

    return zero_counter

def count_whenever_dial_passes_zero_during_sequence(starting_dial_position, rotation_sequence):
    counter = 0
    curr_dial_position = starting_dial_position
    
    for rotation_instruction in rotation_sequence:
      rotation_direction = rotation_instruction[0]
      rotation_steps = int(rotation_instruction[1:])

      counter += calc_number_of_clicks_onto_zero(curr_dial_position, rotation_direction, rotation_steps)
      curr_dial_position = calc_new_dial_position(curr_dial_position, rotation_direction, rotation_steps)

    return counter

with open('input.txt', mode="r", encoding="utf-8") as file:
  lines = [line.rstrip() for line in file]
  print (count_whenever_dial_passes_zero_during_sequence(50, lines))

# 6789