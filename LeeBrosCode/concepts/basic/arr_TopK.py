# Top K 숫자 구하기

import sys

# input
N, k = map(int, sys.stdin.readline().strip().split())
ints = list(map(int, sys.stdin.readline().strip().split()))

# solution
new = sorted(ints)

# output
print(new[k - 1])
