# Day 1: Quartiles

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


class Day1(object):

    def __init__(self):
        pass

    # Enter your code here. Read input from STDIN. Print output to STDOUT

    def quartiles(self, values: list, n: int) -> None:
        values = sorted(values)
        if n % 2 == 0:
            q2 = int((values[n // 2] + values[n // 2 - 1]) / 2)
        else:
            q2 = values[n // 2]

        values1 = values[:n//2]
        values2 = values[n//2:] if n % 2 ==0 else values[n//2 + 1:]
        l1 = len(values1)
        l2 = len(values2)

        if l1 % 2 == 0:
            q1 = int((values1[l1 // 2] + values1[l1 // 2 - 1]) / 2)
        else:
            q1 = values1[l1 // 2]

        if l2 % 2 == 0:
            q3 = int((values2[l2 // 2] + values2[l2 // 2 - 1]) / 2)
        else:
            q3 = values2[l1 // 2]

        print(q1)
        print(q2)
        print(q3)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    d1 = Day1()
    d1.quartiles(arr, n)





