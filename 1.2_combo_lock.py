import time
import math
debug = True

def get_list_of_strings_from_file_of_strings(file_name):
    with open(file_name, "r") as file_to_read:
        list_from_file = file_to_read.read().splitlines()             #read file into list of strings
        file_to_read.close()
        return(list_from_file)

list_of_lock_turns = get_list_of_strings_from_file_of_strings("Advent_Of_Code\\1.1_adventOfCodeInput.txt")

dial_position = 50  #dial starting position
master_combo = 0    #final answer is the number of times the dial hits exactly zero


for step in list_of_lock_turns:
    rotate = int(step[1:])

    if debug:
        print("Master combo:" , master_combo)
    master_combo = master_combo + (rotate // 100)

    if debug:
        print("Dial position before modification:" , dial_position)
        print('Rotate before modification:' , step)
        print("Adding to master combo:" , rotate // 100)

    if step[0] == "R":          #if direction is Right, extract turn as a positive number
        rotate = rotate % 100
    else:                       #otherwise, direction is Left, so extract turn as a negative number
        rotate = -(rotate % 100)

    #FIRST BRANCH DOSENT START ON ZERO
    if dial_position != 0:
        dial_position += rotate         #turn the dial
        
        if dial_position < 0:           #UNDER ROTATED
            dial_position += 100        #wrap around to 99 if negative
            master_combo += 1           #if dial wraps around past 99, increment master_combo
        
            if debug:
                print('UNDER ROTATED, did not start on zero, adding 1 to master combo.')

        elif dial_position > 99:        #OVER ROTATED
            dial_position -= 100
            master_combo += 1           #if dial wraps around past 0, increment master_combo

            if debug:
                print('OVER ROTATED, did not start on zero, adding 1 to master combo.')

        elif (dial_position == 0):        #if dial is at exactly 0, increment master_combo
                master_combo += 1
                if debug:
                    print('HIT 0, didnt start on zero. Adding 1 to master combo.')
            
    #SECOND BRANCH STARTS ON ZERO
    else:
        if debug:
            print("Starting on zero.")

        dial_position += rotate         #turn the dial

        if dial_position < 0:           #UNDER ROTATED
            dial_position += 100        #wrap around to 99 if negative

            if debug:
                print('UNDER ROTATED, started on zero.')
        elif dial_position > 99:        #OVER ROTATED
            dial_position -= 100

            if debug:
                print('OVER ROTATED, started on zero.')
    if debug:
        print('Dial position after roation:' , dial_position)
        print("Master combo:" , master_combo)
    print()
print("The master combo is:", master_combo)

#Last output with elif statments 6469
#Last output with only if statments 6984
#Fixed input? no 6438
#Last solution: 6984
#New solution: 6469 (Fixed if elif statements so you dont over count our master_combo by accounting for 0 twice.)
#New solution: 5923
