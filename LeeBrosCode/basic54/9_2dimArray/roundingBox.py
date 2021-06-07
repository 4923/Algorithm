import sys

# 입력
n = int(sys.stdin.readline().strip())

# 격자 생성
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
