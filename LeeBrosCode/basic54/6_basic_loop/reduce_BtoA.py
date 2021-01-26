import sys

# INPUT
a, b = map(int, sys.stdin.readline().strip().split())

# OUTPUT
for num in range(b, a-1, -1):
    print(num, end = " ")
