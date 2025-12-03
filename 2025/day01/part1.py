# The following was coded at speed!

def calc_new_dial_position(curr_dial_position, rotation_instruction):
    # Decode rotation string into direction and steps 
    rotation_direction = rotation_instruction[0]
    rotation_steps = int(rotation_instruction[1:])

    # Increment/Decrement the position
    new_dial_position = -1
    if rotation_direction == "L":
        new_dial_position = curr_dial_position - rotation_steps
    elif rotation_direction == "R":
        new_dial_position = curr_dial_position + rotation_steps
    else:
        raise ValueError("Unexpected rotation direction: " + rotation_direction)
    
    # Adjust position number whenever it passes zero
    while new_dial_position < 0 or new_dial_position > 99:
        if new_dial_position > 99:
            new_dial_position = new_dial_position - 100
        elif new_dial_position < 0:
            new_dial_position = new_dial_position + 100

    return new_dial_position

def count_whenever_dial_lands_on_zero_during_sequence(starting_dial_position, rotation_sequence):
    counter = 0
    curr_dial_position = starting_dial_position
    
    # Read puzzle input file line by line
    for rotation_instruction in rotation_sequence:
        curr_dial_position = calc_new_dial_position(curr_dial_position, rotation_instruction)
        if (curr_dial_position == 0):
            counter += 1

    return counter

with open('input.txt', mode="r", encoding="utf-8") as file:
  lines = [line.rstrip() for line in file]
  print (count_whenever_dial_lands_on_zero_during_sequence(50, lines))

# 1147