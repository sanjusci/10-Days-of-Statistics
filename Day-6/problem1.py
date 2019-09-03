# Day 6: The Central Limit Theorem I

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

import math


class Day6(object):

    e = 2.71829

    def __init__(self):
        pass


    # Define functions
    def the_central_limit_theorem_i(self, mean, std, value):
        return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))


if __name__ == '__main__':
    d6 = Day6()
    # Set data
    max_weight = float(input())
    n = float(input())
    mean = float(input())
    std = float(input())

    new_mean = mean * n
    new_std = math.sqrt(n) * std

    # Gets the result and show on the screen
    result = d6.the_central_limit_theorem_i(new_mean, new_std, max_weight)
    print('{:.4f}'.format(result))

