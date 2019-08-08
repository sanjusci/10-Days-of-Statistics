# Day 5: Poisson Distribution II

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

from math import factorial


class Day5(object):

    def __init__(self):
        pass

    def poisson_distribution_ii(self, x: float, y: float) -> tuple:

        A = 160 + 40 * (x + x ** 2)
        B = 128 + 40 * (y + y ** 2)
        return A, B


if __name__ == '__main__':
    d5 = Day5()
    x, y = list(map(float, input().split()))
    a, b = d5.poisson_distribution_ii(x, y)
    print("{:.3f}".format(a))
    print("{:.3f}".format(b))

