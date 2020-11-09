
import numpy as np
import random
import time

t0 = time.process_time()

# Generating N rolls of every type of dice
N = 1_000
d = {
    'd4': np.random.randint(1, 5, N),
    'd6': np.random.randint(1, 7, N),
    'd8': np.random.randint(1, 9, N),
    'd12': np.random.randint(1, 13, N),
    'd20': np.random.randint(1, 21, N),
    'd100': np.random.randint(0, 100, N)
    }

def StatRoll():
    raw_num = sorted(np.random.choice(d['d6'], 4, False))
    del raw_num[0]
    print("Your roll is: " + str(sum(raw_num)))

def CheckNeg(list):
    for i in range(len(list)):
        if list[i] < 0:
            list[i] = 0
    return list

opt_num = int(input("Greetings! Please press 1 to roll for stats, press 2 to roll for advantage/disadvantage, or press 3 to roll any other combination of dice.\n"))
print("\n")

if opt_num == 1:
    num_iter = int(input("Enter the total number of stats we are rolling for..\n")) 
    print("\n")
    for i in range(num_iter):
        StatRoll()
    exit
elif opt_num == 2:
    vantage_opt = int(input("We are going to roll 2d20, with modifiers, and you decide if it is advantage or disadvantage. \nPress 1 to roll for advantage, or press 2 to roll for disadvantage.\n"))
    print("\n")
    if vantage_opt == 1:
        mod_num = int(input("Modifiers? (-2, +3, +0, etc)\n"))
        print("\n")
        nums = np.random.choice(d['d20'], 2, False)
        nums[0] += mod_num
        nums[1] += mod_num
        CheckNeg(nums)
        print("The roll is: " + str(max(nums)) + "\n")
    elif vantage_opt == 2:
        mod_num = int(input("Modifiers? (-2, +3, +0, etc)\n"))
        print("\n")
        nums = np.random.choice(d['d20'], 2, False)
        nums[0] += mod_num
        nums[1] += mod_num
        CheckNeg(nums)
        print("The roll is: " + str(min(nums)) + "\n")
    else :
        raise Exception('You punched in an incorrect answer. Code terminating.')
    exit
elif opt_num == 3:
    num_dice = int(input("How many dice are we rolling?\n"))
    print("\n")
    list_of_dice = np.zeros(num_dice, dtype=int)
    reminder = []
    print("Press an integer N to roll a 1dN. Remember, there is a d4, d6, d8, d12, and d20. \nIf you want to roll the percentile dice, just punch in 100.")
    for i in range(num_dice):
        die_num = int(input("Which die?\n"))
        print("\n")
        if die_num == 4:
            reminder.append("1d4")
            list_of_dice[i] = np.random.choice(d['d4'], 1)
        elif die_num == 6:
            reminder.append("1d6")
            list_of_dice[i] = np.random.choice(d['d6'], 1)
        elif die_num == 8:
            reminder.append("1d8")
            list_of_dice[i] = np.random.choice(d['d8'], 1)
        elif die_num == 12:
            reminder.append("1d12")
            list_of_dice[i] = np.random.choice(d['d12'], 1)
        elif die_num == 20:
            reminder.append("1d20")
            list_of_dice[i] = np.random.choice(d['d20'], 1)
        elif die_num == 100:
            reminder.append("2d10")
            list_of_dice[i] = np.random.choice(d['d100'], 1)
        else :
            raise Exception('You punched in an incorrect answer. Code terminating.')
        mod_num = int(input("Modifiers? (-2, +3, +0, etc)\n"))
        print("\n")
        list_of_dice[i] += mod_num
        list_of_dice = CheckNeg(list_of_dice)

    print("Dice rolled were:" + str(reminder) + "\n")
    print("Final number(s), with mod(s), are:" + str(list(list_of_dice)) + "\n")
else :
    raise Exception('You punched in an incorrect answer. Code terminating.')


elapsed_time = time.process_time() - t0
print("\nDone!")
print("Our runtime was "+ str(elapsed_time) + " seconds.")