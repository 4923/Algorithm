# 1. Use `**` : base ** exponent
# 2. Use pow(base, exponent)

import sys

# input
# 1 <= n<= 100000
n = int(sys.stdin.readline())

# output
# sys.stdout.write(str(n**2))
sys.stdout.write(str(pow(n,2)))