# Day 5: Normal Distribution II

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

import math


class Day5(object):

    def __init__(self):
        pass

    def normal_distribution_ii(self, std, mean, x):
        return round(0.5 * 100 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 3)


if __name__ == '__main__':
    d5 = Day5()
    mean, std = list(map(float, input().split()))
    h1, h2 = float(input()), float(input())

    a = round(100 - d5.normal_distribution_ii(std=std, mean=mean, x=h1), 2)
    b = round(100 - d5.normal_distribution_ii(std=std, mean=mean, x=h2), 2)
    print("{:.2f}".format(a))
    print("{:.2f}".format(b))

