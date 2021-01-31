import sys

# 입력 (1 <= n <= 100)
n = int(sys.stdin.readline().strip())

nums = 1

# 행
for i in range(n):
    # 열
    for j in range(n):
        print(nums, end = " ")
        nums += 1
    print()
