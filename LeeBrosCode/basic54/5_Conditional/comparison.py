import sys

# input
a, b = map(int, sys.stdin.readline().strip().split())

# output
# a >= b?
if a >= b:
    sys.stdout.write(str(1) + "\n")
else:
    sys.stdout.write(str(0) + "\n")

# a > b?
if a > b:
    sys.stdout.write(str(1) + "\n")
else:
    sys.stdout.write(str(0) + "\n")

# b >= a?
if a <= b:
    sys.stdout.write(str(1) + "\n")
else:
    sys.stdout.write(str(0) + "\n")

# b > a?
if a < b:
    sys.stdout.write(str(1) + "\n")
else:
    sys.stdout.write(str(0) + "\n")

# a == b?
if a == b:
    sys.stdout.write(str(1) + "\n")
else:
    sys.stdout.write(str(0) + "\n")

# a != b?
if a != b:
    sys.stdout.write(str(1) + "\n")
else:
    sys.stdout.write(str(0) + "\n")
