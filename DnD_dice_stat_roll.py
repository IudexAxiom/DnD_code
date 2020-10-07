import cmath
import sys
import time
import math
import numpy as np
import random

t = time.process_time()
print("Starting!\n")




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

iter = input("Enter the total number of stats we are rolling for..\n")
num_iter = int(iter)
print("\n")
#num_iter = 111

for i in range(num_iter):
    StatRoll()

elapsed_time = time.process_time() - t
print(elapsed_time)
print("Done!\n")