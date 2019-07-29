# Day 4: Binomial Distribution I

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

from math import factorial


class Day4(object):

    def __init__(self):
        pass

    def bino(self, x, n):
        return factorial(n) / (factorial(x) * factorial(n - x))

    def binomial_distribution_i(self, x: int, n: int, p: float, q: float) -> \
            float:
        b = self.bino(x, n)
        px = p ** x
        qd = q ** (n - x)
        return b * px * qd


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    d4 = Day4()
    b, g = list(map(float, input().split()))
    p = b / (b + g)
    q = 1 - p
    result = 0
    for r in range(3, 7):
        result += d4.binomial_distribution_i(r, 6, p, q)

    print('{:.3f}'.format(result))





