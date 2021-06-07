import sys

# INPUT
N = int(sys.stdin.readline())

grid = [
    list(map(int, sys.stdin.readline().strip().split()))  # list로 따로 묶어줘야 이차원 배열이 된다.
    for _ in range(N)  # 0, N으로 범위 지정하지 않아도 된다.
]

# Count Gold
def Count_Gold(start_row, start_col, end_row, end_col):
    cnt = 0
    for i in range(start_col, end_col):
        for j in range(start_row, end_row):
            # 1 0일때가 안나오는데? => main에서 row, col 각각 for문 돌려야 함. (for문 총 4개 사용)
            # print(f'\t[Check] i is {i}, j is {j}\n\t\tand the grid coordinate is \tgrid[{i}][{j}]\t which is {grid[i][j]}')
            if grid[i][j] == 1:
                # i가 2일때 j가 1을 건너뛰는데...
                cnt += 1
                # print(f'\t[Variable] cnt == [{cnt}] NOW')
    return cnt


# print(grid, Count_Gold(0,0,N,N))  # 3 == N, end_row & end_col == N

# Main
def main():
    MAX = Count_Gold(0, 0, 3, 3)  # baseCase
    # print(MAX)
    # print("--------------------------MAIN START----------------------------")
    for k in range(N):
        # print(f'K is {k}')
        for t in range(N):
            start_row = k
            start_col = t
            end_row = k + 3
            end_col = t + 3
            if end_row > N or end_col > N:
                # print(f'[!!ANSWER!!] {MAX}')
                break  # break 걸고 => for문 다 빠져나간 후 MAX 한번만 출력
            elif MAX < Count_Gold(start_row, start_col, end_row, end_col):
                # print("-------------------------------")
                # print(f'[Gold Check] Max gold is {MAX} and init gold is {Count_Gold(start_row, start_col, end_row, end_col)}')
                # print(f'{MAX} => {Count_Gold(start_row, start_col, end_row, end_col)}')
                # print("-------------------------------")
                MAX = Count_Gold(start_row, start_col, end_row, end_col)

    print(MAX)  # OUTPUT


if __name__ == "__main__":
    main()
