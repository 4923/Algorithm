# 입력
n, m = map(int, input().split())
coordinates = [list(map(int, input().split())) for _ in range(m)]

# 격자 생성
grid = [[0] * n for _ in range(n)]

# 격자에 수 추가
cnt = 1
for coordinate in coordinates:
    x = coordinate[0] - 1
    y = coordinate[1] - 1

    grid[x][y] += cnt
    cnt += 1

# 출력
for row in grid:
    for col in range(n):
        print(row[col], end=" ")
    print()
