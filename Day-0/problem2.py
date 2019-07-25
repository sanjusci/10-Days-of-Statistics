# Day 0: Mean, Median, and Mode

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


class Day0(object):

    def __init__(self):
        pass

    def weighted_mean(self, values: list, w_values: list, n) -> float:
        sum = 0
        w_sum = 0
        for i in range(0, n):
            sum += values[i] * w_values[i]
            w_sum += w_values[i]
        return sum / w_sum


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    w_arr = list(map(int, input().split()))

    d0 = Day0()
    print('{:.1f}'.format(d0.weighted_mean(arr, w_arr, n)))





