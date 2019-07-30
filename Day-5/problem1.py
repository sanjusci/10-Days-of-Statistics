# Day 5: Poisson Distribution I

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

from math import factorial


class Day5(object):

    e = 2.71829

    def __init__(self):
        pass

    def bino(self, n):
        return factorial(n)

    def poisson_distribution_i(self, lm: int, k: int) -> float:
        px = lm**k * self.e ** -lm
        k = self.bino(k)
        #p(k, lm) = (lm ^ k * e ^ -lm) / k!
        return px / k


if __name__ == '__main__':
    d5 = Day5()
    lm = int(input())
    k = int(input())
    result = d5.poisson_distribution_i(lm, k)

    print('{:.3f}'.format(result))

