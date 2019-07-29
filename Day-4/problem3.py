# Day 4: Geometric Distribution I

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

from math import factorial


class Day4(object):

    def __init__(self):
        pass

    def geometric_distribution_i(self, n: int, p: float) -> float:
            q = 1 - p
            qd = q ** (n - 1)
            return qd * p


if __name__ == '__main__':
    d4 = Day4()
    b, g = list(map(float, input().split()))
    n = int(input())
    p = b / g
    print('{:.3f}'.format(d4.geometric_distribution_i(n, p)))






