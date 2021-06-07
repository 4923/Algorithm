import sys

# input
# type: int, range: 1 <= n <= 100
n = int(sys.stdin.readline())

# output
# consider : When n is 1, conditional n % 2 != 0 and n % 3 == 0 makes variable n special number.
# need : n // 3 or 5 > 0
if n % 2 != 0 and n % 3 == 0 and n // 3 > 0:
    sys.stdout.write("true")
elif n % 2 == 0 and n % 5 == 0 and n // 5 > 0:
    sys.stdout.write("true")
else:
    sys.stdout.write("false")
