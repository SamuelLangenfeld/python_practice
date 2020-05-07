# 4d10, reroll on 1 or 2

import random
import math

# python mixes keyword and positional arguments
# you can use both in every function call

# self argument name is a convention, not a real keyword
# if you call a function from an instance of a class object,
# then the first argument is populated with a reference to the instance
# if you call a function from a class object,
# there is no automatic first argument

# If you define a method in a class, the first argument is the instance

def d10(num_dice=1, reroll=[]):
    d10sum = 0
    for _ in range(num_dice):
        decimal = random.random()
        roll = math.floor((decimal * 10 + 1))
        if (roll in reroll):
            new_roll = random.random() * 10 + 1
            roll = math.floor(new_roll)
        d10sum += roll
    return d10sum


def avg_4d10_reroll_1_2():
    avg_sum = 0
    for _ in range(10000):
        avg_sum += d10(4, [1, 2])
    avg_sum = avg_sum/10000.0
    print(avg_sum)

def avg_4d10():
    avg_sum = 0
    for _ in range(10000):
        avg_sum += d10(4, [])
    avg_sum = avg_sum/10000.0
    print(avg_sum)

avg_4d10()
avg_4d10_reroll_1_2()

# print(d10(4, [1,2]))