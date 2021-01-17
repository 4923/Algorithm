import sys

# input
# form: yyyy.mm.dd
y, m, d = map(int, sys.stdin.readline().strip().split("."))

# output
# expect: mm-dd-yyyy
sys.stdout.write(str(m) + "-" + str(d) + "-" + str(y))