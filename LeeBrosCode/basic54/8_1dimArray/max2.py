import sys

# 입력
n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

# 정렬
numbers.sort(reverse=True)

# 출력
[print(number, end=" ") for number in numbers[0:2]]
