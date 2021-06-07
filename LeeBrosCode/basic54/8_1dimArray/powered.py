import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    print(numbers[i] ** 2, end=" ")
