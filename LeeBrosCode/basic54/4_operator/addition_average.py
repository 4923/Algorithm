import sys

# input
a, b = map(int, sys.stdin.readline().strip().split())

# output
# addition
sys.stdout.write(str(a + b) + " ")

# average
sys.stdout.write(f"{(a+b)/2:.1f}")
