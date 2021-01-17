import sys

# input
a, b = map(int, sys.stdin.readline().strip().split())

# summation
result = 0
for e in range(a,b+1):
    result += e

# output
sys.stdout.write(str(result))