import sys
import time
import math
import numpy as np
import random

t = time.process_time()

# Generating N rolls of every type of dice
N = 100
d = {
    'd4': np.random.randint(1, 5, N),
    'd6': np.random.randint(1, 7, N),
    'd8': np.random.randint(1, 9, N),
    'd12': np.random.randint(1, 13, N),
    'd20': np.random.randint(1, 21, N),
    'd100': np.random.randint(0, 100, N)
    }

def StatRoll():
    raw_num = np.random.choice(d['d6'], 4)
    raw_num = sorted(raw_num)
    del raw_num[0]
    print(sum(raw_num))

def CheckNeg(list):
    i = 0
    while(i < len(list)): 
        if list[i] < 0: 
           #print("Uh oh! We rolled a negative. We will default this to zero.")
           list[i] = 0
        i += 1
    return list

opt = input("Greetings! Please press 1 to roll for stats, press 2 to roll for advantage/disadvantage, or press 3 to roll any other combination of dice.\n")
opt_num = int(opt)
print("\n")

if opt_num == 1:
    iter = input("Enter the total number of stats we are rolling for..\n")
    num_iter = int(iter)
    print("\n")
    for i in range(num_iter):
        StatRoll()
    sys.exit(0)
elif opt_num == 2:
    print("We are going to roll 2d20, with modifiers, and you decide if it is advantage or disadvantage.")
    vantage_opt = input("Press 1 to roll for advantage, or press 2 to roll for disadvantage.\n")
    vantage_opt = int(vantage_opt)
    mod_num = input("Modifiers? (-2, +3, +0, etc)\n")
    mod_num = int(mod_num)
    nums = np.random.choice(d['d20'], 2)
    nums[0], nums[1] = nums[0] + mod_num, nums[1] + mod_num
    CheckNeg(nums)
    print("\n")
    if vantage_opt == 1:
        print(max(nums))
    elif vantage_opt == 2:
        print(min(nums))
    else :
        print("You punched in an incorrect answer. Code terminating.")
        sys.exit(0)
    sys.exit(0)
elif opt_num == 3:
    num_dice = input("How many dice are we rolling?\n")
    num_dice = int(num_dice)
    list_of_dice = np.zeros(num_dice, dtype=int)
    reminder = []
    print("Press an integer N to roll a 1dN. Remember, there is a d4, d6, d8, d12, and d20.")
    print("If you want to roll the percentile dice, just punch in 100.")

    for i in range(num_dice):
        die_num = input("Which die?\n")
        die_num = int(die_num)
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
            print("You punched in an incorrect answer. Code terminating.")
            sys.exit(0)
        mod_num = input("Modifiers? (-2, +3, +0, etc)\n")
        mod_num = int(mod_num)
        list_of_dice[i] = list_of_dice[i] + mod_num
        list_of_dice = CheckNeg(list_of_dice)

    str(reminder)
    a = list(list_of_dice)
    print("Dice rolled were:")
    print(reminder)
    print("Final number(s), with mod(s), are:")
    print(a)
else :
    print("You punched in an incorrect answer. Code terminating.")
    sys.exit(0)


elapsed_time = time.process_time() - t
print(elapsed_time)
print("Done!\n")