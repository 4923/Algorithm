import sys

# input
a, b = map(int, sys.stdin.readline().strip().split())

# output
# addition
sys.stdout.write(str(a+b)+"\n")

# substraction
sys.stdout.write(str(a-b)+"\n")

# division
# // : division between integers
sys.stdout.write(str(a//b)+"\n")

# remainder
sys.stdout.write(str(a%b))