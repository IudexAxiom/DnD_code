
import cmath
import sys
import time
import math
import numpy as np
import random

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



opt = input("Greetings! Please press 1 to roll for stats or press sny other number for more options.\n")
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



num_dice = input("How many dice are we rolling?\n")
num_dice = int(num_dice)
print("\n")

list_of_dice = np.zeros(num_dice)
reminder = np.zeros(num_dice)

print("Press an integer N to roll a 1dN. Remember, there is a d4, d6, d8, d12, and d20.")
print("If you want to roll the percentile dice, just punch in 100.")
for i in range(num_dice):
    die_num = input("Please press your desired die and then enter.\n")
    die_num = int(die_num)

    if die_num == 4:
        reminder[i] = 4
        list_of_dice[i] = DieRoll(4)
    elif die_num == 6:
        reminder[i] = 6
        list_of_dice[i] = DieRoll(6)
    elif die_num == 8:
        reminder[i] = 8
        list_of_dice[i] = DieRoll(8)
    elif die_num == 12:
        reminder[i] = 12
        list_of_dice[i] = DieRoll(12)
    elif die_num == 20:
        reminder[i] = 20
        list_of_dice[i] = DieRoll(20)
    elif die_num == 100:
        reminder[i] = 10
        list_of_dice[i] = TenSidedDieRoll()
    else :
        print("You punched in an incorrect answer. Code terminating.")
        sys.exit(0)

    mod_num = input("Do you have modifiers for this roll? (-2, +3, +0, etc)\n")
    mod_num = int(mod_num)
    list_of_dice[i] = list_of_dice[i] + mod_num
    #print(list_of_dice)

print("Which specific dice rolled were: ", reminder)
print("The numbers you rolled were: ", list_of_dice)

# We'll add more options with the dice
#print("What do you want to do to these dice?")



elapsed_time = time.process_time() - t
print(elapsed_time)
print("Done!\n")