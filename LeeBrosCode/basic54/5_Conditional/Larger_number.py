import sys

# input (1<=a,b<=100)
a, b = map(int, sys.stdin.readline().strip().split())

# output
if a >= b:
    sys.stdout.write(str(a))
else:
    sys.stdout.write(str(b))