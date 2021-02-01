import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, 10):
    print(numbers.count(i))
    