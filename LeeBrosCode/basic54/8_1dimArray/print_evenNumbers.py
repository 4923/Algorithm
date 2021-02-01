import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

for number in numbers:
    if number % 2 == 0:
        print(number, end = " ")