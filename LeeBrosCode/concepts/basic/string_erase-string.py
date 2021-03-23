'''
A = aabbaa
B = ab

1. substring of A started at A[1] is matched with B
2. Erase 'ab' of A. abaa remained
3. Erase 'ab' of remained A. aa remained
4. Stop erasing
'''

import sys

# [*] string can't be edited
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

while True:
    ind = A.find(B)
    if ind != -1:
        A = A[:ind] + A[ind+len(B):]
    else:
        print(A)
        break
