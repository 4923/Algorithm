"""
문제
John got a bad mark in math. The teacher gave him another task.
John is to write a program which computes the sum of integers from 1 to n.
If he manages to present a correct program, the bad mark will be cancelled.

Write a program which:
* reads the number n from the standard input,
* computes the sum of integers from 1 to n,
* writes the answer to the standard output.

입력
The first and only line of the standard input contains one integer n (1 ≤ n ≤ 10 000).

출력
One integer is to be written to the standard output.
This integer should be the sum of integers from 1 to n.
"""

import sys


def sum(n):
    if n == 0:
        return n
    elif n > 0:
        return n + sum(n - 1)


def main():
    # INPUT: (1 ≤ n ≤ 10 000)
    n = int(input())

    # [error] : revursive error
    # input value: 50000
    # error message: 'RecursionError: maximum recursion depth exceeded in comparison'
    # sys로 setrecursionlimit을 풀어도 같은 에러 발생 => PyPy3으로 언어 변경

    # OUTPUT
    print(sum(n))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
