# Day 1: Standard Deviation

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

from math import sqrt


class Day1(object):

    def __init__(self):
        pass

    def standardDeviation(self, values: list, n: int) -> None:
        sum = 0
        for value in values:
            sum += value
        mu = sum/n
        sum = 0
        for value in values:
            sum += (value - mu) ** 2

        nu = sqrt(sum/n)
        print('{:.1f}'.format(nu))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    d1 = Day1()
    d1.standardDeviation(arr, n)





