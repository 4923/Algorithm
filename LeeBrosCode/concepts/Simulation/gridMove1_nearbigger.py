'''
4 1 1
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
'''
import sys

# 입력
# n: 격자 크기, r for row / c for col: 시작 위치
n, r, c = tuple(map(int, sys.stdin.readline().strip().split()))
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# print(f'[INPUT CHECK]\n\tline 1 - n:{n} r:{r} c:{c}\n\tline 2 - grid:{grid}')

# 변수
# 이동하는 숫자 목록
visited_nums = []

# 이동 조건1 : 격자 범위 안
def InRange(x, y):
    return 1 <= x <= n and 1 <= y <= n

# 이동 조건2 : 현 위치보다 더 큰 수
def CanGo(x, y, compare):
    return InRange(x, y) and grid[x][y] > compare

# 이동
def simulate():
    global r, c

    # 우선 순위: 상 > 하 > 좌 > 우
    dxs=[1,-1, 0, 0]
    dys=[0, 0, -1, 1]

    # zip: [1,-1, 0, 0]와 [0, 0, 1, -1]를 인덱스끼리 묶는다.
    # 결과: (dx, dy) = (1, 0) (-1, 0) ... ...
    for dx, dy in zip(dxs, dys):
        # 새 위치
        next_x, next_y = r + dx, c + dy

        # 갈 수 있는 곳일 때 -> true
        if CanGo(next_x, next_y, grid[r][c]):
            r, c = next_x, next_y
            return True
        
    # 갈 수 없는 경우
    return False

def main():
    for i in range(1, n+1):
        given_row = list(map(int, input().split()))
        for j, e in enumerate(given_row, start = 1):
            grid[i][j] = e

    # 초기 위치의 숫자 입력
    visited_nums.append(grid[r][c])

    while True:
        # 조건에 따라 이동
        greater_number_exist = simulate()

        # 종료 조건: 더 이상 움직일 수 없을 때 까지
        if not greater_number_exist:
            break

        # 움직이고 난 후의 위치 입력
        visited_nums.append(grid[r][c])
    
    # 출력
    for visited_num in visited_nums:
        print(visited_num, end = '')

if __name__ == '__main__':
    main()

