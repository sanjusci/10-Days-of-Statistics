# Day 4: Binomial Distribution II

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
    p = b / 100
    result1 = 0
    result2 = 0
    for r in range(0, 3):
        result1 += d4.binomial_distribution(r, g, p)
    for r in range(2, 11):
        result2 += d4.binomial_distribution(r, g, p)

    print('{:.3f}'.format(result1))
    print('{:.3f}'.format(result2))






