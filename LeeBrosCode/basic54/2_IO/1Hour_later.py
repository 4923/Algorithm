import sys

# input
# form = h:m (1 ≤ h ≤ 22, 0 ≤ m < 60)
h, m = map(int, sys.stdin.readline().strip().split(":"))

# 1 hour after {time}
h += 1

# output
sys.stdout.write(str(h)+":"+str(m))