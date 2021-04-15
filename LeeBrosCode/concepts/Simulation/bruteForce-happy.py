# 살펴보기
# 숫자의 개수 1~100, 격자의 크기 n*n
# 행복한 수열 : 연속하여 m개 이상의 동일한 수가 나오는 수열
# 전체 수열이 n개인 이유 : 가로로 n개 + 세로로 n개 (정방행렬이므로)
# 열탐색하면서 연속되는 수 일경우 cnt += 1씩 추가하는 방식, 열탐색이므로 O(n2)

import sys

# 1. 입력
SIZE, X = map(int, sys.stdin.readline().strip().split())  # n, m
grid = [
    list(map(int, sys.stdin.readline().strip().split()))
    for _ in range(SIZE)
]

# 2. 격자 탐색

# 격자 우측으로 90도 돌리기
def rollGrid(grid):
    grid2 = [ [] for _ in range(SIZE) ]
    for row in range(SIZE):
        for col in range(SIZE):
            grid2[row].append(grid[col][row])
    return grid2
            
# 인자 number의 연속을 확인하는 함수 isContinued

# 1~100까지 연속을 확인

# 3. 행복한 수열의 수 출력