# n개의 숫자 중 최소

import sys

# input
n = int(sys.stdin.readline())  # int
ints = [int(e) for e in sys.stdin.readline().split()]  # list, str

'''
# solution 1 : Use first index
# 5ms 76MB
counts = 0
minimum = ints[0]
for i in range(0, n):
    if minimum >= ints[i]:
        minimum = ints[i]

for i in range(0,n):
    if minimum == ints[i]:
        counts += 1
        
print(f'{minimum} {counts}')
'''

# solution 2 : Use sys.maxsize
# 4ms 76MB
MIN = sys.maxsize
for i in range(0,n):
    if ints[i] < MIN:
        MIN = ints[i]

print(f'{MIN} {ints.count(MIN)}')