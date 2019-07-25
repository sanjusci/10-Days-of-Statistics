# Day 0: Mean, Median, and Mode

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


class Day0(object):

    def __init__(self):
        pass

    def mean(self, values: list, n) -> int:
        result = 0
        for value in values:
            result += value
        result /= n
        return result

    def median(self, values: list, n)-> float:
        values = sorted(values)
        if n % 2 != 0:
            return values[n//2] / 2
        else:
            return (values[n//2] + values[n//2 -1]) / 2

    def mode(self, values: list) -> int:
        counters = {}
        result = None
        for value in values:
            if value not in counters:
                counters[value] = 1
            else:
                counters[value] += 1
            if result is None or counters[value] > counters[result]:
                result = value
            elif (counters[value] == counters[result]) and (value < result):
                result = value
        return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    d0 = Day0()
    print(d0.mean(arr, n))
    print(d0.median(arr, n))
    print(d0.mode(arr))





