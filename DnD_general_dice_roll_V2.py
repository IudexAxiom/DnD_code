import cmath
import sys
import time
import math
import numpy as np
import random
import pprint

t = time.process_time()
#print("Starting!\n")




# Rolling ONE die from 1 to n
def DieRoll(n):
    num = random.randint(1,n)
    #print("We rolled one die for ", num)
    return(num)

# Rolling a ten-sided die from 00 to 90, by tens
def TenSidedDieRoll1():
    num = random.randrange(00,99, 10)
    return(num)

# Rolling a ten-sided die from 0 to 9, by ones
def TenSidedDieRoll2():
    num = random.randint(0,9)
    return(num)

# The sum of rolling the two ten sided dice
def TenSidedDieRoll():
    num1 = TenSidedDieRoll1()
    num2 = TenSidedDieRoll2()
    num = num1 + num2
    if num == 00:
        num = 100
    print("We rolled two ten-sided dice for ", num)
    return(num)


# Rolling dice to determine stats
def StatRoll():
    raw_num = [DieRoll(6), DieRoll(6), DieRoll(6), DieRoll(6)]
    #print(raw_num)
    raw_num = sorted(raw_num)
    del raw_num[0]
    new_num = raw_num
    total = sum(new_num)
    print("The combined roll is ", total, "\n")
    return(total)

# This is to check to make sure no negatives, with mods, are rolled
def CheckNeg(list):
    num = 0
    while(num < len(list)): 
        if list[num] < 0: 
           #print("Uh oh! We rolled a negative. We will default this to zero.")
           list[num] = 0
        num += 1
    return(list)





opt = input("Greetings! Please press 1 to roll for stats, press 2 to roll for advantage/disadvantage, or press any other number for more options.\n")
opt_num = int(opt)
print("\n")

if opt_num == 1:
    iter = input("Enter the total number of stats we are rolling for..\n")
    num_iter = int(iter)
    #num_iter = 111
    print("\n")
    for i in range(num_iter):
        StatRoll()
    sys.exit(0)

if opt_num == 2:
    print("We are going to roll 2d20, with modifiers, and you decide if it is advantage or disadvantage.")
    adv_opt = input("Press 1 to roll for advantage, or press 2 to roll for disadvantage.\n")
    adv_opt = int(adv_opt)
    nums = np.zeros(2)

    if adv_opt == 1:
        nums = [DieRoll(20), DieRoll(20)]
        mod_num = input("Do you have modifiers for this roll? (-2, +3, +0, etc)\n")
        mod_num = int(mod_num)
        nums[0], nums[1] = nums[0] + mod_num, nums[1] + mod_num
        nums = CheckNeg(nums)
        num1 = max(nums)
        print(num1)
    elif adv_opt == 2:
        nums = [DieRoll(20), DieRoll(20)]
        mod_num = input("Do you have modifiers for this roll? (-2, +3, +0, etc)\n")
        mod_num = int(mod_num)
        nums[0], nums[1] = nums[0] + mod_num, nums[1] + mod_num
        nums = CheckNeg(nums)
        num1 = min(nums)
        print(num1)
    else :
        print("You punched in an incorrect answer. Code terminating.")
        sys.exit(0)

    sys.exit(0)




num_dice = input("How many dice are we rolling?\n")
num_dice = int(num_dice)
print("\n")

list_of_dice = np.zeros(num_dice, dtype=int)
reminder = []

print("Press an integer N to roll a 1dN. Remember, there is a d4, d6, d8, d12, and d20.")
print("If you want to roll the percentile dice, just punch in 100.")
for i in range(num_dice):
    die_num = input("Please press your desired die and then enter.\n")
    die_num = int(die_num)

    if die_num == 4:
        #reminder[i] = 4
        reminder.append("1d4")
        list_of_dice[i] = DieRoll(4)
    elif die_num == 6:
        #reminder[i] = 6
        reminder.append("1d\6")
        list_of_dice[i] = DieRoll(6)
    elif die_num == 8:
        #reminder[i] = 8
        reminder.append("1d8")
        list_of_dice[i] = DieRoll(8)
    elif die_num == 12:
        #reminder[i] = 12
        reminder.append("1d12")
        list_of_dice[i] = DieRoll(12)
    elif die_num == 20:
        #reminder[i] = 20
        reminder.append("1d20")
        list_of_dice[i] = DieRoll(20)
    elif die_num == 100:
        #reminder[i] = 10
        reminder.append("1d10")
        list_of_dice[i] = TenSidedDieRoll()
    else :
        print("You punched in an incorrect answer. Code terminating.")
        sys.exit(0)

    mod_num = input("Do you have modifiers for this roll? (-2, +3, +0, etc)\n")
    mod_num = int(mod_num)
    list_of_dice[i] = list_of_dice[i] + mod_num
    list_of_dice = CheckNeg(list_of_dice)
    print("\n")

str(reminder)
a = list(list_of_dice)
print("Dice rolled were:")
print(reminder)
print("Final number(s), with mod(s), are:")
print(a)

# We'll add more options with the dice
# Add GUI?

elapsed_time = time.process_time() - t
print(elapsed_time)
print("Done!\n")