import sys

# INPUT
a, b = map(int, sys.stdin.readline().strip().split())

# solve
sum = 0
for even in range(a, b + 1):
    if even % 2 == 0:
        sum += even

# OUTPUT
print(sum)
