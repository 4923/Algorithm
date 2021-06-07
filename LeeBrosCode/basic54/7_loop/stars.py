import sys

# 입력
n = int(sys.stdin.readline().strip())

# 출력
for i in range(1, 2 * n):  # 줄
    if i < n:
        print(f'{ " " * (n-i) }{ "*" * (i*2-1) }{ " " * (n-i-2) }')
    elif i == n:
        print("*" * (i * 2 - 1))
    else:
        i -= n
        print(f'{ " " * i }{ "*" * (2*n - 2*i -1) }{ " " * i }')

"""
n == 2
[1] 공백 1 별 1 공백 1
[2] 공백 0 별 3 공백 0
[3] 공백 1 별 1 공백 1

n == 3
[1] 공백 2 별 1 공백 2
[2] 공백 1 별 3 공백 1
[3] 공백 0 별 5 공백 3
[4] 공백 1 별 3 공백 1
[5] 공백 2 별 1 공백 2
"""
