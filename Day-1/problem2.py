# Day 1: Interquartile Range

# Enter your code here. Read input from STDIN. Print output to STDOUT

__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"


class Day1(object):

    def __init__(self):
        pass

    def interquartile(self, values: list, f_values: list, n: int) -> None:
        S = []
        for i in range(0, n):
            S.extend([values[i]] * f_values[i])
        S = sorted(S)
        sl = len(S)

        lower_half = S[:sl//2]
        upper_half = S[sl//2:]
        l1 = len(lower_half)
        l2 = len(upper_half)
        q1 = (lower_half[l1//2] + lower_half[l1//2 - 1]) / 2
        q3 = (upper_half[l2//2] + upper_half[l2//2 - 1]) / 2 if n % 2 == 0 \
            else (upper_half[l2//2] + upper_half[l2//2 + 1]) / 2

        print(q3 - q1)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    f_arr = list(map(int, input().split()))
    d1 = Day1()
    d1.interquartile(arr,f_arr, n)





