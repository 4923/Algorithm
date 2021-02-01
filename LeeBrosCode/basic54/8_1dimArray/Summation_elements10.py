import sys

numbers = list( map(int, sys.stdin.readline().strip().split()))

print(sum(numbers))