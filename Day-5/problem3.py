# Day 5: Normal Distribution I

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

import math


class Day5(object):

    def __init__(self):
        pass

    def normal_distribution_i(self, std, mean, x):
        return round(0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5)))), 3)


if __name__ == '__main__':
    d5 = Day5()
    mean, std = list(map(float, input().split()))
    h = float(input())
    h1, h2 = list(map(float, input().split()))

    a = d5.normal_distribution_i(std=std, mean=mean, x=h)
    b = d5.normal_distribution_i(std=std, mean=mean, x=h2) - \
        d5.normal_distribution_i(std=std, mean=mean, x=h1)
    print("{:.3f}".format(a))
    print("{:.3f}".format(b))

