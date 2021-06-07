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

# INPUT
n = int(input())

# OUTPUT
sum = 0
for i in range(1, n + 1):
    sum += i

print(sum)
