import sys

# input
# define a, b
a, b = map(int, sys.stdin.readline().strip().split())

# output
# print(f'{a}\n{b}')
sys.stdout.write(str(a) +'\n' + str(b))