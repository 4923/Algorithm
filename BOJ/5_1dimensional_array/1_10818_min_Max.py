"""
https://www.acmicpc.net/problem/10818

문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
"""

# INPUT
n = int(input())
# How to read n integer numbers -> loop?
numbers = list(map(int, input().split()))

# Solve: 1 (147116KB 556ms)
# Does the program need other variables?
min_ = numbers[0]
max_ = numbers[0]

for i in range(len(numbers)):
    if numbers[i] < min_:
        min_ = numbers[i]
    if numbers[i] > max_:
        max_ = numbers[i]

print(f"{min_} {max_}")

# Solve: 2 (147100KB	432ms)
# Use list function `min()` `max()`
print(f"{min(numbers)} {max(numbers)}")

# Question:
# Why should the program reads variable `n` if it reads integer numbers at one line?
# Solution:
# Unlike C/C++ and so on, Python does not need to assign a volume of test cases.
# Thus, using Python as a programming language, variable `n` does not affect test case values.
